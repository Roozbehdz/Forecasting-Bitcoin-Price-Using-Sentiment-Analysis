from mongo_query import mongo_query
import pymongo
import pandas as pd



def mongo_sort(database, collection ,phrase = 'retweet_count', num = 100):
    
    results = mongo_query(database,collection).find().sort([
            (phrase, pymongo.DESCENDING)
            ]).limit(num)


    times = [] 
    tweets = []
    ids = []
    ret_counts = []
    user_id = []
    user_name = []
    user_screen_name = []
    follower_counts = []


    for result in results:

        times += [result["created_at"]]
        tweets+= [result["text"]]
        ids+= [result["id"]]
        ret_counts+= [result["retweet_count"]]
        user_id += [result["user"]["id"]]
        user_name += [result["user"]["name"]]
        user_screen_name += [result["user"]["screen_name"]]
        follower_counts += [result["user"]["followers_count"]]

        df = pd.DataFrame(
            {'Time': times,
            'Tweet': tweets,
            'ID': ids,
            'Retweet Count': ret_counts,
            'user_id': user_id,
            'user_name' : user_name,
            'user_screen_name' : user_screen_name,
            'follower_counts' : follower_counts,
            })
    
    return df


collections = [ 'October 18th','October 19th','October 20th',
                'October 21st','October 22nd','October 23rd',
                'October 24th','October 25th','October 26th',
                'October 27th','October 28th','October 29th',
                'October 30th','October 31st','November 1st',
                'November 2nd','November 3rd']

for collection in collections:
    df = mongo_sort('Tweets-no-RT',collection,'user.followers_count',200)
    df.to_csv(str('sorted_tweets'+ collection + '.csv'))
    print(collection)
