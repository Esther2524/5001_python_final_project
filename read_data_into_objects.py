'''
CS5001
Final Project
Spring 2023
MyName: Zhixiao Wang

This is a file to read artist and artwork data into objects depending on the country selected by the user.

Note:
The data passed to the function is from df_art and df_artist. 
The function generates objects by extracting the required data frame based on the countries entered by the user. 
This allows objects to be created and filled with data when the user interacts with the program and makes a selection.
'''

import pandas as pd

from class_of_artist import Artist
from class_of_art import ArtWork


def read_data_into_objects_by_country(df_art, df_artist, chosen_country):
    '''
    Function:
        read_data_into_objects_by_country -- read data into objects according to the selected country and return lists of objects
    
    Parameter:
        df_art -- a pandas dataframe, containing information about artwork
        df_artist -- a pandas dataframe, containing information about artists
        chosen_country -- a string that represents the chosen country
    
    Returns:
        list_of_artist_objects -- a list of Artist objects for the selected country
        list_of_artwork_objects -- a list of ArtWork objects for the selected country
    
    Error handling:
        raise TypeError if df_art is not a pandas DataFrame
        raise TypeError if df_artist is not a pandas DataFrame
        raise TypeError if chosen_country is not a string
    '''
    
    if not isinstance(df_art, pd.DataFrame):
        raise TypeError(f"in read_data_into_objects_by_country(): {df_art} should be a data frame")
    
    if not isinstance(df_artist, pd.DataFrame):
        raise TypeError(f"in read_data_into_objects_by_country(): {df_artist} should be a data frame")
    
    if not isinstance(chosen_country, str):
        raise TypeError(f"in read_data_into_objects_by_country(): {chosen_country} should be a string")
    
    # create a list of Artist objects for the selected country
    list_of_artist_objects = []

    # create artist objects based on the selected country
    for i in range(len(df_artist["country"])):
        if df_artist["country"][i] == chosen_country:
            artist = Artist(df_artist["artist id"][i], df_artist["first name"][i], df_artist["last name"][i], df_artist["country"][i])
            list_of_artist_objects.append(artist)

    # artist id links two tables
    list_of_artwork_objects = []

    for i in range(len(df_art["artist id"])):
        for artist in list_of_artist_objects:
            if (artist.id == df_art["artist id"][i]) or (artist.id in df_art["artist id"][i].split(",")):
                artwork = ArtWork(df_art["work title"][i], artist.id, df_art["type"][i], df_art["status"][i], df_art["material"][i], df_art["neighbourhood"][i], df_art["year"][i])
                list_of_artwork_objects.append(artwork)

    return list_of_artist_objects, list_of_artwork_objects








    
