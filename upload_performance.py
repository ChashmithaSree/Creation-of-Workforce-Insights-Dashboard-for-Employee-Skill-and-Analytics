import os
import pandas as pd
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)

client.admin.command("ping")
print("MongoDB connection successful!")

db = client["workforce_db"]

collection = db["performance"]

df = pd.read_csv("performance.csv")

performance_records = df.to_dict("records")

print("Records to upload:", len(performance_records))

result = collection.insert_many(performance_records)

print("Performance data uploaded successfully!")
print("Number of records inserted:", len(result.inserted_ids))