from mongo_query import mongo_query
import pymongo
import pandas as pd
import re

def mongo_delete_retweets(collection):
    
    RT = { "text": {"$regex": "^RT"} }

    results = mongo_query('Tweets-no-RT',collection).delete_many(RT)
    print(results.deleted_count, " documents deleted.", collection)
