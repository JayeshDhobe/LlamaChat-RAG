# db.py
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
DB_NAME = os.getenv('DB_NAME', 'yogadb')
if '/' not in MONGO_URI.split('/')[-1]:
    MONGO_URI = f"{MONGO_URI}/{DB_NAME}"
client = MongoClient(MONGO_URI)
db = client[DB_NAME]