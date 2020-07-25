#from miner import *
from db_connect import *
from conf import OK_C
from conf import NOT_OK_C
from conf import END_CODE_C
from twitter_handler import *
from clean import *
from place import *
from metadata import *
from spacy_example import *
from monkey import *
from procedures import *
import os
import tweepy

def debug_results():
    res = db_insert("SELECT * FROM RESULT").fetchall()
    ok_count = 0
    not_ok_count = 0
    for r in res:
        j = r[-1]
        out = json.loads(j)
        if type(out) == type([]):
            if type(out[0]) == type({}):
                if 'Result' in out[0].keys():
                    print(NOT_OK_C + "NO MEDIA" + END_CODE_C)
                    not_ok_count = not_ok_count + 1
                else:
                    print(OK_C + "HAS MEDIA" + END_CODE_C)
                    ok_count = ok_count + 1
            else:
                print(out[0])
                print(type(out[0]))
        else:
            print(OK_C + "OK ANALYSIS" + END_CODE_C)
            ok_count = ok_count + 1

    print(NOT_OK_C + str(not_ok_count)+END_CODE_C)
    print(OK_C + str(ok_count)+END_CODE_C)


def comp_tweet_anal():
    tweets = db_insert("SELECT * FROM TWEETS").fetchall()
    results = db_insert("SELECT * FROM RESULT").fetchall()
    anal = db_insert("SELECT * FROM ANALYSIS").fetchall()
    print("Number of tweets: " + str(len(tweets)))
    print("Number of Results: " + str(len(results)))
    print("Number of analysis made: " + str(len(anal)))


def get_media_debug(id):
    status = handler.get_tweet_from_id(id)
    print("TWEET ID: " + str(status.id))
    if 'media'in status.entities.keys():
        print(OK_C + "TWEET HAS MEDIA" + END_CODE_C)
        for m in status.extended_entities['media']:
            t = m['type']
            if t == "photo":
                print(OK_C+"type: "+str(m['type']) +" || url: "+str(m['media_url']) + END_CODE_C)
            else:
                print(NOT_OK_C+"type: "+str(m['type']) +" || url: "+str(m['media_url']) + END_CODE_C)
    pass

def get_media_analysis_debug(url):
    
    print('\n\n  ANALYZING IMAGE \n')
    print('\n ----- AZURE COMPUTER VISION ----\n')
    
    
    print('\nDESCRIPTION \n')
    
    desc = get_description(url)
    if desc is not None:
        for d in desc:
            print(d[0] + " with {:.1f}% confidence".format(d[1]*100))
    else:
        print(NOT_OK_C + "NO DESCRIPTION AVAILIABLE" + END_CODE_C)
    

    print('\nFACES\n')
    
    fac = get_faces(url)
    if fac is not None:
        for d in fac:
            print(str(d[0]) + " year old " + str(d[1].name))
            #print(type(d[1]))
    else:
        print(NOT_OK_C + "NO FACES AVAILIABLE" + END_CODE_C)
    
    
    print('\nOBJECTS\n')
    
    ob = get_objects(url)
    if ob is not None:
        for d in ob:
             print(d[0])
    else:
        print(NOT_OK_C + "NO OBJECTS AVAILIABLE" + END_CODE_C)
    
    
    print('\nCATEGORIES\n')
    
    cat = get_categories(url)
    if cat is not None:
        for d in cat:
             print(d[0] + " with {:.1f}% confidence".format(d[1]*100))
    else:
        print(NOT_OK_C + "NO CATEGORIES AVAILIABLE" + END_CODE_C)
    
    
    print('\n ---------- PLACES 365 ----------\n')
    print('Getting image from source')
    os.system('wget -O image.jpg ' + str(url) + ' 2> /dev/null')
    img  = Image.open('image.jpg')
    
    try:
        pl = analyse_img(img)
        for p in pl:
            print(p)
    except:
        print(NOT_OK_C + 'IMAGE ANALYSIS NOT POSSIBLE' + END_CODE_C)
    
    
    print('\n --------- PIL ANALYSIS  --------\n')
    
    
    try:
        meta = extract_metadata(img)
        if meta is None:
            print(NOT_OK_C + "NO METADATA AVAILIABLE" + END_CODE_C)
        else:
            dt = json.loads(pil_template(meta)) 
            if dt['metadata'] == [] :
                print(NOT_OK_C + "NO METADATA AVAILIABLE" + END_CODE_C)
            else:
                print(pil_template(meta))

    except:
        print(NOT_OK_C + 'IMAGE ANALYSIS NOT POSSIBLE' + END_CODE_C)

    os.system('rm image.jpg')

    print('\n\n ---------- END OF ANALYSIS ------------\n\n')
    
    return

