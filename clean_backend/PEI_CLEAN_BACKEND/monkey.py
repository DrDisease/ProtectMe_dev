from monkeylearn import MonkeyLearn
from conf import MONKEY_KEY
from json_templates import monkey_template

ml = MonkeyLearn(MONKEY_KEY)


def get_feel(txt):
    global ml
    response = ml.classifiers.classify(
            model_id='cl_Jx8qzYJh', data=[txt]
        )
    return response.body[0]['classifications'][0]['tag_name']

def get_profanity(txt):
    global ml
    response = ml.classifiers.classify(
        model_id='cl_KFXhoTdt', data=[txt]
        )
    return response.body[0]['classifications'][0]['tag_name']

def get_topic(txt):
    global ml
    response = ml.classifiers.classify(
        model_id='cl_WDyr2Q4F', data=[txt]
        )
    return response.body[0]['classifications'][0]['tag_name']


def get_language(txt):
    global ml
    response = ml.classifiers.classify(
        model_id='cl_Vay9jh28', data=[txt]
        )
    return response.body[0]['classifications'][0]['tag_name']

def check_english(txt):
    lang = get_language([txt])[0]['classifications'][0]['tag_name']
    if lang == 'English-en':
        return True
    return False

if __name__ == "__main__":
    strng = "If it was rigged in 2016 against Trump, and will be rigged in 2020 against Trump, why did he do nothing during the intervening time to fight election interference?"
    #t = get_topic(strng)
    #f = get_feel(strng)
    #p = get_profanity(strng)
    #print(monkey_template(t,f,p))
    print("Text: " + strng)
    print("Topic: " + get_topic(strng))
    print("Feeling: " + get_feel(strng))
    print("Profanity: " + get_profanity(strng))
