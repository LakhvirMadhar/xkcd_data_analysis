"""
Goal:
* To make a catalog/explorer for the xkcd comic so that I can do data analysis on it.

TO DO:
* [DONE]Put comic info into a list and then a file:

* [DONE] Store the comic information in a file to avoid running the big for loop everytime

* [DONE] Print an un-formatted name for a given comic

* Print a formatted name for a given comic:
   - Comic Title:
   - Published date (Y-M-D):
   - Description:
      Make sure alt:title/ alt is excluded
   - Link to external site (some have that under their link dict)
   - Link to raw comic

* [DONE] Get comic by index

* Get comic by comic number

* [DONE] Create a method to update the json and list for when the comic updates

"""
import requests
import json
from datetime import datetime
from pathlib import Path


# This is the latest comic
url = 'https://xkcd.com/info.0.json'

# This is how you get a specific comic with a json
num = 0
url_02 = f'https://xkcd.com/{num}/info.0.json'

# Link to actual website
# NOTE: 404 leads to a Does Not Exist page. Keep that in mind
website_url = 'https://xkcd.com/'
website_url_custom = f'https://xkcd.com/{num}'

# Variable setup
xkcd_response = requests.get(url)
filename = 'all_xkcd.json'


def get_latest_comic_num():
    """Get the number of the latest comic"""
    xkcd_repo = xkcd_response.json()
    latest_comic = xkcd_repo['num']
    return latest_comic


def initialize_xkcd_list(last_comic_num):
    """Initializes our xkcd catalog into a list"""
    all_xkcd_repo = []
    file_path = Path('all_xkcd.json')
    if not file_path.exists():
        print("Adding comics to list. Please wait while program runs.")
        for index in range(1, last_comic_num+1):
            # Adds all xkcd comics to a list
            json_url = f'https://xkcd.com/{index}/info.0.json'
            r = requests.get(json_url)

            try:
                comic_info = r.json()
                all_xkcd_repo.append(comic_info)
            except requests.exceptions.JSONDecodeError as e:
                # To handle comic 404
                print(f"JSON Decode Error for Comic {index}:\n\t{e}")
                continue

        print("All comics have been added to the list.")
        return all_xkcd_repo
    else:
        print(f"{file_path} already exists. Skipping initializing.")


def initialize_xkcd_json(all_xkcd_repo):
    """If a json file of the xkcd doesn't exist, we take our list and put it a json file"""
    file_path = Path('all_xkcd.json')
    if not file_path.exists():
        with open(filename, 'w') as f:
            json.dump(all_xkcd_repo, f)
            print("Json file created")
    else:
        print(f"{file_path} already exists. Skipping json creation.")


def update_xkcd_catalog(all_xkcd_repo):
    """
    Appends the latest comic(s) to our xkcd_list.
    Then overwrites the json file with our appended list.
    """
    to_pass = all_xkcd_repo[-1]['num']
    for index in range(to_pass, get_latest_comic_num()+1):
        if index == to_pass:
            pass
        else:
            # Get the missing comic data
            json_url = f'https://xkcd.com/{index}/info.0.json'
            r = requests.get(json_url)

            # Append that to our list
            comic_info = r.json()
            all_xkcd_repo.append(comic_info)

            # Append that to our json
            with open(filename, 'w') as f:
                json.dump(all_xkcd_repo, f)
            print(f"{json_url} successfully added")


def is_xkcd_updated(all_xkcd_repo):
    """Checks to see if there's an added comic to xkcd"""
    latest_comic_num = get_latest_comic_num()
    if all_xkcd_repo[-1]['num'] < latest_comic_num:
        print(f"Current comic num in list is: {all_xkcd_repo[-1]['num']}.")
        print(f"Latest comic is: {latest_comic_num}.")
        print(".json needs an update")
        # Update the file
        update_xkcd_catalog(all_xkcd_repo)
        print("Local json file is now all up to date!")
        print(f"Latest comic on file is comic {all_xkcd_repo[-1]['num']}.")
    else:
        print("Local json file is all up to date!")
        print(f"Latest comic on file is comic {all_xkcd_repo[-1]['num']}.")


def get_status_code():
    if xkcd_response.status_code == 200:
        print("Connection Successful")
    else:
        print(f"Status Code Issue: {xkcd_response.status_code}")


def get_comic_info(all_xkcd_repo,index):
    """
    Shows the info of the comic by index
    NEEDS TO MAKE SURE THAT INDEX ISN'T OUT OF BOUNDS via variant does_comic_num_exist
    """
    for k, v in all_xkcd_repo[index].items():
        print(f"{k}: {v}")


def change_date_format(xkcd_comic):
    """Changes the format of the published date for the comic to be month day, year"""
    # Get the published date
    published_date = f"{xkcd_comic['month']}-{xkcd_comic['day']}-{xkcd_comic['year']}"

    # Convert string to datetime object
    parsed_date = datetime.strptime(published_date, "%m-%d-%Y")

    # Format the date to "Month Day, Year"
    formatted_date = parsed_date.strftime("%b %d, %Y")

    return formatted_date


def does_comic_num_exist(repo_name, comic_num):
    """Checks to see if the given comic exists"""
    latest_comic_num = get_latest_comic_num()
    for dict_item in repo_name:
        if comic_num == 404:
            print(f"Comic {comic_num} does not exist.")
            print(f"The next available comic is {comic_num+1}.")
            break
        elif comic_num > latest_comic_num:
            print(f"Comic {comic_num} does not exist in my json.")
            print(f"The latest comic available is {latest_comic_num}")
            break
        elif dict_item['num'] == comic_num:
            print(dict_item)
            break


def is_real_word(word):
    """Checks if a word in a comic is part of a dictionary"""
    dict_url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    dict_response = requests.get(dict_url)
    if dict_response.status_code == 200:
        return True
    elif dict_response.status_code == 404:
        return False


# This block of code only executes when this specific file is run
if __name__ == '__main__':
    return_xkcd_repo = initialize_xkcd_list(get_latest_comic_num())
    initialize_xkcd_json(return_xkcd_repo)


