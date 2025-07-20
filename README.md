# 📚 Smart Study Scheduler

This web app helps students estimate how many hours they should study per day based on their exam date, difficulty level, and available hours.

It features a clean interface, a machine learning-based schedule predictor (via FastAPI + TensorFlow), and a live countdown to the exam day.

---

## 🚀 Features

✅ Enter subject, exam date, difficulty level, and available hours  
✅ Predict how many hours/day to study using ML  
✅ Countdown timer shows days left until the exam  
✅ Simple and responsive UI using Tailwind CSS  
✅ FastAPI backend using Python  
✅ No user login, no database — beginner-friendly!

---

## 🛠 Tech Stack

| Part       | Technology              |
|------------|--------------------------|
| Frontend   | HTML, Tailwind CSS, JS   |
| Backend    | Python, FastAPI          |
| Prediction | TensorFlow (basic logic) |

---

## 📂 Folder Structure

study-scheduler/
├── backend/
│ ├── main.py
│ ├── ml_model.py
│ ├── database.py
│
├── frontend/
│ ├── index.html
│ ├── tailwind.css
│ ├── output.css
│ ├── package.json
│ ├── tailwind.config.js
│
└── README.md

---

## ⚙️ How to Run Locally


1. Backend Setup
cd backend
python -m venv venv
# Windows:
venv\Scripts\activate
# Install dependencies
pip install fastapi uvicorn tensorflow
# Run server
uvicorn main:app --reload
2. Frontend Setup
cd frontend
npm install
npm run dev

##How It Works
1.User submits form (subject, exam date, etc.)
2.Data sent to FastAPI backend
3.TensorFlow model calculates hours/day
4.Countdown shows days left till exam
