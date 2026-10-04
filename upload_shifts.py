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
collection = db["shifts"]

# Read shifts CSV
df = pd.read_csv("shifts.csv")

# Convert to dictionaries
shift_records = df.to_dict("records")

print("Records to upload:", len(shift_records))

# Upload to MongoDB
result = collection.insert_many(shift_records)

print("Shift data uploaded successfully!")
print("Number of records inserted:", len(result.inserted_ids))