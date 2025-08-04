# 💰 Expense Tracker Web App

## 📖 Project Overview

**Expense Tracker Web App** is a fully functional personal finance management system developed using **Python Flask** for the backend and **MongoDB** for the database. The application allows users to **sign up and log in securely**, manage their **monthly budgets**, and **track daily expenses** through a clean and minimal dashboard interface.

This project was built with the goal of understanding and implementing **full-stack development using Flask**, including RESTful routing, authentication, MongoDB integrations, and static frontend templating. While the frontend uses **static HTML and CSS**, the backend is structured in a modular and scalable way with separate routes for authentication, budget management, and expense tracking.

Key highlights of the project include a clean separation between backend and frontend logic, proper use of JWT-based authentication, and extensible design to support future additions like analytics, charts, or cloud deployment.

Whether you're managing your personal finances or exploring Flask with MongoDB, this project serves as a practical example of how to build and organize a complete web application from scratch.

---

## 📸 Screenshots

### 🔐 Login Page

![Login](screenshots/login.png)

### 📝 Sign Up Page

![Sign Up](screenshots/signup.png)

### 📊 Dashboard

![Dashboard](screenshots/dashboard.png)

---

## 🚀 Features

* 🔐 User Registration and Login (JWT Auth)
* ➕ Add Budget and Expense
* 🗂️ View Expense History
* 🔄 Reset All Entries
* 📉 See Total Budget, Total Expenses, and Remaining Budget
* 🧩 Modular Flask backend (converted from FastAPI structure)

---

## 🛠 Tech Stack

### Backend

* Python Flask
* MongoDB (Localhost)
* Flask-JWT-Extended (Authentication)
* WebSocket (for future real-time updates)

### Frontend

* HTML5
* CSS3 (Static styling)
* Vanilla JavaScript (optional client-side interactivity)

---

## 📂 Project Structure

```
expense-tracker/
├── backend/
│   ├── app_fc.py              # Frontend entry Flask app
│   ├── app_bc.py              # Backend Flask app logic
│   ├── config.py              # App config
│   ├── models.py              # MongoDB schema
│   ├── database.py            # DB connection
│   ├── auth.py                # JWT authentication logic
│   ├── websocket.py           # (Optional) WebSocket setup
│   └── routes/
│       ├── users.py           # User routes
│       ├── expenses.py        # Expense routes
│       └── budgets.py         # Budget routes
├── frontend/
│   ├── index.html             # Login & Signup UI
│   └── dashboard.html         # Budget & Expense UI
└── screenshots/
    ├── login.png
    ├── signup.png
    └── dashboard.png
```

---

## 💻 How to Run Locally

### ⚙️ Prerequisites

* Python 3.x
* MongoDB running locally
* `pip` installed

### ▶️ Steps

```bash
git clone https://github.com/Srikardrdo2026/expense-tracker-flask.git
cd expense-tracker-flask/backend

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # For Linux/Mac: source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Add .env file with your Mongo URI and secret key
# Run the Flask app
python app_fc.py
```

Open the frontend in your browser using `index.html` (you may use Live Server or just double-click it).

---

## 📌 Author

* GitHub: [@Srikardrdo2026](https://github.com/Srikardrdo2026)

---

## 🌟 Star the Repo

If you found this project helpful, consider giving it a ⭐️!
