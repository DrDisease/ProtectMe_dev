import json


def azure_template(cat,desc,faces,objects):
    data = {
        'categories': cat,
        'desc': desc,
        'faces': faces,
        'objects': objects 
    }
    r = json.dumps(data)
    return r


def monkey_template(t,f,p):
    data = {
        'feel': p,
        'profanity': f,
        'topics': t
    }
    r = json.dumps(data)
    return r


def places_template(p):
    data={
        'preditctions': p
    }
    r = json.dumps(data)
    return r 


def spacy_template(k,rel=[]):
    data = {
        'keywords': k,
        'related' : rel
    }
    r = json.dumps(data)
    return r

def pil_template(lst):
    data = {
        'metadata': lst
    }
    r = json.dumps(data)
    return r
