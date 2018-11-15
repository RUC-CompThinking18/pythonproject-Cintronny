import re
from textblob import TextBlob
import random


research = TextBlob("The the the cause you you you and and and we we we college run throw pay pay pay school money income aide")

research.tags

#tag each word with the type of word it is(noun, verb, etc.)
nouns = []
verbs = []
#create empty list for tagged words to be sent
for tag in research:
    if tag[0] == NN:
        nouns.push
    elif tag[0] == VB:
        verbs.push
    print (nouns, verbs)
