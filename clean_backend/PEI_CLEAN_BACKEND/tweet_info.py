from twitter_handler import *
from monkey import *
import json

handler = TwitterClient()

data = {
    'topic': 'COVID19',
    'average_feeling': 'Neutral',
    'negative':'0.34',
    'positive': '0.22',
    'neutral': '0.44',
    'average_likes': '35',
    'average_retweets' : '20',
    'average_cooments': '29',
    'media_embeded': '0.269',
    'profanity': '0.624',
    'keywords': ['India','Health','SARS','Ebola', 'Italy','USA','Russia','Modi Government','piss','facemask','doubt','CNN','fakenews'],
    }

f=open('ESTA_MERDA_JA_E_DIFERENTE_V2_XPTO_TOP_KEK.json','w')
json.dump(data,f)
