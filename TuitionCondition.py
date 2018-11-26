# -*- coding: utf-8 -*-
import re
import random
import time


#The goal of this project is to
#Due to incredible lack of ability to solve my issues with understanding textblob I decided to remove that portion of my code all together.
#As an adjustment I decided to take the top 30 tweets on that had the word "tuition" in it on twitter and input them into a word cloud application to find repeated words.
#I then scanned through the list of words that were repeated 3 or more times and piled them into a seperate list that I scanned to seperate the verbs, nouns, and adjectives.

nouns = ("tuition", "students", "college", "fees", "university", "semesters", "school", "books", "class", "loans", "dorm", "job", "")
verbs = ("paying", "willing", "makes", "fighting", "helps", "can", "accesses", "attending", "gonna", "learning", "withdrawing", "failing", "get", "go",)
adj = ("free", "many", "new", "expensive", "affordable", "rich", "poor", "stupid", "smarter", "tired")

#The next few variables  are created to search through the lists above so that a random word will be chosen to develop the random generated sentance.

def create_quote():
    num = random.choice(nouns)
    num_two = random.choice(nouns)
    vernum = random.choice(verbs)
    adnum = random.choice(adj)
    adnum_two = random.choice(adj)
    #the randrange function allows the code to select a random word from each list.
    first_half = (adnum + ' ' + num + ' ' + vernum)
    second_half = (adnum_two + ' ' + num_two)
    print('"' + first_half + ' ' + second_half + '"')
#I want this function to run every 15 seconds

quote = "Here is a quote from an incredibly stressed college student struggling with paying tuition:"

while True:
    print quote
    create_quote()
    time.sleep(15)
