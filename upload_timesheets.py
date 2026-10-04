import os
import pandas as pd
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)

# Test connection
client.admin.command("ping")
print("MongoDB connection successful!")

# Select database
db = client["workforce_db"]

# Select collection
collection = db["timesheets"]

# Read CSV
df = pd.read_csv("timesheets.csv")

# Convert to MongoDB documents
timesheet_records = df.to_dict("records")

print("Records to upload:", len(timesheet_records))

# Insert into MongoDB
result = collection.insert_many(timesheet_records)

print("Timesheet data uploaded successfully!")
print("Number of records inserted:", len(result.inserted_ids))