#import pymssql
from procedures import *
import pyodbc
from conf import DB_ADDRESS
from conf import DB_PORT
from conf import USER
from conf import PWD
from conf import OK_C
from conf import NOT_OK_C
from conf import END_CODE_C
from collections import Counter
import json
#print(pyodbc.drivers())
#con = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};' 'DATABASE=PROTECTME;' 'SERVER=127.0.0.1,1433;' 'Trusted_Connection=no;' 'UID=test;' 'PWD=test')
#conn= pymssql.connect("127.0.0.1","test","test","PROTECTME")
def get_tweet_dict(ttid,tid,likes,comments,rt):
    tweet={
        'id': str(ttid),
        'tid':str(tid),
        'likes': str(likes),
        'comments':str(comments),
        'rt':str(rt),
        'rm':'0',
    }
    return tweet

def get_media_dict(typ,url):
    media={
        'type': typ,
        'url': url
    }
    return media

def get_media_data_dict(framework,related,data):
    media_data={
        'framework':framework,
        'related':related,
        'data': data
    }
    return media_data

def db_insert(query):
    global cursor
    return cursor.execute(query)   

def cursor_feedback():
    global cursor
    return cursor.description

def cursor_commit():
    global cursor
    cursor.commit()

def cursor_fetch():
    global cursor
    cursor.fetchone()

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};' 'DATABASE=PROTECTME;' 'SERVER=127.0.0.1,1433;' 'Trusted_Connection=no;' 'UID=SA;' 'PWD=')
conn.autocommit = True
cursor = conn.cursor()


#if __name__ == '__main__':
    #t = db_insert("SELECT * FROM TWEETS LEFT JOIN RELATED ON (RELATED.tweet_id like TWEETS.id) left join TOPICS ON (RELATED.topic_id like TOPICS.id) left join ANALYSIS ON (ANALYSIS.tweet_id like TWEETS.id) left join RESULT ON (RESULT.analysis_id like ANALYSIS.id);")
    #for l in t:
    #    print(l)
    #res = db_insert("SELECT * FROM RESULT").fetchall()
    #ok_count = 0
    #not_ok_count = 0
    #for r in res:
    #    j = r[-1]
    #    out = json.loads(j)
    #    if type(out) == type([]):
    #        if type(out[0]) == type({}):
    #            if 'Result' in out[0].keys():
    #                print(NOT_OK_C + "NO MEDIA" + END_CODE_C)
    #                not_ok_count = not_ok_count + 1
    #            else:
    #                print(OK_C + "HAS MEDIA" + END_CODE_C)
    #                ok_count = ok_count + 1
    #        else:
    #            print(out[0])
    #            print(type(out[0]))
    #    else:
    #        print(OK_C + "OK ANALYSIS" + END_CODE_C)
    #        ok_count = ok_count + 1
    #print(NOT_OK_C + str(not_ok_count)+END_CODE_C)
    #print(OK_C + str(ok_count)+END_CODE_C)
    #print(db_insert("SELECT * FROM TOPICS WHERE keyword like 'butffucked'").fetchone())
    #print(db_insert("SELECT  * FROM ANALYSIS").fetchall())
    #print(db_insert("SELECT * FROM RESULT").fetchall())

def database_stats():
    print(str(db_insert("SELECT COUNT(id) as NUM FROM TWEETS").fetchone()[0]) + " TWEETS")
    print(str(db_insert("SELECT COUNT(analysis_id) as NUM FROM RESULT").fetchone()[0]) + " ANALYSIS")
    print(str(db_insert("SELECT COUNT(id) as NUM FROM TOPICS").fetchone()[0]) + " TOPICS")

def topic_stat(topic):
    print("STATS FOR TOPIC: " + str(topic))
    tid = db_insert("SELECT * FROM TOPICS WHERE keyword like '"+str(topic)+"'").fetchone()[0]
    lst = db_insert("SELECT * FROM RELATED WHERE topic_id =" + str(tid)).fetchall()
    print(str(len(lst)) + " TWEETS")
    print("MOST RELEVANT KEYWORDS (WORD  -->  COUNT)\n ")
    for k in most_important_keywords(tid):
        print(str(k[0]) + "  -->  " + str(k[1]))
    print("\nOVERALL FEELING\n")
    fel = overall_feeling(tid)
    if fel == [0,0,0]:
        fel = None
    if fel is not None:
        tot = fel[0] + fel[1] + fel[2]
        print('\n FROM '+str(tot)+' TWEETS:\n\n '+str(fel[2])+' WERE POSITIVE\n '+str(fel[0])+' WERE NEGATIVE\n'+str(fel[1])+' WERE NEUTRAL')
    else:
        print(NOT_OK_C + "DATA IS NOT AVAILIABLE" + END_CODE_C)


def most_important_keywords(topic_id):
    lst = db_insert('SELECT * FROM RELATED WHERE topic_id='+str(topic_id)).fetchall()
    counter = Counter()
    for l in lst:
        for ln in db_insert("SELECT * FROM RELATED WHERE tweet_id like '"+str(l[0])+"'").fetchall():
            counter[ln[1]] += 1
    words = []
    common = counter.most_common(10)
    for c in common:
        words.append((db_insert("SELECT * FROM TOPICS where id="+str(c[0])).fetchone()[1],c[1]))
    return words

def overall_feeling(topic_id):
    counter = [0,0,0]
    tweets = db_insert("SELECT * FROM RELATED WHERE topic_id=" + str(topic_id)).fetchall()
    for t in tweets:
        an = db_insert("SELECT * FROM ANALYSIS WHERE tweet_id like'"+str(t[0])+"'").fetchall()
        for a in an:
            tmp = db_insert("SELECT * FROM RESULT WHERE analysis_id=" + str(a[0])).fetchone()
            if tmp is not None:
                if tmp[1] == 'monkeylearns':
                    data = json.loads(tmp[2])
                    if data['feeling'] == 'Negative':
                        counter[0] += 1
                    elif data['feeling'] == 'Neutral':
                        counter[1] += 1
                    else:
                        counter[2] += 1
            else:
                return
        return counter

def related_media(topic_id):
    counter = 0
    tweets = db_insert("SELECT * FROM RELATED WHERE topic_id=" + str(topic_id)).fetchall()
    for t in tweets:
        an = db_insert("SELECT * FROM ANALYSIS WHERE tweet_id like'"+str(t[0])+"'").fetchall()
        for a in an:
            tmp = db_insert("SELECT * FROM RESULT WHERE analysis_id=" + str(a[0])).fetchone()
            if tmp is not None:
                if tmp[1] == 'spacy':
                    data = json.loads(tmp[2])
                    if data['media_related'] == []:
                        counter = counter + 1
        return counter

#topic_stat('world')
#related_media('covid19') 
