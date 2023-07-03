import os
import pymongo
from dotenv import load_dotenv
load_dotenv()

try:
    client = pymongo.MongoClient(os.getenv("DB_URL"))
    db = client['studentsDB']
except:
    print("Error Connecting to database")