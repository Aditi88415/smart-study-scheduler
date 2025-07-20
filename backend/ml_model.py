from datetime import datetime

def predict_schedule(subject, exam_date, difficulty, available_hours):
    today = datetime.today()
    exam = datetime.strptime(exam_date, "%Y-%m-%d")
    days_left = (exam - today).days
    recommended_hours = round(min(available_hours, (difficulty * 0.5)), 2)

    return {
        "subject": subject,
        "days_left": days_left,
        "recommended_hours_per_day": recommended_hours
    }
