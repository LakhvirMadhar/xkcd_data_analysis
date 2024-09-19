"""
--------ANALYSIS QUESTIONS-------

* Make a chart to show how many comics were published each month

-------WORDS ANALYSIS-------
* [DONE] How many total strings are there?

* [DONE] How many unique strings are there?

* [DONE] What's the longest string to show up in the totality of comics?

* [DONE] What's the longest real word to show up in the totality of comics?

* [DONE] How many comics has no transcripts to them?

* [DONE] What's the most common string? Visualize the x most common words.


-------DATES-------
* [DONE] From what years/dates were the comics running from?

* [DONE] How many comics were created in each year of publication?

* [DONE] Plot the total amount of comics published each year.

* [DONE] What's the average publication rate each year, excluding the current year?

* [DONE] What's the median amount of comics published each year, excluding the current year?

* [DONE] What's the longest gap time(s) b/w comics?

* [DONE] What's the average gap times b/w comics?

* [DONE] What's the median gap times b/w comics?

* [DONE] Plot the frequencies of the time gap times, in descending order.


-------FIELDS-------
* [DONE] How many comics use the links key?

* [DONE] How many comics use the news key?

* [DONE] Comic 404 does not exist. Are there any other comics that don't exist in the sequence?

"""
from xkcd_catalog_functions import *
import time
import matplotlib.pyplot as plt
import datetime

# Load our json file which contains all of our comics
filename = 'all_xkcd.json'
with open(filename) as f:
    full_xkcd_repo = json.load(f)

# Verify that the json file is up-to-date. If not, update the file.
is_xkcd_updated(full_xkcd_repo)

# The Data Analysis of our xkcd.json
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

print("\nWhat are top 25 most used words?")
word_count = {}
for word in split_words_in_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_word_count = dict(sorted(word_count.items(), key=lambda item: (item[1], item[0]), reverse=True))
top_25_words = dict(list(sorted_word_count.items())[:26])


print(f"Let's plot the top 25 words!")
pixels_width = 1920
pixels_height = 1080
dpi = 100
fig_size = (pixels_width/dpi, pixels_height/dpi)

x_values = list(top_25_words.keys())
y_values = list(top_25_words.values())

fig_01 = plt.figure()
fig_01.set_size_inches(fig_size)

plt.style.use('seaborn-v0_8')
plt.bar(x_values, y_values)

plt.title("Top 25 Repeated Words in XKCD Comics", fontsize=24, pad=20, fontweight='bold')
plt.xlabel("Words", fontsize=18, fontweight='bold')
plt.xticks(rotation=45, ha='right', fontsize=16)
plt.ylabel("Amount", fontsize=18, labelpad=20, fontweight='bold')
plt.yticks(fontsize=16)

for i, value in enumerate(y_values):
    plt.text(i, value, str(value), ha='center', va='bottom', fontsize=14)

plt.savefig('Top 25 Words in XKCD Comics')

print("\nHow many comics have no transcripts to them?")
empty_comics = []
for dict_item in full_xkcd_repo:
    if not dict_item['transcript']:
        empty_comics.append(dict_item)

print(f"\tThere are {len(empty_comics)} comics with no transcripts to them.")


"""-----DATES ANALYSIS-----"""
print("\nHow long has the comic been running?")

start_date = datetime.date(int(full_xkcd_repo[0]['year']),
                           int(full_xkcd_repo[0]['month']),
                           int(full_xkcd_repo[0]['day']))

latest_date = datetime.date(int(full_xkcd_repo[-1]['year']),
                            int(full_xkcd_repo[-1]['month']),
                            int(full_xkcd_repo[-1]['day']))
difference = latest_date - start_date
days_in_year = 365.25
years = difference.days / days_in_year
print(f"The first comic was published on {start_date} and the latest comic was published on {latest_date}.")
print(f"The comic has been running for {int(years)} years!")

print("\nHow many comics were made in each year?")
comic_years = {}
for dict_item in full_xkcd_repo:
    comic_year = dict_item['year']
    if comic_year in comic_years:
        comic_years[comic_year] += 1
    else:
        comic_years[comic_year] = 1

print("\nLet's plot the amount of comics published each year!")
year_values = list(comic_years.keys())
total_comics_each_year = list(comic_years.values())

fig_02 = plt.figure()
fig_02.set_size_inches(fig_size)

plt.bar(year_values, total_comics_each_year)

plt.title("XKCD Comics Released By Year", fontsize=24, pad=20, fontweight='bold')
plt.xlabel("Year", fontsize=18, labelpad=20, fontweight='bold')
plt.xticks(fontsize=16)
plt.ylabel("Amount", fontsize=18, labelpad=20, fontweight='bold')
plt.yticks(fontsize=16)

for index, value in enumerate(total_comics_each_year):
    plt.text(index, value, str(value), ha='center', va='bottom', fontsize=16)

plt.savefig('Total XKCD Comics Released By Year')

print("\nWhat's the average amount of comics published each year, excluding the current year?")
total = sum(total_comics_each_year[:-1])
average = total/len(total_comics_each_year)-1

print(f"\tThe average comics published each year is {average:.2f} comics.")

