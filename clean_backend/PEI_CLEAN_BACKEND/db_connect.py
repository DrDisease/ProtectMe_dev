#import pymssql
from procedures import *
import pyodbc
from conf import DB_ADDRESS
from conf import DB_PORT
from conf import USER
from conf import PWD
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

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};' 'DATABASE=PROTECTME;' 'SERVER=127.0.0.1,1433;' 'Trusted_Connection=no;' 'UID=test;' 'PWD=test')
conn.autocommit = True
cursor = conn.cursor()