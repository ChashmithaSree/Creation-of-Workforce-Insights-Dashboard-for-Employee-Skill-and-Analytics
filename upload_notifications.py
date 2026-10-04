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

collection = db["notifications"]

df = pd.read_csv("notifications.csv")

notification_records = df.to_dict("records")

print("Records to upload:", len(notification_records))

result = collection.insert_many(notification_records)

print("Notifications data uploaded successfully!")
print("Number of records inserted:", len(result.inserted_ids))