print("\nWhat's the median number of comics published each year, excluding the current year")
sorted_yearly_comic_rate = sorted(total_comics_each_year[:-1])
n = len(sorted_yearly_comic_rate)
median_yearly_comics = 0
if n % 2 == 1:
    median_yearly_comics = sorted_yearly_comic_rate[n//2]
elif n % 2 == 0:
    median_yearly_comics = (sorted_yearly_comic_rate[(n//2)-1] + sorted_yearly_comic_rate[n//2]) / 2

print(f"\tThe median number of comics published each year is {median_yearly_comics} comics.")

print("\nLet's create a data structure to store the time gaps between comics!")
# Once that is done, see which is the greatest difference. Make sure to account for ties
# Based on the results, see if there's some plotting potential, like avg, median, mean of when comics get published
comic_years_difference = []
for index in range(0, len(full_xkcd_repo)-1):
    initial_date = datetime.date(int(full_xkcd_repo[index]['year']),
                                 int(full_xkcd_repo[index]['month']),
                                 int(full_xkcd_repo[index]['day']))

    date_after = datetime.date(int(full_xkcd_repo[index+1]['year']),
                               int(full_xkcd_repo[index+1]['month']),
                               int(full_xkcd_repo[index+1]['day']))

    difference = date_after - initial_date
    new_dict = {
        'comic_range': f"Between comic {full_xkcd_repo[index]['num']} and comic {full_xkcd_repo[index+1]['num']}",
        'initial_date': initial_date,
        'date_after': date_after,
        'difference': difference.days
    }

    comic_years_difference.append(new_dict)

print("\tTime Gap Data Structure created!")


print("\nWhat's the longest gap time between comics?")
largest_time_gap = 0
for dict_item in comic_years_difference:
    if dict_item['difference'] > largest_time_gap:
        largest_time_gap = dict_item['difference']

print(f"\tThe largest time gap is {largest_time_gap} days!")

print("\nWhat's the average time gap between comics?")
time_gaps = []
for dict_item in comic_years_difference:
    time_gaps.append(dict_item['difference'])

average_time_gap = sum(time_gaps)/len(time_gaps)

print(f"\tThe average time gap between comics is {average_time_gap:.2f}!")


print("\nWhat's the median time gap between comics?")
sorted_time_gaps = sorted(time_gaps)
n = len(sorted_time_gaps)
median_time_gap = 0
if n % 2 == 1:
    median_time_gap = sorted_time_gaps[n//2]
elif n % 2 == 0:
    median_time_gap = (sorted_time_gaps[(n//2)-1] + sorted_time_gaps[n//2]) / 2

print(f"\tThe median time gap between comics is {median_time_gap} days!")

print("\nWhat are the frequencies of the time gaps?")
time_gap_frequency = {}
for days in time_gaps:
    time_gap = days
    if time_gap in time_gap_frequency:
        time_gap_frequency[time_gap] += 1
    else:
        time_gap_frequency[time_gap] = 1

print("\tLet's plot the frequencies of the time gaps!")

fig_03 = plt.figure()
fig_03.set_size_inches(fig_size)

x_xkcd_days = list(time_gap_frequency.keys())
y_xkcd_frequency = list(time_gap_frequency.values())

plt.bar(x_xkcd_days, y_xkcd_frequency)

plt.title("XKCD Time Gap Frequencies", fontsize=24, pad=20, fontweight='bold')
plt.xlabel("Days Before Next Comic", fontsize=18, labelpad=20, fontweight='bold')
plt.xticks(fontsize=16)
plt.ylabel("Frequency", fontsize=18, labelpad=20, fontweight='bold')
plt.yticks(fontsize=16)

for x_xkcd_days, y_xkcd_frequency in zip(x_xkcd_days, y_xkcd_frequency):
    plt.text(x_xkcd_days, y_xkcd_frequency+15, str(y_xkcd_frequency), ha='center', va='bottom', fontsize=16)

plt.savefig("XKCD Time Gap Frequencies Jan 1, 2006 - September 19, 2024.png")

"""-----FIELDS ANALYSIS-----"""
print("\nHow many comics use the news key?")
news_count = 0
xkcd_news = []
for dict_item in full_xkcd_repo:
    if dict_item['news'] != '':
        xkcd_news.append(dict_item)
        news_count += 1

print(f"\tThere are {news_count} comics where the news key is used in the comic.")

print("\nHow many comics use the link key?")
link_count = 0
xkcd_links = []
for dict_item in full_xkcd_repo:
    if dict_item['link'] != '':
        xkcd_links.append(dict_item)
        link_count += 1

print(f"\tThere are {link_count} comics where the link key is used for the comic.")


print(f"\nComic 404 does not exist. Are there any other comics that don't exist in the sequence?")
comic_num = 0
comic_sequence = []
for dict_item in full_xkcd_repo:
    comic_num += 1
    if comic_num != dict_item['num']:
        # Debug code:
        # print(f"\nComic num {comic_num} does not match {dict_item['num']}")
        # print(f"That comic doesn't exist!!!")

        # Append the missing comic num to a list, correct comic num
        comic_sequence.append(comic_num)
        comic_num = dict_item['num']

print(f"\tComic(s) {comic_sequence} skips the sequence!")
