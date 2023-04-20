'''
CS5001
Final Project
Spring 2023
MyName: Zhixiao Wang

This is a file to extract and clean the data of artworks from a url using regular expressoions.
'''

import requests
import re

STATUS_CODE = 200
ART_URL = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/public-art/exports/csv?lang=en&timezone=America%2FLos_Angeles&use_labels=true&delimiter=%3B"

TYPE_INDEX = 0
STATUS_INDEX = 1
MATERIAL_INDEX = 2
NEIGHBOURHOOD_INDEX = 3
ARTIST_ID_INDEX = 0
YEAR_INDEX = 1

MISSING_VALUE = ""
REPLACED_VALUE = "Unknown"


def get_art_csv_file():
    '''
    Function: 
        get_art_csv_file -- Read a CSV file containing data from a given URL, cleans the data, and returns the contents as a string.
    Parameters: 
        Nothing
    Returns: 
        content_of_arts -- a string, containing the infomation of the CSV file 
    Error handling:
        HTTPError occurred if the HTTP response was invalid
        ConnectionError occurred if network problem occurred
        TimeoutError occurred if request times out
        requests.RequestException occurred if other errors occurred
    '''

    try:
        
        download_arts = ART_URL
        response_of_art = requests.get(download_arts)

        # if response.status_code != STATUS_CODE:
            # raise requests.exceptions.HTTPError(f"Error occurred in get_art_csv_file(): status code {response.status_code}")
        
        response_of_art.raise_for_status()

        content_of_arts = response_of_art.text

        # Clean the data by replacing semicolons followed by a space with just a space.
        content_of_arts = content_of_arts.replace("; ", " ")
        return content_of_arts
        
       
    except requests.exceptions.HTTPError as he:
        print("HTTPError occurred in get_art_csv_file()", type(he), he)

    except ConnectionError as ce:
        print("ConnectionError occurred in get_art_csv_file()", type(ce), ce)

    except TimeoutError as te:
        print("TimeoutError occurred in get_art_csv_file()", type(te), te)

    except requests.RequestException as re:
        print("Other Errors occurred in get_art_csv_file().", type(re), re)
    


    
def replace_art_empty_with_unknown(original_list):
    '''
    Function: 
        Replaces empty values in a list with the string "Unknown".
    Parameters: 
        original_list -- a list of values to be checked and modified.
    Return: 
        original_list -- the modified list.
    Error handling:
        raise TypeError if original_list is not a list
    '''
    if not isinstance(original_list, list):
        raise TypeError(f"In replace_art_empty_with_unknown(), {original_list} should be a list")
    
    for i in range(len(original_list)):
        # If the item is an empty string, replace it with "Unknown".
        if original_list[i] == MISSING_VALUE:
            original_list[i] = REPLACED_VALUE

    return original_list


def get_work_title_from_art_table(content_of_arts):
    '''
    Function: 
        get_work_title_from_art_table -- Extracts the titles of public art works from a CSV file, and returns a list of the titles.
    Parameters:
        content_of_arts -- a string, containing the infomation of the CSV file
    Returns: 
        list_of_work_title -- a list of the titles of public art works
    Error handling:
        raise TypeError if content_of_arts is not a str
    '''

    if not isinstance(content_of_arts, str):
        raise TypeError(f"in get_work_title_from_art_table(), {content_of_arts} should be a string")

    # work_id, title, no, type, status, no, no, material, http, no, no, neighborhood, no, no, no, no, id, no, year
    # Define a regular expression pattern for extracting the titles of public art works
    pattern_of_work_title = r"\r\n\d{1,};([^;]*);"

    # extract the data of 'work_title'
    matches_of_work_title = re.findall(pattern_of_work_title, content_of_arts)

    # print(matches_of_work_title)
    # print(len(matches_of_work_title))

    list_of_work_title = matches_of_work_title

    # Clean the list of work titles by replacing empty strings with "Unknown".
    list_of_work_title = replace_art_empty_with_unknown(list_of_work_title)
    
    return list_of_work_title
    


def get_other_info_from_art_table(content_of_arts):
    '''
    Function: 
        get_other_info_from_art_table -- Extracts additional information about public art works from a CSV file, and returns four lists: 
                                         the types, statuses, materials, and neighbourhoods of the works.
    Parameters: 
        content_of_arts -- a string, containing the infomation of the CSV file
    Returns: 
        list_of_type -- a list, containing the types the public art works.
        list_of_status -- a list, containing the statuses the public art works.
        list_of_material -- a list, containing the materials the public art works.
        list_of_neighbourhood -- a list, containing the neighbourhoods the public art works.
    Error handling:
        raise TypeError if content_of_arts is not a str
    '''
    
    if not isinstance(content_of_arts, str):
        raise TypeError(f"in get_other_info_from_art_table(), {content_of_arts} should be a string")

    # extract the data of type, status, material, neighbourhood
    pattern_of_other_info = r";([^;]*);([^;]*);[^;]*;[^;]*;([^;]*);https[^;]*;[^;]*;[^;]*;([^;]*);"

    matches_of_other_info = re.findall(pattern_of_other_info, content_of_arts)
    list_of_type_and_status_and_material = matches_of_other_info

    list_of_type = []
    list_of_status = []
    list_of_material = []
    list_of_neighbourhood = []

    for lst in list_of_type_and_status_and_material:
        list_of_type.append(lst[TYPE_INDEX])
        list_of_status.append(lst[STATUS_INDEX])
        list_of_material.append(lst[MATERIAL_INDEX])
        list_of_neighbourhood.append(lst[NEIGHBOURHOOD_INDEX])

    # Clean each list by replacing empty strings with "Unknown".
    list_of_type = replace_art_empty_with_unknown(list_of_type)
    list_of_status = replace_art_empty_with_unknown(list_of_status)
    list_of_material = replace_art_empty_with_unknown(list_of_material)
    list_of_neighbourhood = replace_art_empty_with_unknown(list_of_neighbourhood)

    return list_of_type, list_of_status, list_of_material, list_of_neighbourhood
    

    
    
