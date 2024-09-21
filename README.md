# XKCD Exploratory Data Analysis

This exploratory data analysis project aims to provide insights about the xkcd comic series, made available via the xkcd API.

## **Project Overview**

The analysis covers:

- **Word Analysis:** Examines the frequency and uniqueness of words found in XKCD comics, identifies the longest strings, longest real words, and visualizes the 25 most common words.
- **Publication Analysis:** Investigates the publication timeline, including the number of comics released each year, average and median publication rates, and identifies any missing comics in the sequence.
- **Publication Time Gap Analysis:** Analyzes gaps between comic releases, including the longest gap, average gap, and median gap, with visualizations of time gap frequencies.
- **Field Analysis:** Counts occurrences of specific fields in the dataset, such as the use of links and news keys, and identifies any missing comics.

## **Project Setup**
There are two .py files for this project.
- **xkcd_catalog_functions.py**: Contains functions used to initialize and update our local JSON file containing all the information of the xkcd comics. Also contains helper functions to conduct data analysis on the xkcd comics and to gain a better understanding of the xkcd JSON.
- **xkcd_analysis.py**: The core script for conducting exploratory data analysis of the xkcd comic series.

# **Results**

The following questions were answered as part of the exploratory data analysis:

## *Words Analysis*
### How many total unique split strings are there?
    There are 16726 total unique strings that are only characters

### What's the longest string, containing only characters?
    The string is glhdfkuouahuuuuguuuaaauuauuuuuuugggggh, with a total length of 38 characters.

### What's the longest string, containing only characters, that's actually a real word?
    The word is supercalifragilisticexpialidocious, with a total length of 34 characters.

### What are top 25 most used words?
![Top 25 Words in XKCD Comics](https://github.com/user-attachments/assets/b85b598e-e8fb-4a98-ac53-0e41434e4ed1)

## *Publication Analysis*
### How long has the comic been running?
    The first comic was published on 2006-01-01 and the latest comic was published on 2024-09-18.
    The comic has been running for 18 years!

### What's the average amount of comics published each year, excluding the current year?
	The average number of comics published each year is 150.21 comics.

### What's the median number of comics published each year, excluding the current year
	The median number of comics published each year is 157.0 comics.

### Comic 404 does not exist. Are there any other comics that don't exist in the sequence? List them.
	Comic(s) [404] skips the sequence!

### How many comics were made in each year?
![Total XKCD Comics Released By Year](https://github.com/user-attachments/assets/985d14f0-9c13-4266-9a6b-199c1f7c65c5)

## *Publication Time Gap Analysis*
### What's the longest gap time between comics?
	The largest time gap is 5 days!

### What's the average time gap between comics?
	The average time gap between comics is 2.29 days!

### What's the median time gap between comics?
	The median time gap between comics is 2 days!

### What are the frequencies of the time gaps?
![XKCD Time Gap Frequencies Jan 1, 2006 - September 19, 2024](https://github.com/user-attachments/assets/434ebfcd-0dc1-4442-b374-8304460376ad)

## *Fields Analysis*
### How many comics use the news key?
	There are 55 comics where the news key is used in the comic.

### How many comics use the link key?
	There are 72 comics where the link key is used for the comic.

### How many comics have no transcripts to them?
    There are 1321 comics with no transcripts to them.


## **Acknowledgements**

- [XKCD](https://xkcd.com/info.0.json) - For providing the API to their comics.
- [Free Dictionary API](https://dictionaryapi.dev/) - For providing a free dictionary API to crosscheck if strings were real words.
