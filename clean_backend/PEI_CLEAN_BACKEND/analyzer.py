from clean import * # Azure Computer Vision Module
#from keywords import * # Additional Keyword extraction using textRank algorithm
from metadata import * # PIL metadata extraction
from monkey import * # MonkeyLearns pretrained models
from place import * # Places 365 pretrained model for location recognition
from spacy_example import * # Spacy Module
from twitter_handler import * # Tweepy Twitter Mining Module

#Analyze takes as arg a Status element
def analyze(tweet_id):
    handler = TwitterClient()
    tweet_status = handler.get_tweet_from_id(tweet_id)
    text = tweet_status.full_text
    tweet_media = get_media(tweet_status.id) 
 
    # Azure Analysis
    azure = []
    print(tweet_media)
    for media in tweet_media:
        results = {
            'categories': get_categories(media),
            'description': get_description(media),
            'faces': get_faces(media),
            'objects': get_objects(media)
        }
        print(results)
        azure.append(results)
    
    
    # Places 365 and PIL
    pil = []
    places = []
    for media in tweet_media:
        image = get_image(media)
        tmp_pil = extract_metadata(image)
        tmp_places = analyse_img(image)
        pil.append(tmp_pil)
        places.append(tmp_places)
        delete_img()
    
    # Monkey Learns
    monkey = {
        'profanity' : get_profanity(text),
        'topic' : get_topic(text),
        'feeling' : get_feel(text),
    }
    
    # Spacy
    mx = 0
    for a in azure:
        if a['description'] is not None:
            if a['description'] != []:
                for s in a['description']:
                    #Azure APIs' output is trash, so... some jank is needed
                    tmp_mx = similarity(text,s[0])
                    if tmp_mx > mx:
                        mx = tmp_mx
    related = evaluate_weight(mx)
    spacy={
        'keywords' : get_hotwords(text),
        'media_related': related
    }

    data = {
        'azure':azure,
        'spacy':spacy,
        'monkey':monkey,
        'pil':pil,
        'places365':places
    }


    return data


def get_image(url):
        name = 'image.jpg'
        os.system('wget -O image.jpg ' + 'url')
        try:
            img = Image.open(name)
            return img
        except:
            return None

def delete_img():
    os.system('rm image.jpg')

def get_media(id):
    handler = TwitterClient()
    tweet = handler.get_tweet_from_id(id)
    m = tweet.entities['media']
    media = []
    for p in m:
        media.append(p['media_url'])
    return media