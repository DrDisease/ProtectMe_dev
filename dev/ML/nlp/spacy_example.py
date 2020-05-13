import spacy
from spacy import displacy
from collections import counter
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


# Returns a given text element's keywords
# Still needs some adjustments and might be
# deprecated as soon as the 
# main pipeline is implemented
def get_keywords(nlp, text):
    res = []
    tag = []
    processed = nlp(text.lower())
    for token in processed:
        if token.tag_ in tag:
            res.append(token.text)
        print(token)
    return res


# The core of this script.
# Verifies if there is some sort of similarity between
# Two different text elements


# -----------------Testing ------------------------
#
# Starting the NLP and loading a piece of sample text to it
nlp = spacy.load("en_core_web_sm")
vectors = spacy.load("en_vectors_web_lg")
txt = 'Top of the 8 pm hour starts with ' + \
        'President Donald Trump congratulating ' + \
        'Dana White for putting on this event and ' + \
        'urging other sports league to return, as well.'
processed = nlp(txt)
print(join_proper_names(processed))
displacy.serve(processed, style="dep")
sents = list(processed.sents)
for s in sents:
    processed = nlp(str(s))
    print(str(s))
    sentence = ''
    for token in processed:
        if dep_check(token.dep_):
            sentence = sentence + token.text + " "
            print(green + str(token.tag_) + endc)
            print(spacy.explain(token.tag_))
            print(str(token.text) + " " + str(token.dep_))
    print(sentence)
    print(lemmas(processed))
