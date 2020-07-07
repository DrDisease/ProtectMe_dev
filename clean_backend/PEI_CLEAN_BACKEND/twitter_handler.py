from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener as SL
from tweepy import OAuthHandler as OA
from tweepy import Stream

from textblob import TextBlob as TB

import twitter_credentials

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re

import csv
import urllib.request


# # # # TWITTER CLIENT # # # #
class TwitterClient:
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.client = API(self.auth)
        self.user = twitter_user

    def get_twitter_client_api(self):
        return self.client

    def get_user_timeline_tweets(self, n):
        tweets = []
        for tweet in Cursor(self.client.user_timeline, id=self.user).items(n):
            tweets.append(tweet)
        return tweets

    def get_friend_list(self, n):
        friends = []
        for friend in Cursor(self.client.friends, id=self.user).items(n):
            friends.append(friend)
        return friends

    def get_home_timeline_tweets(self, n):
        tweets = []
        for tweet in Cursor(self.client.home_timeline, id=self.user).items(n):
            tweets.append(tweet)
        return tweets

    def get_tag_tweets(self, tag, n):
        tweets = []
        for tweet in Cursor(self.client.search, q=tag, id=self.user).items(n):
            tweets.append(tweet)
        return tweets

    def get_tweet(self, url):
        id = url.split("/")[-1]
        return self.client.get_status(id, tweet_mode="extended")

    def get_tweet_from_id(self, id):
        return self.client.get_status(id, tweet_mode="extended")



# # # # TWITTER AUTHENTICATER # # # #
class TwitterAuthenticator:
    def authenticate_twitter_app(self):
        auth = OA(
            twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET
        )
        auth.set_access_token(
            twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET
        )
        return auth

class TweetAnalyzer:
    """
    Puting tweets inside a dataframe
    """

    def clean_tweet(self, tweet):
        return " ".join(
            re.sub(
                "(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet
            ).split()
        )

    def tweets_to_data_frame(self, tweets):
        df = pd.DataFrame(
            data=[tweet.full_text for tweet in tweets], columns=["tweets"]
        )

        # csvFile = open('hashtag.csv', 'a')
        # csvWriter = csv.writer(f)

        df["id"] = np.array([tweet.id for tweet in tweets])
        df["len"] = np.array([len(tweet.full_text) for tweet in tweets])
        df["date"] = np.array([tweet.created_at for tweet in tweets])
        df["source"] = np.array([tweet.source for tweet in tweets])
        df["likes"] = np.array([tweet.favorite_count for tweet in tweets])
        df["retweets"] = np.array([tweet.retweet_count for tweet in tweets])
        df.to_csv("hashtag.csv", header=None, index=None, sep="\t", mode="a")
        # np.savetxt('test.txt', df.values, fmt='%d', delimiter='\t')
        """
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
        """
        return df

    