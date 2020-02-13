import sys
sys.path.append('/MongoDB/')


from mongo_push_data import  mongo_push_data
from mongo_delete_retweets import  mongo_delete_retweets


def mongo_update(date):

    #push tweet json file to Tweets database

    file_path = 'C:/Users/10/Documents/GitLab - Karo/ForecastingBitcoinPrice/#bitcoin' + '/#bitcoin_' + date + '.json'

    mongo_push_data('Tweets',date,file_path)

    #push tweet json file to Tweets-no-RT database
    
    mongo_push_data('Tweets-no-RT',date,file_path)

    #delete Tweet-no-RT database retweets

    mongo_delete_retweets(date)

# dates = ['2019-10-18', '2019-10-19', '2019-10-20', '2019-10-21',
#          '2019-10-22', '2019-10-23', '2019-10-24', '2019-10-25',
#          '2019-10-26', '2019-10-27', '2019-10-28', '2019-10-29',
#          '2019-10-30', '2019-10-31', '2019-11-01', '2019-11-02',
#          '2019-11-03', '2019-11-04', '2019-11-05', '2019-11-06',
#          '2019-11-07', '2019-11-08', '2019-11-09', '2019-11-10', 
#          '2019-11-11', '2019-11-12', '2019-11-13', '2019-11-14',
#          '2019-11-15', '2019-11-16', '2019-11-17', '2019-11-18',
#          '2019-11-19', '2019-11-20', '2019-11-21', '2019-11-22', 
#          '2019-11-23'
#          ]



for date in dates :
    mongo_update(date)