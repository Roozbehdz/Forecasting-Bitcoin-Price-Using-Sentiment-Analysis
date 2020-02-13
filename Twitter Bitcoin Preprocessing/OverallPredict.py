import pandas as pd 
import matplotlib.pyplot as plt

from mongo_sentiment_query_df import mongo_sentiment_query_df
from mongo_bitcoin_query_df import mongo_bitcoin_query_df

from numpy import *
from numpy.core._multiarray_umath import isnan
tweet =mongo_sentiment_query_df('Comulative-Data','10-18 to 11-23')

tweet = tweet.set_index('Time')
tweet.index = pd.to_datetime(tweet.index)

bitcoin = pd.read_csv(r'C:/Users/10/Documents/GitLab - Karo/ForecastingBitcoinPrice/#price/XBTUSD-1m-data.csv',
                                            index_col=0, 
                                            parse_dates=True,
                                            usecols=['timestamp','close'],
                                            squeeze=True)
bitcoin = bitcoin.to_frame()
list_num = ['5T','10T','15T','30T', '45T','60T','120T']

bitcoin = bitcoin['2019-10-18':'2019-11-23']

print('Start')

for item in list_num :

    tweet_temp = tweet

    tweet_temp = tweet_temp.resample(item).sum()

    bitcoin.index = pd.to_datetime(bitcoin.index)
    bitcoin_temp = bitcoin
    bitcoin_temp = bitcoin_temp.resample(item).mean()

    tweet_temp = tweet_temp.diff().diff()
    bitcoin_temp = bitcoin_temp.diff().diff().shift(-3)

    where_are_NaNs = isnan(tweet_temp)
    tweet_temp[where_are_NaNs] = 0
    where_are_NaNs = isnan(bitcoin_temp)
    bitcoin_temp[where_are_NaNs] = 0

    # print(bitcoin_temp)
    # print(tweet_temp)
    predict = []
    predict = tweet_temp['Sentiment']*bitcoin_temp['close']
    # print(predict)

    correct_predict = 0

    for item_2 in range(len(predict)):
        if predict[item_2] > 0:
            correct_predict += 1

    print(correct_predict/len(predict)*100,len(predict),' ',item)




