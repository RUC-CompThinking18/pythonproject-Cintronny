# -*- coding: utf-8 -*-
import re
import random
import time


#The goal of this project is to
#Due to incredible lack of ability to solve my issues with understanding textblob I decided to remove that portion of my code all together.
#As an adjustment I decided to take the top 30 tweets on that had the word "tuition" in it on twitter and input them into a word cloud application to find repeated words.
#I then scanned through the list of words that were repeated 3 or more times and piled them into a seperate list that I scanned to seperate the verbs, nouns, and adjectives.

nouns = ("tuition", "students", "college", "fees", "university", "semester", "school", "books", "class")
verbs = ("pay", "will", "make", "fighting", "helps", "can", "access", "attending", "gonna", "learn")
adj = ("free", "many", "new")

#The next few variables  are created to search through the lists above so that a random word will be chosen to develop the random generated sentance.
num = random.randrange(0,8)
num_two = random.randrange(0,8)
vernum = random.randrange(0,9)
adnum = random.randrange(0,2)
adnum_two = random.randrange(0,2)
#the randrange function allows the code to select a random word from each list.
first_half = (adj[adnum] + ' ' + nouns[num] + ' ' + verbs[vernum])
second_half = (adj[adnum_two] + ' ' + nouns[num_two])

def create_tweet():
    print(first_half + ' ' + second_half)

def countdown():
    s=0
    while s<=15:
        time.sleep(1)
        s+=1
        if s==15:
            create_tweet()
            s=0
