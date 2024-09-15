"""
--------ANALYSIS QUESTIONS-------

* Make a chart to show how many comics were published each month

-------WORDS ANALYSIS-------
* [DONE] How many total strings are there?

* [DONE] How many unique strings are there?

* [DONE] What's the longest string to show up in the totality of comics?

* [DONE] What's the longest real word to show up in the totality of comics?

* How many comics has no stings in them?

* Which comic contains the most strings?



* What's the most common strings? Visualize the x most common words.
  - Why are certain words more common? Exclude them and see your new result.

* What's the average word count? Median?

* Can I plot the word count across time?

* How many words are in all caps? What are they?
    Make sure to include phrases and which comic they are in (as a set).

* Which comic has the most words in all caps?



* How many words begin with the letter (insert letter here)?

-------FIELDS-------
* [DONE] How many comics use the links key?

* Of these links, what are the unique domain names? Plot them

* [DONE] How many comics use the news key?

* Is there a comic number that skips the sequence? (answer: 404)

* What countries have been mentioned in the comic? How many times?

* Same for states/territories/cities.

* Plot these on scattergeo.


"""
from xkcd_catalog_functions import *
import time

# Load our json file which contains all of our comics
filename = 'all_xkcd.json'
with open(filename) as f:
    full_xkcd_repo = json.load(f)

# Verify that the json file is up-to-date. If not, update the file.
is_xkcd_updated(full_xkcd_repo)

# The Data Analysis of our xkcd.json
"""
-----WORDS-----
STEPS:
1. Set a variable equal to the phrase. 
2. Lowercase and split every word when storing it inside the variable.
3. Clean the variable of punctuation marks
4. Append all the words to a single list for later manipulation.
5. Maybe store it in a json so I don't have to keep looping.

This clean list can then be used for further analysis.

Total word count:
1. Get the word count via the len of the list

Count of all words;
1. In our list, count how many times a word shows up in our list and store it in a dictionary.
2. Organize the dictionary by it's values, also make sure to deal with ties.
3. Plot the results as a I see fit.
2. Maybe even write our results to a .json so I don't have to loop it everytime. 

Total unique words:
1. Use len(set(my_list)) to get how many unique words are in the list

Banned word list:
1. Loop a del method to remove banned words or phrases from our list.
  -Keep in mind that since every word has been split, I'd have to grab the og list, ban the phrases (ex. alt title),
  then split the words. Else I'll remove the word title when it might actually have a use case

Longest word:
1. Store the first word in the list.
2. Get the len of each following word in the list via len(my_list[index]). 
3. If the len of the word is greater than my variable, that's my new longest word.
4. Based on the results, make an .isalpha check so that words with numbers aren't part of the equation.
5. Take into account comics that lead to an external site.

Word with the most vowels:
1. Get a word. 
2. Count how many vowels it has. 
3. Store the word and the count as in a dictionary as two different keys
4. Make sure there's an isalpha check.
5. Replace the word if there's a word with more vowels.
6. Variant of this is to count the vowels of every word and then plot the words with the most vowels.
7. Also note what the comic num was? That'd require a new approach with storing my list. 
It'd probably have to be a dictionary that stores the comic num and the split words as two different keys.
Then that'd be stored into a list full of dictionaries.
"""

"""
------CREATING OUR MASTER WORD LIST----
I need to create a list full of all the words used in each comic so that I can do data analysis of the words.
This is done by getting the transcript key of each comic, storing it inside a list.
Then we split the words of each transcript, which creates it's own list inside the list we just made.
We then also need to make sure that certain words are not undercounted due to how xkcd wrote them 
(ex. 'alt]]', '{{alt' and 'alt' count as three different words
"""
# Storing each comics transcript key into a list
words = []
for dict_item in full_xkcd_repo:
    transcript = dict_item['transcript']
    words.append(transcript)

"""
We split the words of each transcript for further data analysis
For each transcript, the words are split and stored inside the transcript list called split_words.
This creates a 2D collection. 
The outer list holds the transcript for each comic.
The inner list is the split words of that specific comic
Ex. [
      ['list', 'of', 'words', 'used', 'in', 'first', 'comic',],
      ['list', 'of', 'words', 'used', 'in', 'second', 'comic', ],
      ['list', 'of', 'words', 'used', 'in', 'second', 'comic', ],
      [], <-Sometimes there are empty lists, which I need to account for
    ]
"""
split_words = []
for list_item in words:
    split_word = list_item.lower().split()
    split_words.append(split_word)

"""
Test code to see if it works
print(len(split_words))
print(split_words[0])
print(type(split_words[0]))
"""

# We store each word in each transcript into a single list, removing the 2D collection to just make one big list
# We also strip the special characters so that we get a better sense of what words are repeated
# (ex. 'alt', 'alt]]', and '{{alt' are different words

split_words_in_list = []
special_characters = '\'.[]"()<>?!@#$%^&*=+-_/{}\\|:;,`~'
for list_item in split_words:
    for y in list_item:
        y = y.strip(special_characters)
        if y.isalpha():
            split_words_in_list.append(y)

"""------WORDS ANALYSIS----"""

print("\nHow many total split strings are there?")
print(f"\tThere are {len(split_words_in_list)} total split strings.")

# Create a set of unique words
set_split_words_in_list = set(split_words_in_list)
print("\nHow many total unique split strings are there?")
print(f"\tThere are {len(set_split_words_in_list)} total unique strings that are only characters")


print("\nWhat's the longest string with only characters?")
long_word = ''
for word in set_split_words_in_list:
    if len(word) > len(long_word):
        long_word = word
print(f"\tThe string is {long_word}, with a total length of {len(long_word)} characters.")

print("\nWhat's the longest string with only characters that's actually a real word?")
long_word = ''
for word in set_split_words_in_list:
    if len(word) > len(long_word):
        time.sleep(0.5)  # Needed b/c otherwise, the API call can't keep up
        if is_real_word(word):
            long_word = word

print(f"\tThe word is {long_word}, with a total length of {len(long_word)} characters.")


"""-----FIELDS ANALYSIS-----"""
news_count = 0
xkcd_news = []
for dict_item in full_xkcd_repo:
    if dict_item['news'] != '':
        xkcd_news.append(dict_item)
        news_count += 1
        """
        print(f"Comic num: {dict_item['num']}")
        print(f"News: {dict_item['news']}")
        print(f"Link: https://xkcd.com/{dict_item['num']}\n")"""

print("\nHow many comics use the news key?")
print(f"\tThere are {news_count} comics where the news key is used in the comic.")

"""Are there any that repeats? What are they?"""

link_count = 0
xkcd_links = []
for dict_item in full_xkcd_repo:
    if dict_item['link'] != '':
        xkcd_links.append(dict_item)
        link_count += 1

print("\nHow many comics use the link key?")
print(f"\tThere are {link_count} comics where the link key is used for the comic.")