def full_analysis_debug(tweet_id):
    
    tweet = handler.get_tweet_from_id(tweet_id)
    
    fav = tweet.favorite_count
    text = tweet.full_text

    urls = []

    print('\n\nTWEET ID: ' + str(tweet_id) + '\n\n TEXT: ' + str(text) \
        + '\n\n FAVORITE COUNT: ' + str(fav))

    print('\n\n ------ TEXT ANALYSIS ----------- \n')
    
    
    print('\n\n ----------- SPACY -------------- \n')
    
    print('Keywords: ' + str(get_hotwords(text)))
    print('Proper Nouns: ' + str(join_proper_names(nlp(text)))) 
    
    try:

        print('\n\n -------MONKEY LEARNS ----------- \n')

        print('Topic: ' + str(get_topic(text)))
        print('Feeling: ' + str(get_feel(text)))
        print('Profanity: ' + str(get_profanity(text)))
    
    except:

        print(NOT_OK_C + 'MONKEY LEARNS REQUESTS THROTLED' + END_CODE_C)

    print('\n\n ----- END OF TEXT ANALYSIS ---------\n')

    urls = []

    if 'media' in tweet.entities.keys():
        print(OK_C + 'TWEET CONTAINS ADITIONAL MEDIA' + END_CODE_C)
        media_list = tweet.extended_entities['media']
        for m in media_list:
            if m['type'] == 'photo':
                print(OK_C + 'type: ' + str(m['type']) + ' || url: ' + m['media_url'] + END_CODE_C)
                urls.append(m['media_url'])
            else:
                print(NOT_OK_C + 'type: ' + str(m['type']) + ' || url: ' + m['media_url'] + END_CODE_C)


    if urls != []:
        for url in urls:

            print('\n\n  ANALYSING IMAGE \n')
            
            print('\n IMAGE URL: ' + url + '\n')

            print('\n ----- AZURE COMPUTER VISION ----\n')
            
            
            print('\nDESCRIPTION \n')
            
            desc = get_description(url)
            if desc is not None:
                for d in desc:
                    print(d[0] + " with {:.1f}% confidence".format(d[1]*100))
            else:
                print(NOT_OK_C + "NO DESCRIPTION AVAILIABLE" + END_CODE_C)
            

            print('\nFACES\n')
            
            fac = get_faces(url)
            if fac is not None:
                for d in fac:
                    print(str(d[0]) + " year old " + str(d[1].name))
            else:
                print(NOT_OK_C + "NO FACES AVAILIABLE" + END_CODE_C)
            
            
            print('\nOBJECTS\n')
            
            ob = get_objects(url)
            if ob is not None:
                for d in ob:
                    print(d[0])
            else:
                print(NOT_OK_C + "NO OBJECTS AVAILIABLE" + END_CODE_C)
            
            
            print('\nCATEGORIES\n')
            
            cat = get_categories(url)
            if cat is not None:
                for d in cat:
                    print(d[0] + " with {:.1f}% confidence".format(d[1]*100))
            else:
                print(NOT_OK_C + "NO CATEGORIES AVAILIABLE" + END_CODE_C)
            
            
            print('\n ---------- PLACES 365 ----------\n')
            print('Getting image from source')
            os.system('wget -O image.jpg ' + str(url) + ' 2> /dev/null')
            img  = Image.open('image.jpg')
            
            try:
                pl = analyse_img(img)
                for p in pl:
                    print(p)
            except:
                print(NOT_OK_C + 'IMAGE ANALYSIS NOT POSSIBLE' + END_CODE_C)
            
            
            print('\n --------- PIL ANALYSIS  --------\n')
            
            
            try:
                meta = extract_metadata(img)
                if meta is None:
                    print(NOT_OK_C + "NO METADATA AVAILIABLE" + END_CODE_C)
                else:
                    dt = json.loads(pil_template(meta)) 
                    if dt['metadata'] == [] :
                        print(NOT_OK_C + "NO METADATA AVAILIABLE" + END_CODE_C)
                    else:
                        print(pil_template(meta))

            except:
                print(NOT_OK_C + 'IMAGE ANALYSIS NOT POSSIBLE' + END_CODE_C)

            os.system('rm image.jpg')

            #TODO: Implement this part and add MonkeyLearns Pipeline
            print('\n -------- SPACY ANALYSIS --------\n')
            if desc is not None:
                for d in desc:
                    ev = similarity(d[0],text)
                    if evaluate_weight(ev):
                        print(OK_C + 'Image is correlated to text with {:.2f}% confidence'.format(ev) + END_CODE_C)
                    else:
                        print(NOT_OK_C + 'Image is not correlated to text' + END_CODE_C)

            print('\n\n ---------- END OF ANALYSIS ------------\n\n')
            
            pass


