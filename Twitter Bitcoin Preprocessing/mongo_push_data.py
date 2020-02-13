from pymongo import MongoClient
import json

client = MongoClient()

def mongo_push_data(database,collection,file_path):
    db = client[database]
    data_db = db[collection]


    with open(file_path) as json_file:
        lines = json_file.readlines()
        
    # print(type(data))
    for line in range(len(lines)):
    
        data = json.loads(lines[line])
        result = data_db.insert_one(data)

