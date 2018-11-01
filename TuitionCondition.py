import re
from textblob import TextBlob
import random


research = TextBlob("The the the cause you you you and and and we we we")

seperate = research.words
#turns the arguement into list by seperating each word

research.word_counts
#count how many times the word is repeated in the phrase
print research.word_counts
