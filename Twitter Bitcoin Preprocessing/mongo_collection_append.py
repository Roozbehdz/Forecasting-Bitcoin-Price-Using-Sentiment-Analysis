from pymongo import MongoClient
from mongo_query import mongo_query
from mongo_push_data import mongo_push_data


client = MongoClient()

def mongo_collection_append(database,collection,Comulative_db,Comulative_collection):

    #query database

    temp  = mongo_query(database,collection).find()

    #push  data
    
    db = client[Comulative_db]
    data_db = db[Comulative_collection]

    data_db.insert(temp)

dates = ['2019-10-18', '2019-10-19', '2019-10-20', '2019-10-21',
         '2019-10-22', '2019-10-23', '2019-10-24', '2019-10-25',
         '2019-10-26', '2019-10-27', '2019-10-28', '2019-10-29',
         '2019-10-30', '2019-10-31', '2019-11-01', '2019-11-02',
         '2019-11-03', '2019-11-04', '2019-11-05', '2019-11-06',
         '2019-11-07', '2019-11-08', '2019-11-09', '2019-11-10', 
         '2019-11-11', '2019-11-12', '2019-11-13', '2019-11-14',
         '2019-11-15', '2019-11-16', '2019-11-17', '2019-11-18',
         '2019-11-19', '2019-11-20', '2019-11-21', '2019-11-22', 
         '2019-11-23'
         ]

num = 0 
for date in dates :
    mongo_collection_append('Tweets-no-RT',date,'Comulative-Data','10-18 to 11-23')
    num += 1
    print(date,' Overall Progress : '+str(num/len(dates)*100))