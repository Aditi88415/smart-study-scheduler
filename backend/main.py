from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from ml_model import predict_schedule
from database import insert_user_data

app = FastAPI()

# CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5500"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StudyData(BaseModel):
    subject: str
    exam_date: str
    difficulty: int
    available_hours: float

@app.post("/predict_schedule")
def get_schedule(data: StudyData):
    schedule = predict_schedule(data.subject, data.exam_date, data.difficulty, data.available_hours)
    insert_user_data(data)
    return {"schedule": schedule}

@app.get("/")
def read_root():
    return {"message": "Smart Study Scheduler Backend is working!"}
