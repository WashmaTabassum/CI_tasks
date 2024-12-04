from pymongo import MongoClient, ASCENDING, DESCENDING
from datetime import datetime
connection_string = "mongodb://localhost:27017"

def save_chat(data:dict):
    data["timestamp"] = datetime.now()
    with MongoClient(connection_string) as client:
        client["UET"]["chat"].insert_one(data)

save_chat({
    # "user_id": "123",
    "role": "user",
    "content": "Hello"
})  
        
def fetch_chat(user_id):
    with MongoClient(connection_string) as client:
        return list(client["UET"]["chat"].find(
            {"user_id": user_id }
        ).sort("timestamp", ASCENDING))
        
      
        
        
    