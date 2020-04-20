from tweepy import API 
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from textblob import TextBlob
 
import twitter_credentials

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re

import csv
import urllib.request


# # # # TWITTER CLIENT # # # #
class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client

    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_friend_list(self, num_friends):
        friend_list = []
        for friend in Cursor(self.twitter_client.friends, id=self.twitter_user).items(num_friends):
            friend_list.append(friend)
        return friend_list

    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets = []
        for tweet in Cursor(self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets

    def get_hashtag_tweets (self, hashtag, num_tweets):
        hashtag_tweets = []
        for tweet in Cursor(api.search,q=hashtag,id=self.twitter_user).items(num_tweets):
            hashtag_tweets.append(tweet)
        return hashtag_tweets


# # # # TWITTER AUTHENTICATER # # # #
class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth



class TweetAnalyzer():
    """
    Puting tweets inside a dataframe
    """

    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
        
    def tweets_to_data_frame(self, tweets):
        df = pd.DataFrame(data=[tweet.full_text for tweet in tweets], columns=['tweets'])

        #csvFile = open('hashtag.csv', 'a')
        #csvWriter = csv.writer(f)
    
        df['id'] = np.array([tweet.id for tweet in tweets])
        df['len'] = np.array([len(tweet.full_text) for tweet in tweets])
        df['date'] = np.array([tweet.created_at for tweet in tweets])
        df['source'] = np.array([tweet.source for tweet in tweets])
        df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
        df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
        df.to_csv('hashtag.csv', header=None, index=None, sep='\t', mode='a')
        #np.savetxt('test.txt', df.values, fmt='%d', delimiter='\t')
        '''
        with open('hashtag.csv', 'w',newline='') as f:
            fieldnames = ['ID','text','length','date','source','likes','retweets']
            csvWriter = csv.DictWriter(f,fieldnames)
            csvWriter.writeheader()
            for tweet in tweets:
                tweetID = ([tweet.id])
                tweetText = ([tweet.text])
                length= ([len(tweet.text)])
                date = np.array([tweet.created_at])
                source = ([tweet.source])
                likes= ([tweet.favorite_count])
                retweets= ([tweet.retweet_count])
                csvWriter.writerow({'ID':tweetID,'text':tweetText,'length':length,'date':date,'source':source,'likes':likes,'retweets':retweets})
        '''
        return df

 
if __name__ == '__main__':

    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()

    csvFile = open('hashtag.csv', 'a')
    csvWriter = csv.writer(csvFile)

    api = twitter_client.get_twitter_client_api()
    #for tweet in Cursor(api.search,q="#CoronaVirusArv",count=200, lang="en",since="2020-04-03",tweet_mode='extended').items():
        #csvWriter.writerow([tweet.full_text.encode('utf-8')])
        #print (tweet.full_text)
    #tweets = api.user_timeline(screen_name="realDonaldTrump",count=50,tweet_mode='extended',include_entities=True)
    tweets = (api.search(q='#Covid_19 -filter:retweets',lang='en',count=50,tweet_mode='extended',include_entities=True))
    imageTweets = []
    videoTweets = []
    imageUrl = []
    for tweet in tweets:
        if 'media' in tweet.entities:
            i = 0
            for image in tweet.entities['media']:
                imageTweets.append([tweet.id,tweet.entities['media'][0]['media_url']])
                #imagename='image-{}.jpg'.format(i)
                #imageUrl = urllib.request.urlretrieve(tweet.entities['media'][0]['media_url'],imagename)
                imageUrl.append(tweet.entities['media'][0]['media_url'])
                
            for iurl in imageUrl:
                print(iurl)
                imagename='image-{}.jpg'.format(i)
                #Uncomment next line to download imagens
                #urllib.request.urlretrieve(iurl,imagename)
                i+=1
                
        #if 'extended_entities' in tweet.extended_entities.get("media", [{}]) :
        j=0
        for video in tweet.entities.get("video", []):
            if video.get("type", None) == "video":                
                videoTweets.append(tweet.id,video["video_info"]["variants"][0]["url"])
            j+=1
            
    #tweets = api.user_timeline(screen_name="realDonaldTrump",count=50)
    #print(imageTweets)
    print(videoTweets)
    df = tweet_analyzer.tweets_to_data_frame(tweets)
    print (df.head(10))
    #df = tweet_analyzer.tweets_to_data_frame(tweets)
    #df['sentiment'] = np.array([tweet_analyzer.analyze_sentiment(tweet) for tweet in df['tweets']])

    #print(df.head(10))