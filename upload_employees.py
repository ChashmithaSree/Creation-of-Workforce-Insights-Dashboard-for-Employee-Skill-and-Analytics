import os
import pandas as pd
from dotenv import load_dotenv
from pymongo import MongoClient

# Load MongoDB connection details from .env
load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

# Connect to MongoDB Atlas
client = MongoClient(mongo_uri)

# Select database
db = client["workforce_db"]

# Select collection
collection = db["employees"]

# Read the CSV file
df = pd.read_csv("employees.csv")

# Convert DataFrame rows into dictionaries
employees = df.to_dict("records")

# Insert all employees into MongoDB
result = collection.insert_many(employees)

print("Employees uploaded successfully!")
print("Number of employees inserted:", len(result.inserted_ids))