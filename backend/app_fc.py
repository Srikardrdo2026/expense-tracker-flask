from flask_cors import CORS
from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from werkzeug.security import check_password_hash, generate_password_hash
from bson.objectid import ObjectId
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "../frontend")  # Adjusted for backend location

app = Flask(__name__, template_folder=TEMPLATE_DIR)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "your_secret_key_here")

FRONTEND_URL = "http://localhost:5173/"

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_CLUSTER = os.getenv("MONGO_CLUSTER")
MONGO_DB = os.getenv("MONGO_DB")

MONGO_URI = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_CLUSTER}/{MONGO_DB}?retryWrites=true&w=majority"

# Ensure sensitive environment variables are properly configured
if not all([MONGO_USER, MONGO_PASSWORD, MONGO_CLUSTER, MONGO_DB]):
    raise ValueError("MongoDB environment variables are not properly configured.")

try:
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DB]
except Exception as e:
    raise ConnectionError(f"Failed to connect to MongoDB: {e}")

users_collection = db["users"]
budgets_collection = db["budgets"]
expenses_collection = db["expenses"]

# Allow CORS from your frontend URL only, with credentials support
CORS(app, supports_credentials=True, origins=[FRONTEND_URL])

# Improve session security
app.config.update(
    SESSION_COOKIE_SECURE=True,  # Ensures cookies are sent over HTTPS
    SESSION_COOKIE_HTTPONLY=True,  # Prevents JavaScript access to cookies
)

@app.route("/", methods=["GET"])
def serve_frontend():
    # Redirect to your frontend hosted URL
    return redirect(FRONTEND_URL)
