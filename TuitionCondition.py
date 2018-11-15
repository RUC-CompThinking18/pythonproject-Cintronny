import re
from textblob import TextBlob
import random
from textblob.taggers import NLTKTagger
nltk_tagger = NLTKTagger()

research = TextBlob("The the the cause you you you and and and we we we college run throw pay pay pay school money income aide", pos_tagger=nltk_tagger)
research.pos_tags
nouns = []
verbs = []
for tag in research.pos_tags:
    if tag[1] == "NN":
        nouns.apend(tag)
