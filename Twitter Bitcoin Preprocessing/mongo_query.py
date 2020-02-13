from pymongo import MongoClient

def mongo_query(database,collection):
    
    client = MongoClient()
    
    db = client[database]
    data_db = db[collection]

    return data_db