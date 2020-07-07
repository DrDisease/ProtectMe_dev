import json


# tweet structure
# id int
# thread_id int
# likes int
# comments int
# retweets int
# related_media bit


def add_tweet(tweet):
    query="INSERT INTO TWEETS VALUES('"+str(tweet['id']) +"',"+str(tweet['tid'])+ \
        ","+str(tweet['likes'])+","+str(tweet["comments"])+','+str(tweet['rt'])+ \
            ","+str(tweet['rm'])+");"
    return query


#Topics Structure
#id int
#keyword int

def add_topic(keyword):
    query="INSERT INTO TOPICS(keyword) VALUES('"+keyword+"');"
    return query

#Related Structure
#tweet_id int
#topic_id int

def add_related(tweet_id, topic_id):
    query="INSERT INTO RELATED VALUES('"+str(tweet_id)+"',"+str(topic_id)+");"
    return query

#Analysis Structure
#id int
#analysis_date date
#tweet_id int

def add_analysis(tweet_id):
    query=('INSERT INTO ANALYSIS(tweet_id) VALUES('+str(tweet_id)+');')
    return query

#Media Structure
#id int
#tweet id int
#media type str
#media_url str
def add_media(tweet_id,media):
    print(media)
    query=("INSERT INTO MEDIA(tweet_id,media_type,media_url) VALUES('" \
        +str(tweet_id)+"','"+'image'+"','"+media+ "');"
        )
    return query
#Media Analysis
#analysis_id int (different from previous analysis id)
#media _id int
#analysis_date date
#framework str
#media_related bit
#retrieved_data json_str

def add_result(aid,framework,a_data):
    encoded = json.dumps(a_data)
    query = "INSERT INTO RESULT VALUES('"+str(aid)+"','"+framework+"','"+str(encoded)+"')"
    return query