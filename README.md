# XKCD Comics Data Analysis

This repository contains a comprehensive analysis of XKCD comics using a dataset in JSON format. The project explores various aspects of XKCD comics, including word frequency, publication patterns, and time gaps between comics. The analysis generates visualizations and reports to provide insights into the XKCD universe.

## **Project Overview**

The analysis covers:

- **Word Analysis:** Examines the frequency and uniqueness of words found in XKCD comics, identifies the longest strings, longest real words, and visualizes the 25 most common words.
- **Publication Analysis:** Investigates the publication timeline, including the number of comics released each year, average and median publication rates, and identifies any missing comics in the sequence.
- **Time Gap Analysis:** Analyzes gaps between comic releases, including the longest gap, average gap, and median gap, with visualizations of time gap frequencies.
- **Field Analysis:** Counts occurrences of specific fields in the dataset, such as the use of links and news keys, and identifies any missing comics.

## **Charts**

- **Word Frequency Visualization:** Bar chart of the top 25 most common words in XKCD comics.
- **Yearly Publication Trends:** Bar chart showing the number of comics published each year.
- **Time Gap Frequency Plot:** Bar chart of the frequencies of gaps between comic releases.

## **Output**

The analysis produces the following output files:

- `Top 25 Words in XKCD Comics.png` - Bar chart of the top 25 most common words.
- `Total XKCD Comics Released By Year.png` - Bar chart of comics published each year.
- `XKCD Time Gap Frequencies.png` - Bar chart of the frequencies of time gaps between comic releases.
- `analysis_output.txt` - A text file containing detailed analysis results and findings.

## **Acknowledgements**

- [XKCD](https://xkcd.com/info.0.json) - For providing the dataset.
- [Matplotlib](https://matplotlib.org/) - For the plotting library used in visualizations.
