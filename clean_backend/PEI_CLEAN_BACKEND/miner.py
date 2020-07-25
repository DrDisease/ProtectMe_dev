from db_connect import *
from procedures import *
from monkey import *
from spacy_example import *
from twitter_handler import *
from conf import *
import tweepy
from twython import Twython
from analyzer import analyze
from analyzer import get_media

def search_single_topic(topic,num):
    global handler
    data=[]
    counter=0 
    for tweet in tweepy.Cursor(handler.client.search,q=topic,count=100,
                               lang="en",
                               since="2017-04-03").items():
            counter = counter +1
            if counter > num:
                return data
            #print(tweet.favorite_count)
            data.append((tweet.id,tweet.entities,tweet.retweet_count))
    return data


#returns a dict with a list of tweets for each topic
def search_topics(topics, num):
    data= {}
    if topics==[]:
        return None
    for t in topics:
        data[t] = search_single_topic(t,num)
    return data

def insert_tweet(id,likes=0,comm=0,rt=0,relat=0):
    d=get_tweet_dict(id,0,likes,comm,rt)
    exists = db_insert("SELECT * FROM TWEETS WHERE id like'"+str(id)+"';").fetchone()
    print(exists)
    if exists is None:
        db_insert(add_tweet(d))

def insert_keywords(lst):
    for k in lst:
        exists = db_insert("SELECT * FROM TOPICS WHERE KEYWORD LIKE'"+str(k)+"';" ).fetchone()
        if exists is None: 
            db_insert(add_topic(str(k)))

def keyword_id(k):
    exists = db_insert("SELECT * FROM TOPICS WHERE KEYWORD LIKE'"+str(k)+"';" ).fetchone()
    if exists is None: 
        db_insert(add_topic(str(k)))
    else:
        return exists[0]


def insert_related(tweet_id,topic_id):
    db_insert(add_related(tweet_id,topic_id))


def insert_analysis(id):
    db_insert(add_analysis(id))

def insert_media(tweet_id,media_lst):
    if media_lst is not None:
        for m in media_lst:
            db_insert(add_media(tweet_id,m))

def insert_result(id,analysis_data):
    aid = db_insert("SELECT * FROM ANALYSIS WHERE tweet_id like '"+str(id)+"' ORDER BY analysis_date DESC").fetchall()[0][0]
    db_insert(add_result(aid,'spacy',analysis_data['spacy']))
    db_insert(add_result(aid,'monkeylearns',analysis_data['monkey']))
    db_insert(add_result(aid,'azure_computer_vision',analysis_data['azure']))
    db_insert(add_result(aid,'places365',analysis_data['places365']))
    db_insert(add_result(aid,'pil',analysis_data['pil']))


def singlemine(id):
    try:
        #Insert tweet into the database
        insert_tweet(id)
        #Analyze data
        analysis = analyze(id)
        #Insert Keywords
        keywords=[]
        keywords.append(analysis['monkey']['topic'])
        for k in analysis['spacy']['keywords']:
            keywords.append(k)
        insert_keywords(keywords)
        for k in keywords:
            key = keyword_id(k)
            insert_related(id,key)
        insert_media(id,get_media(id))
        insert_analysis(id)
        insert_result(id,analysis)
    except:
        return


def mine_topics(tlist,num,continuous=False):
    if continuous == False:
        tweets = []
        for t in tlist:
            status = search_single_topic(t,num)
            for s in status:
                tweets.append(s[0])
        for t in tweets:
            singlemine(t)
    else:
        while True:
            tweets = []
            for t in tlist:
                status = search_single_topic(t,num)
                for s in status:
                    tweets.append(s[0])
            for t in tweets:
                singlemine(t)
    
def mine_tweets(tlist):
    for t in tlist:
        singlemine(t)
    return


handler = TwitterClient()

#test tweet:
#singlemine(1275150247782543360)
mine_topics(['COVID19','Trump','Racism','Politics','Economy'],100,continuous=True)
