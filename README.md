# Forecasting Bitcoin Price Using Twitter Sentimet Analysis


### Introduction
This project focuses on the relation between twitter sentiment and bitcoin price fluctuations. There has to be an unidentified correlation between the two of them as our studies suggest.Our approach toward this analysis is based on an article claiming that by gathering 2.25 million tweets they have achieved to 79% accuracy in predicting the direction of bitcoin changes(either increase or decrease).
This study consists of 3 different steps:

### Data collection:
1.1 Twitter Data Collection
  Tweets are extracted with a file called twitter_search.py which enables us to access twitter data for any given phrase or hashtag.

1.2 Bitcoin Data Collection :
  Bitcoin prices are gathered in a .csv file in periods of one minute, five minutes, one hour and one day using Bitmex API ranging from 26th of September 2015
 up until now.
### Preprocessing :
2.1 Data Type Converstion :
  This process just begins with converting  .json file which we have access to from the server to   the pandas data frame.

2.2 Text Cleaning :
  Then we try to clean the data and eliminate bots and identifying influencers through the power of preprocessor and nltk libraries

2.3 Sentiment Analysis :
  This cleaned data is sent to be processed based on sentiments using VADER lexicon.
### Modelling :
3.1 Time Series :
Using sentiments calculated in the last step, we apply the time series algorithm.

3.2 Tweet Volumes :
It is mentioned in a paper worked by Abraham et al. that the volume of tweets related to cryptocurrencies also can give us insight about probable bitcoin price
fluctuations