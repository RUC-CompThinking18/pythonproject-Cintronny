import re
import random
#due to incredible lack of ability to solve my issues with understanding textblob I decided to remove that portion of my code all together.
#As an adjustment I decided to take all of the tweets that I farmed on twitter and input them into a word cloud application to find repeated words.
#I then scanned through the list of words that were repeated 3 or more times and piled them into a seperate list that I scanned to seperate the verbs, nouns, and adjectives.

nouns = ("tuition", "students", "college", "fees", "university", "semester", "school", "books", "class")
verbs = ("pay", "will", "make", "fighting", "helps", "can", "access", "attending", "don't", "gonna", "learn")
adj = ("free", "many", "new")

num = random.randrange(0,9)
vernum = random.randrange(0,11)
adnum = random.randrange(0,3)

first_half = (adj[adnum] + ' ' + nouns[num] + ' ' + verbs[vernum])
second_half = (adj[adnum] + ' ' + nouns[num])
print first_half + ' ' + second_half
