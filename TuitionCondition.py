import re
from textblob import TextBlob
import random


research = TextBlob("The the the cause you you you and and and we we we")

research.tags

seperate = research.words
#turns the arguement into list by seperating each word

def popularNouns(sequence):
    nouns = ()
    for elements in sequence:
        int(nouns.word.counts([nouns for x in sequence if nouns > 3]))
    return nouns

popularNouns("The The The The The buy buy")
