import os
import pandas as pd
import certifi
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(
    mongo_uri,
    tls=True,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=30000
)

# Test connection first
client.admin.command("ping")

print("MongoDB connection successful!")

db = client["workforce_db"]
collection = db["attendance"]

df = pd.read_csv("attendance.csv")

attendance_records = df.to_dict("records")

print("Records to upload:", len(attendance_records))

result = collection.insert_many(attendance_records)

print("Attendance data uploaded successfully!")
print("Number of records inserted:", len(result.inserted_ids))