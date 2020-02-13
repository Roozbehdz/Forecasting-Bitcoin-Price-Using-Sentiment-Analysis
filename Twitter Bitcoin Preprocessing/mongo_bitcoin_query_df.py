from pymongo import MongoClient
import pandas as pd

def mongo_bitcoin_query_df(database,collection):
    client = MongoClient()
    db = client[database]
    data_db = db[collection]

    times = [] # create an empty list for TIMEs
    prices = [] # create an empty list for TWEETs
    

    for doc in data_db.find():

        times += [doc["timestamp"]]
        prices+= [doc["close"]]
        
    df = pd.DataFrame(
        {'Time': times,
        'ClosePrice': prices
        })

    return df
