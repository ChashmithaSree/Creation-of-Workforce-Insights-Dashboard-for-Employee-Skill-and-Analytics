import os

from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="AI Workforce Management System",
    description="Backend API for Workforce Analytics and Talent Intelligence",
    version="1.0.0"
)

# Connect to MongoDB
mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)

db = client["workforce_db"]


@app.get("/")
def home():
    return {
        "message": "AI Workforce Management System API is running!"
    }


@app.get("/health")
def health_check():
    try:
        client.admin.command("ping")

        return {
            "status": "healthy",
            "mongodb": "connected"
        }

    except Exception as e:
        return {
            "status": "unhealthy",
            "mongodb": "connection failed",
            "error": str(e)
        }

@app.get("/employees")
def get_employees():

    employees = list(
        db["employees"].find(
            {},
            {"_id": 0}
        )
    )

    return {
        "total": len(employees),
        "employees": employees
    }
@app.get("/attendance")
def get_attendance():

    attendance = list(
        db["attendance"].find(
            {},
            {"_id": 0}
        )
    )

    # Replace NaN values with None
    for record in attendance:
        for key, value in record.items():
            if isinstance(value, float) and value != value:
                record[key] = None

    return {
        "total": len(attendance),
        "attendance": attendance
    }