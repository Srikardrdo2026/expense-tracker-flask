from flask import Flask, send_from_directory, abort
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Define template directory (frontend static files)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "../frontend")

# Initialize Flask app
app = Flask(__name__, template_folder=TEMPLATE_DIR)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "your_secret_key_here")

# MongoDB configuration
MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_CLUSTER = os.getenv("MONGO_CLUSTER")
MONGO_DB = os.getenv("MONGO_DB")

# Check for required env vars
if not all([MONGO_USER, MONGO_PASSWORD, MONGO_CLUSTER, MONGO_DB]):
    raise ValueError("MongoDB environment variables are not properly configured.")

# MongoDB connection
MONGO_URI = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_CLUSTER}/{MONGO_DB}?retryWrites=true&w=majority"
try:
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DB]
except Exception as e:
    raise ConnectionError(f"Failed to connect to MongoDB: {e}")

# Collections
users_collection = db["users"]
budgets_collection = db["budgets"]
expenses_collection = db["expenses"]

# CORS configuration
CORS(app, supports_credentials=True)

# Session security config
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
)

# Route: Homepage → serves index.html
@app.route("/")
def home():
    return send_from_directory(TEMPLATE_DIR, "index.html")

# Route: Dashboard → serves dashboard.html
@app.route("/dashboard")
def dashboard():
    return send_from_directory(TEMPLATE_DIR, "dashboard.html")

# Fallback: Serve any other HTML files (optional, like /about.html)
@app.route("/<path:filename>")
def serve_static(filename):
    file_path = os.path.join(TEMPLATE_DIR, filename)
    if os.path.exists(file_path):
        return send_from_directory(TEMPLATE_DIR, filename)
    else:
        abort(404)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
