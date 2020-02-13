from pymongo import MongoClient
import pandas as pd

def mongo_sentiment_query_df(database,collection):
    client = MongoClient()
    db = client[database]
    data_db = db[collection]

    times = [] # create an empty list for TIMEs
    # tweets = [] # create an empty list for TWEETs
    sentiments = [] # create an empty list for SENTIMENTs

    for doc in data_db.find():

        times += [doc["created_at"]]
        # tweets+= [doc["text"]]
        sentiments +=[doc["sentiment"]]
    df = pd.DataFrame(
        {'Time': times,
        # 'Tweet': tweets,
        'Sentiment':sentiments
        })

    return df
