import spacy
from collections import Counter
from string import punctuation
import pytextrank


#def get_hotwords(text):
#    result = []
#    pos_tag = ['PROPN', 'ADJ', 'NOUN'] # 1
#    doc = nlp(text.lower()) # 2
#    for token in doc:
#        # 3
#        if(token.text in nlp.Defaults.stop_words or token.text in punctuation):
#            continue
#        # 4
#        if(token.pos_ in pos_tag):
#            result.append(token.lemma_)
                
#    return result # 5

#def trank(text,nlp):
#    doc=nlp(text)
#    r = []
#    for p in doc._.phrases:
        #Checking the rank of the extracted keywords
#        if p.rank > 0.08:
#            r.append(p.chunks)
#    return r