def singlemine_debug(tweet_id):
    

    try:
        tweet = handler.get_tweet_from_id(tweet_id)
    except:
        print(NOT_OK_C + "TWEET NO ACCESSIBLE" + END_CODE_C)
        return
    fav = tweet.favorite_count
    text = tweet.full_text


    #db_insert("INSERT INTO TWEETS VALUES('"+str(tweet_id)+"',0,'"+str(fav)+"',0,0,0)")

    #db_insert("INSERT INTO ANALYSIS(tweet_id) VALUES('"+str(tweet_id)+"')")

    urls = []

    print('\n\nTWEET ID: ' + str(tweet_id) + '\n\n TEXT: ' + str(text) \
        + '\n\n FAVORITE COUNT: ' + str(fav))

    print('\n\n ------ TEXT ANALYSIS ----------- \n')
    
    
    print('\n\n ----------- SPACY -------------- \n')
    
    hword = get_hotwords(text)


    try:
	    for h in hword:
	        aid = db_insert("SELECT * FROM TOPICS WHERE keyword like '"+str(h)+"'") .fetchone()
	        if aid is None:
	            db_insert("INSERT INTO TOPICS(keyword) VALUES('"+str(h)+"')")
	            aid = db_insert("SELECT * FROM TOPICS WHERE keyword like '"+str(h)+"'").fetchone()[0]
	        else:
	            aid=aid[0]
	        #print("INSERT INTO RELATED VALUES('"+str(tweet_id)+"',"+str(aid)+");")
	        db_insert("INSERT INTO RELATED VALUES('"+str(tweet_id)+"',"+str(aid)+");")
    except:
    	print("ERROR CRASH")
    print('Keywords: ' + str(hword))
    print('Proper Nouns: ' + str(join_proper_names(nlp(text)))) 
    
    spacy={
        'keywords' : hword,
        #'proper_nouns: ': join_proper_names(nlp(text)),
        'media_related': []
        }

    monkey = None

    try:
        print('\n\n -------MONKEY LEARNS ----------- \n')
        topic = get_topic(text)
        feeling = get_feel(text)
        profanity = get_profanity(text)

        print('Topic: ' + str(topic))
        print('Feeling: ' + str(feeling))
        print('Profanity: ' + str(profanity))

        monkey = {
            'profanity': profanity,
            'topic': topic,
            'feeling': feeling
        }
    except:
        print(NOT_OK_C + 'MONKEY LEARNS REQUESTS THROTLED' + END_CODE_C)
        monkey = None

    print('\n\n ----- END OF TEXT ANALYSIS ---------\n')

    urls = []

    pil = {
        'result' : [],
        'metadata' : []
        }
    places = {  'result' : [],
                'tags' : []
            }
    azure = {
        'description': [],
        'faces': [],
        'objects': [],
        'categories': []
    }

    if 'media' in tweet.entities.keys():
        print(OK_C + 'TWEET CONTAINS ADITIONAL MEDIA' + END_CODE_C)
        media_list = tweet.extended_entities['media']
        for m in media_list:
            db_insert("INSERT INTO MEDIA(tweet_id,media_type,media_url) VALUES('" +\
            str(tweet_id)+"','"+str(m['type'])+"','"+str(m['media_url'])+"')")
            if m['type'] == 'photo':
                print(OK_C + 'type: ' + str(m['type']) + ' || url: ' + m['media_url'] + END_CODE_C)
                urls.append(m['media_url'])
            else:
                print(NOT_OK_C + 'type: ' + str(m['type']) + ' || url: ' + m['media_url'] + END_CODE_C)


    if urls != []:
        for url in urls:

            print('\n\n  ANALYSING IMAGE \n')
            
            print('\n IMAGE URL: ' + url + '\n')

            print('\n ----- AZURE COMPUTER VISION ----\n')
            
            
            print('\nDESCRIPTION \n')
            
            desc = get_description(url)
            if desc is not None:
                azure['description'].append(desc)
                for d in desc:
                    print(d[0] + " with {:.1f}% confidence".format(d[1]*100))
            else:
                print(NOT_OK_C + "NO DESCRIPTION AVAILIABLE" + END_CODE_C)
            

            print('\nFACES\n')
            
            fac = get_faces(url)
            if fac is not None:
                azure['faces'].append(fac)
                for d in fac:
                    print(str(d[0]) + " year old " + str(d[1].name))
            else:
                print(NOT_OK_C + "NO FACES AVAILIABLE" + END_CODE_C)
            
            
            print('\nOBJECTS\n')
            
            ob = get_objects(url)
            if ob is not None:
                azure['objects'].append(ob)
                for d in ob:
                    print(d[0])
            else:
                print(NOT_OK_C + "NO OBJECTS AVAILIABLE" + END_CODE_C)
            
            
            print('\nCATEGORIES\n')
            
            cat = get_categories(url)
            if cat is not None:
                azure['categories'].append(cat)
                for d in cat:
                    print(d[0] + " with {:.1f}% confidence".format(d[1]*100))
            else:
                print(NOT_OK_C + "NO CATEGORIES AVAILIABLE" + END_CODE_C)
            


            
            print('\n ---------- PLACES 365 ----------\n')
            print('Getting image from source')
            os.system('wget -O image.jpg ' + str(url) + ' 2> /dev/null')
            img  = Image.open('image.jpg')
            
            try:
                pl = analyse_img(img)
                for p in pl:
                    print(p)
                places['result'].append('OK')
                places['tags'].append(pl)
            except:
                print(NOT_OK_C + 'IMAGE ANALYSIS NOT POSSIBLE' + END_CODE_C)
                places['result'].append('ERROR')

            print('\n --------- PIL ANALYSIS  --------\n')
            

            try:
                meta = extract_metadata(img)
                if meta is None:
                    print(NOT_OK_C + "NO METADATA AVAILIABLE" + END_CODE_C)
                    pil['result'].append('ERROR')
                else:
                    dt = json.loads(pil_template(meta)) 
                    if dt['metadata'] == [] :
                        print(NOT_OK_C + "NO METADATA AVAILIABLE" + END_CODE_C)
                        pil['result'].append('ERROR')
                    else:
                        print(pil_template(meta))
                        pil['result'].append('OK')
                        pil['metadata'].append(pil_template(meta))

            except:
                print(NOT_OK_C + 'IMAGE ANALYSIS NOT POSSIBLE' + END_CODE_C)
                pil['result'].append('ERROR')
            os.system('rm image.jpg')

            
            
            print('\n -------- SPACY ANALYSIS --------\n')
            
            if desc is not None:
                for d in desc:
                    ev = similarity(d[0],text)
                    if evaluate_weight(ev):
                        print(OK_C + 'Image is correlated to text with {:.2f}% confidence'.format(ev) + END_CODE_C)
                        spacy['media_related'].append(True)
                    else:
                        print(NOT_OK_C + 'Image is not correlated to text' + END_CODE_C)
                        spacy['media_related'].append(False)
            
            
            
            
            print('\n\n ---------- END OF ANALYSIS ------------\n\n')
        else:
            pil= None
            places = None
            azure = None


    data = None

    aid = db_insert("SELECT * FROM ANALYSIS WHERE tweet_id like '"+str(tweet_id)+"' ORDER BY analysis_date DESC").fetchone()[0]


    if azure is None and monkey is None:
        #spacy = json.dumps(spacy)
        db_insert(add_result(aid,'spacy',spacy))
    elif monkey is not None and azure is not None:
        #spacy = json.dumps(spacy)
        #azure = json.dumps(azure)
        #monkey = json.dumps(monkey)
        #pil = json.dumps(pil)
        #places = json.dumps(places)
        db_insert(add_result(aid,'spacy',spacy))
        db_insert(add_result(aid,'azure',azure))
        db_insert(add_result(aid,'monkey',monkey))
        db_insert(add_result(aid,'pil',pil))
        db_insert(add_result(aid,'places365',places))
    elif azure is None:
        #spacy = json.dumps(spacy)
        #monkey = json.dumps(monkey)
        db_insert(add_result(aid,'spacy',spacy))
        db_insert(add_result(aid,'monkey',monkey))
    else:
        db_insert(add_result(aid,'spacy',spacy))
        db_insert(add_result(aid,'azure',azure))
        db_insert(add_result(aid,'pil',pil))
        db_insert(add_result(aid,'places365',places))