def get_artist_id_and_year_from_art_table(content_of_arts):
    '''
    Function: 
        get_artist_id_and_year_from_art_table -- Extracts ids and years information, and returns two lists: the artist ids and years of the works.
    Parameters: 
        content_of_arts -- a string, containing the infomation of the CSV file
    Returns: 
        list_of_artist_id -- a list, containing the artist ids the public art works.
        list_of_year -- a list, containing the years the public art works.
    Error handling:
        raise TypeError if content_of_arts is not a str
    '''

    if not isinstance(content_of_arts, str):
        raise TypeError(f"in get_artist_id_and_year_from_art_table(), {content_of_arts} should be a string")

    # extract the data of year
    pattern_of_id_and_year = r"([^;]*);[^;]*;([^;]*);[^;]*(?:\r\n\d{1,3};|\r$)"
    matches_of_id_and_year = re.findall(pattern_of_id_and_year, content_of_arts)

    # print(matches_of_artist_id)
    # print(len(matches_of_artist_id))

    # creates a new list of matches starting from the second match because the first match is the header row.
    list_of_id_and_year = matches_of_id_and_year[1::]

    list_of_artist_id = []
    list_of_year = []

    for lst in list_of_id_and_year:
        list_of_artist_id.append(lst[ARTIST_ID_INDEX])
        list_of_year.append(lst[YEAR_INDEX])
    
    # print(list_of_artist_id, list_of_year)
    # print(len(list_of_artist_id))

    # replace any empty values with the string "unknown"
    list_of_artist_id = replace_art_empty_with_unknown(list_of_artist_id)
    list_of_year = replace_art_empty_with_unknown(list_of_year)

    return list_of_artist_id, list_of_year



def get_public_art_data(work_title, type, status, material, neighbourhood, artist_id, year):
    '''
    Function:
    get_public_art_data -- Extracts data from the art CSV file and save it in a list of lists containing
                           the following fields for each artwork: work title, artist ID, type, status, material,
                           neighbourhood, and year. 
    Parameters:
        work_title -- a list, containing titles of public art works
        type -- a list, containing the types the public art works.
        status -- a list, containing the statuses the public art works.
        material -- a list, containing the materials the public art works.
        neighbourhood -- a list, containing the neighbourhoods the public art works.
        artist_id -- a list, containing the artist ids the public art works.
        year -- a list, containing the years the public art works.
    Returns:
        data_of_art_table -- a list of lists, containing all the infomation we need from the art table
    Error handling:
        raise TypeError if work_title is not a list
        raise TypeError if type is not a list
        raise TypeError if status is not a list
        raise TypeError if material is not a list
        raise TypeError if neighbourhood is not a list
        raise TypeError if artist_id is not a list
        raise TypeError if year is not a list
        raise ValueError if these lists are not of the same length
    '''

    if not isinstance(work_title, list):
        raise TypeError(f"in get_public_art_data(): the {work_title} should be a list")
    
    if not isinstance(type, list):
        raise TypeError(f"in get_public_art_data(): the {type} should be a list")
    
    if not isinstance(status, list):
        raise TypeError(f"in get_public_art_data(): the {status} should be a list")
    
    if not isinstance(material, list):
        raise TypeError(f"in get_public_art_data(): the {material} should be a list")
    
    if not isinstance(neighbourhood, list):
        raise TypeError(f"in get_public_art_data(): the {neighbourhood} should be a list")
    
    if not isinstance(artist_id, list):
        raise TypeError(f"in get_public_art_data(): the {artist_id} should be a list")
    
    if not isinstance(year, list):
        raise TypeError(f"in get_public_art_data(): the {year} should be a list")
    
    if not (len(work_title) == len(type) == len(status) == len(material) == len(neighbourhood) == len(artist_id) == len(year)):
        raise ValueError("in get_public_art_data(), the length of lists should be identical")

    # save data in a list of lists
    data_of_art_table = []
    
    for i in range(len(artist_id)):
        data_of_art_table.append([work_title[i], artist_id[i], type[i], status[i], material[i], neighbourhood[i], year[i]])
    
    # print(data_of_art_table) 
    return data_of_art_table





