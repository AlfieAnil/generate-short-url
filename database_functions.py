import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi
from bson.objectid import ObjectId
from dotenv import load_dotenv

load_dotenv()

cert = certifi.where()

# Connecting to MongoDB
client = MongoClient(os.getenv('MONGO_DB_URL'), server_api=ServerApi('1'), tlsCAFile=cert)
db = client.urls_db

def insert_url(url):
    try:
        result = db.urls.insert_one({'url': url})
        return result.inserted_id
    except Exception as e:
        print("Exception : ", e)

def find_url(url_id):
    print(url_id)
    result = db.urls.find_one({'_id': ObjectId(url_id)})
    print("Result: ", result['url'])
    return result['url']