def analyze_media_debug(id):
    media = []
    status = handler.get_tweet_from_id(id)
    if 'media' in status.entities.keys():
        for m in status.extended_entities['media']:
            media.append((m['type'],m['media_url']))
    if media == []:
        print('STATUS ID: ' + str(id) + '\n' + NOT_OK_C + 'STATUS HAS NO MEDIA CONTENT' + END_CODE_C)
    else:
        print('STATUS ID: ' + str(id))
        for m in media:
            if m[0] == 'photo':
                print(OK_C + 'type: photo || url: ' + str(m[1]) + END_CODE_C)
                get_media_analysis_debug(m[1])
            else:
                print(NOT_OK_C + 'type: ' + str(m[0]) + ' || url:' + str(m[2]) + END_CODE_C)



def  debug_search_single_topic(topic,num):
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
            data.append(tweet.id)
    return data

def debug_search_topics(topics, num,cont=True):
    for t in topics:
        print(OK_C + "MINING: "+str(t)+ END_CODE_C)
        tl = debug_search_single_topic(t,num)
        for tweet in tl:
            singlemine_debug(tweet)
    while cont:
        for t in topics:
            print(OK_C + "MINING: "+str(t)+ END_CODE_C)
            tl = debug_search_single_topic(t,num)
            for tweet in tl:
                singlemine_debug(tweet)



handler = TwitterClient()
if __name__ == '__main__':

    debug_results()
    #comp_tweet_anal()

    ##Beginning Debug Routine
    

    #List of tweets used for debug purposes
    #lst = [
    #    1282012039825764352,
    #    1282096802188189706,
    #    1282107114605940736,
    #    1282129114766258176,
    #    1282061256078159872,
    #    1281998991316713478
    #]
    #singlemine_debug(lst[0])
    #returns amount of favorites tweet has received
    #print(handler.get_tweet_from_id(lst[0]).favorite_count)
    #for l in lst:
        #tweet = handler.get_tweet_from_id(l)
        #print(tweet.favorite_count)
        #print(tweet.full_text)
        #print(tweet.id)
        #print('\n\n')
        #get_media_debug(l)
        #analyze_media_debug(l)
    #full_analysis_debug(lst[1])    
    #insertions debug
    #debug_search_topics(['covid19','trump', 'cybersecurity', 'Brexit', 'Racism', 'Protests', 'Immigration', 'EU'],100,cont=True)
singlemine_debug(1283027127118553088)
singlemine_debug(1282771446335406080)
singlemine_debug(1282891059056578560)
singlemine_debug(1283016884582064130)
