
import pandas as pd 
import matplotlib.pyplot as plt

from mongo_sentiment_query_df import mongo_sentiment_query_df
from mongo_bitcoin_query_df import mongo_bitcoin_query_df

tweet =mongo_sentiment_query_df('Comulative-Data','10-18 to 11-23')

tweet = tweet.set_index('Time')
tweet.index = pd.to_datetime(tweet.index)


bitcoin = pd.read_csv(r'C:/Users/10/Documents/GitLab - Karo/ForecastingBitcoinPrice/#price/XBTUSD-1m-data.csv',
                                            index_col=0, 
                                            parse_dates=True,
                                            usecols=['timestamp','close'],
                                            squeeze=True)
bitcoin = bitcoin.to_frame()

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

for date in dates:
    tweet_temp = tweet[date]
    
    tweet_temp = tweet_temp.resample('60T').sum()

    bitcoin.index = pd.to_datetime(bitcoin.index)

    bitcoin_temp = bitcoin[date]
    bitcoin_temp = bitcoin_temp.resample('60T').mean()

    tweet_temp = tweet_temp.diff()
    bitcoin_temp = bitcoin_temp.diff()

    plt.figure()
    plt.subplot(211)
    plt.plot(tweet_temp, 'r-')

    plt.xlabel('Time')
    plt.ylabel('Changes')
    plt.title(str('Sentiment~Price '+ date))
    plt.legend('Sentiment')
    plt.grid(True)

    plt.subplot(212)
    plt.plot(bitcoin_temp, 'b-')
    plt.xlabel('Time')
    plt.ylabel('Changes')
    plt.legend('Price')
    plt.grid(True)
    plt.savefig(str('Sentiment~Price B-1m-T60-M '+ date + ".png"))


