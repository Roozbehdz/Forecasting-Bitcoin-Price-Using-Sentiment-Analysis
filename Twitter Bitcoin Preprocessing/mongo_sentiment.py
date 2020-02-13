import mongo_query
import pymongo
import sentiment_analyst




mycol = mongo_query.mongo_query('Comulative-Data','10-18 to 11-23')

results = mycol.find()

num = 0
for result in results :
    
    temp = sentiment_analyst.sentiment_analyzer_scores(result['text'])['compound']

    mycol.update({"_id": result["_id"]}, {"$set": {"sentiment": temp}})

    num += 1
    print(num)