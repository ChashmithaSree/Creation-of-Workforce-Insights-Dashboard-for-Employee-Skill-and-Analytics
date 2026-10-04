import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

print("MONGO_URI loaded:", mongo_uri is not None)
print("Starts with:", mongo_uri[:20])

client = MongoClient(mongo_uri)

client.admin.command("ping")

print("MongoDB connection successful!")