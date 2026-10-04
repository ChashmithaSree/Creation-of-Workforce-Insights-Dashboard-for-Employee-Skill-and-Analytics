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

# Select database and collection
db = client["workforce_db"]
collection = db["leave_requests"]

# Read CSV
df = pd.read_csv("leave_requests.csv")

# Convert to dictionaries
leave_records = df.to_dict("records")

print("Records to upload:", len(leave_records))

# Upload to MongoDB
result = collection.insert_many(leave_records)

print("Leave data uploaded successfully!")
print("Number of records inserted:", len(result.inserted_ids))