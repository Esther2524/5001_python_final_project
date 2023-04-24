'''
CS5001
Final Project
Spring 2023
MyName: Zhixiao Wang

This is a file to extract and clean the data of artists from a url regular expressoions.
'''

import requests
import re

STATUS_CODE = 200

MISSING_VALUE = ""
REPLACED_VALUE = "Unknown"

ID_INDEX = 0
FIRST_NAME_INDEX = 1
LAST_NAME_INDEX = 2 


def get_artist_csv_file(artist_url):
    '''
    Function: 
        get_art_csv_file -- Read a CSV file containing data from a given URL, cleans the data, and returns the contents as a string.
    Parameters: 
        artist_url -- a string, the url of artist data
    Returns: 
        content_of_arts -- a string, containing the contents of the CSV file
    Error handling:
        HTTPError occurred if the HTTP response was invalid
        ConnectionError occurred if network problem occurred
        TimeoutError occurred if request times out
        requests.RequestException occurred if other errors occurred
        raise TypeError if artist_url is not a str
    '''
    try:
        
        if not isinstance(artist_url, str):
            raise TypeError(f"{artist_url} should be a str")
        
        response_artists_website = requests.get(artist_url)

        response_artists_website.raise_for_status()

        content_of_artists = response_artists_website.text

        return content_of_artists

    except requests.exceptions.HTTPError as he:
        print("HTTPError occurred in get_artist_csv_file()", type(he), he)

    except ConnectionError as ce:
        print("ConnectionError occurred in get_artist_csv_file()", type(ce), ce)

    except TimeoutError as te:
        print("TimeoutError occurred in get_artist_csv_file()", type(te), te)

    except requests.RequestException as re:
        print("Other Errors occurred in get_artist_csv_file().", type(re), re)




def replace_artist_empty_with_unknown(original_list):
    '''
    Function: 
        replace_artist_empty_with_unknown -- Replaces empty values in a list with the string "Unknown".
    Parameters: 
        original_list -- a list of values to be checked and modified.
    Return: 
        original_list -- the modified list
    Error handling:
        raise TypeError if original_list is not a list
    '''
    if not isinstance(original_list, list):
        raise TypeError(f"In replace_artist_empty_with_unknown(), {original_list} should be a list")
    
    for i in range(len(original_list)):
        if original_list[i] == MISSING_VALUE:
            original_list[i] = REPLACED_VALUE

    return original_list


def get_basic_info_from_artist_table(content_of_artists):
    '''
    Function:
        get_basic_info_from_artist_table -- takes in a string and extracts the artist IDs, first names, and last names from it using a regular expression.
    Parameters:
        content_of_artists -- a string, containing artist data
    Returns:
        list_of_artist_id --  a list of artist IDs extracted from the input string.
        list_of_first_name -- a list of artist first names extracted from the input string.
        list_of_last_name -- a list of artist last names extracted from the input string.
    Error handling:
        raise TypeError if content_of_artists is not a str
    '''
    if not isinstance(content_of_artists, str):
        raise TypeError(f"in get_basic_info_from_artist_table(), {content_of_artists} should be a string")

    # extract the data of id, first_name, last_name
    pattern_of_basic_info = r"\r\n(\d{1,});([^;]*);([^;]*);http.*\d{1,};"

    matches_of_basic_info = re.findall(pattern_of_basic_info, content_of_artists)
    
    list_of_artist_id = []
    list_of_first_name = []
    list_of_last_name = []

    for match in matches_of_basic_info:
        list_of_artist_id.append(match[ID_INDEX])
        list_of_first_name.append(match[FIRST_NAME_INDEX])
        list_of_last_name.append(match[LAST_NAME_INDEX])


    list_of_artist_id = replace_artist_empty_with_unknown(list_of_artist_id)
    list_of_first_name = replace_artist_empty_with_unknown(list_of_first_name)
    list_of_last_name = replace_artist_empty_with_unknown(list_of_last_name)

    return list_of_artist_id, list_of_first_name, list_of_last_name

   

def get_country_from_artist_table(content_of_artists):
    '''
    Function:
        get_country_from_artist_table -- Extracts the country of each artist from a string of artist data.
    Parameters:
        content_of_artists -- a string, containing artist data
    Returns:
        list_of_country -- a list of countries extracted from the input string
    Error handling:
        raise TypeError if content_of_artists is not a str  
    '''

    if not isinstance(content_of_artists, str):
        raise TypeError(f"get_country_from_artist_table(): {content_of_artists} should be a string")
    
    pattern_of_country = r";([^;]*);[^;]*;[^;]*;[^;]*(?:\r\n\d{1,};|\r$)"
    matches_of_country = re.findall(pattern_of_country, content_of_artists)

    list_of_country = matches_of_country[1:]
    list_of_country = replace_artist_empty_with_unknown(list_of_country)
    return list_of_country
    


def get_public_arist_data(artist_id, first_name, last_name, country):
    '''
    Function:
        get_public_artist_data -- Merges the information of each artist into a list of lists
    Parameters:
        artist_id -- a list of artist IDs
        first_name -- a list of first names of the artists
        last_name -- a list of last names of the artists
        country -- a list of countries of the artists
    Returns:
        data_of_artist_table -- a nested list containing the information of each artist, with each sublist containing the artist ID, first name, last name, and country
    Error handling:
        raise TypeError if artist_id is not a list
        raise TypeError if first_name is not a list
        raise TypeError if last_name is not a list
        raise TypeError if country is not a list
        raise ValueError if these lists are not of the same length
    '''

    if not isinstance(artist_id, list):
        raise TypeError(f"in get_public_arist_data(): the {artist_id} should be a list")
    if not isinstance(first_name, list):
        raise TypeError(f"in get_public_arist_data(): the {first_name} should be a list")
    if not isinstance(last_name, list):
        raise TypeError(f"in get_public_arist_data(): the {last_name} should be a list")
    if not isinstance(country, list):
        raise TypeError(f"in get_public_arist_data(): the {country} should be a list")
    if not (len(artist_id) == len(first_name) == len(last_name) == len(country)):
        raise ValueError("in get_public_arist_data(): the length of lists should be identical")


    data_of_artist_table = []

    for i in range(len(artist_id)):
        data_of_artist_table.append([artist_id[i], first_name[i], last_name[i], country[i]])

    return data_of_artist_table

















