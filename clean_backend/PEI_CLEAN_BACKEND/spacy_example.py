import spacy
from spacy import displacy
from string import punctuation
# Adding color to the terminal in order
# To make debug messages easier to read


red = '\033[91m'
green = '\033[92m'
endc = '\033[0m'


# Checking if the GPU is enabled


gpu = spacy.prefer_gpu()
valid_gpu = red


if gpu:
    valid_gpu = green


print(str(valid_gpu) + "GPU ENABLED: " + str(gpu) + str(endc))


# --------Start of the Script ------------------


# The purpose of this short script is to 
# Generate a context from simple text
# As such, the output must be equal, or very
# similar, so that it makes finding sentences
# in the same context easy to identify


# Checks the Dependencies and removes dependencies
# Irrelevant for context generation
def dep_check(dep):
    irrelevant = ['det', 'prep', 'punct', 'cc', 'advmod']
    if dep in irrelevant:
        return False
    return True


# Accepts a list of processed text from the NLP
# and returns a list with every token lemmatized
def lemmas(tokens):
    lem = []
    for t in tokens:
        lem.append(t.lemma_)
    return lem


# Takes a list of tokens from the NLP
# And parses through it in order to find
# every proper noun and join nouns that belong 
# to the same entity
def join_proper_names(tokens):
    proper_nouns = []
    tmp_str = ""
    for token in tokens:
        if tmp_str == "":
            if token.tag_ == "NNP":
                tmp_str = tmp_str+str(token.text) + " "
        else:
            if token.tag_ != "NNP":
                proper_nouns.append(tmp_str)
                tmp_str = ""
            else:
                tmp_str = tmp_str + str(token.text) + " "
    if tmp_str != "":
        proper_nouns.append(tmp_str)
    return proper_nouns


def get_hotwords(text):
    result = []
    pos_tag = ['PROPN', 'ADJ', 'NOUN'] # 1
    doc = nlp(text.lower()) # 2
    for token in doc:
        # 3
        if(token.text in nlp.Defaults.stop_words or token.text in punctuation):
            continue
        # 4
        if(token.pos_ in pos_tag):
            result.append(token.lemma_)
                
    return list(set(result)) # 5

def similarity(text1,text2):
    # getting a list of keywords
    lst1 = get_hotwords(text1)
    comp1 = "" 
    for w in lst1:
        comp1 = comp1 + w + " "
    lst2 = get_hotwords(text2)
    comp2 = ""
    for w in lst2:
        comp2 = comp2 + w + " "
    # generating token lists
    vec1 = nlp(comp1)
    vec2 = nlp(comp2)
    # temp accumulator
    accum = []
    # iterating over tokens
    for token1 in vec1:
        # max similarity detected for token 1
        sim_chck = 0
        for token2 in vec2:
            sim = token1.similarity(token2)
            if sim > sim_chck:
                sim_chck = sim
        accum.append(sim_chck)
    # weighing values according to a geometric series
    accum.sort(reverse=True)
    weighted = 0
    counter = -1
    for a in accum:
         weighted = weighted + ( a * ( 2 ** ( counter ) ) )
         counter = counter -1
         print(weighted)
    return weighted

def evaluate_weight(weight):
    #compare to weight heuristic
    if weight > 0.42 :
        return True
    else:
        return False

# ----------------- On module init: -----------------

#load nlp core
nlp = spacy.load("en_core_web_sm")
#load word vector lookup table
vectors = spacy.load("en_vectors_web_lg")


# ----------------- Testing ------------------------
#
# Starting the NLP and loading a piece of sample text to it
if __name__ == "__main__":

    txt = 'Top of the 8 pm hour starts with ' + \
            'President Donald Trump congratulating ' + \
            'Dana White for putting on this event and ' + \
            'urging other sports league to return, as well.'
    processed = nlp(txt)
    #prints a list with the joined proper names
    print(join_proper_names(processed))
    #lists the sentences present in the phrase
    sents = list(processed.sents)
    print(similarity(txt,txt))
    print(get_hotwords(txt))