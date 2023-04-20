'''
CS5001
Final Project
Spring 2023
MyName: Zhixiao Wang

This is a file to filter out the data after user selection and generate the corresponding charts.

Note:
This file is not finished because it involves user interaction, and there will be larger changes later

'''
import tkinter as tk
from tkinter import ttk
import matplotlib.pylab as plt
import pandas as pd

from read_data_into_objects import *

def classify_artworks_by_criterion(artworks, criterion):
    '''
    Function:
        classify_artworks_by_criterion -- classifies artworks by a given criterion and returns a dictionary where the keys are the unique values of the criterion found in the artworks, 
                                          and the values are the number of artworks that have each value of the criterion.
    Parameters:
        artworks -- a list of artwork objects
        criterion -- a string, the name of an attribute of the artwork objects to be used as the criterion for classification.
    Returns:
        dic_of_artworks_by_criterion -- a dictionary, where the keys are the unique values of the criterion found in the
                                        artworks, and the values are the number of artworks that have each value of the criterion.
    Error handling:
        raise TypeError if artworks is not a list
        raise TypeError if criterion is not a string
    '''

    if not isinstance(artworks, list):
        raise TypeError(f"in classify_artworks_by_criterion(): {artworks} should be a list")
    if not isinstance(criterion, str):
        raise TypeError(f"in classify_artworks_by_criterion(): {criterion} should be a string")

    # in the list of artwork objects, some artworks objects will be created many times
    # because one artwork may have many artists, and I use id of artists to create corresponding artwork objects

    # A set is an unordered collection of unique elements, meaning that it can only contain one copy of each element, and the order in which the elements were added to the set is not preserved.
    # unique_artworks is intended to store unique instances of the ArtWork class.
    # When we add an ArtWork instance to the unique_artworks set using the add() method, 
    # the __eq__ method of the ArtWork class is used to determine if the instance is already present in the set.
    
    unique_artworks = set()
    
    for artwork in artworks:
        unique_artworks.add(artwork)

    dic_of_artworks_by_criterion = {}
        # artwork is an object of class ArtWork, so self.artworks is a list of artwork objects

    for artwork in unique_artworks:
        # print(artwork)
        # getattr function to get the value of the attribute specified by the criterion parameter from the artwork object
        # in this case, artwork_criterion is like artwork.type
        # getattr(object, attribute) is equal to object.attribute, like "sculpture" = artwork.type = getattr(artwork, "type")
        artwork_criterion = getattr(artwork, criterion)
        if artwork_criterion in dic_of_artworks_by_criterion:
            dic_of_artworks_by_criterion[artwork_criterion] += 1
        else:
            dic_of_artworks_by_criterion[artwork_criterion] = 1

        # the dic artworks_by_type is like 
    
    return dic_of_artworks_by_criterion



def display_chart_and_output_result(df_art, df_artist, country, category):
    '''
    Function:
        display_chart_and_output_result --  Classifies artworks by a given category for the artworks created by artists from a given country. 
                                            Outputs the classification result as a dictionary and displays a chart based on the result.
    
    Parameters:
        df_art -- a pandas DataFrame, containing the artwork data
        df_artist -- a pandas DataFrame, containing the artist data
        country -- a string, representing the country for which the artworks will be classified
        category -- a string, representing the category by which the artworks will be classified
    
    Returns:
        dict_of_artworks --  a dictionary where the keys are the unique values of the category found in the artworks, and the values are the number of artworks that have each value of the category
          
    Error handling:
        raise TypeError if df_art is not a pandas DataFrame
        raise TypeError if df_artist is not a pandas DataFrame
        raise TypeError if country is not a string
        raise TypeError if category is not a string
    '''

    if not isinstance(df_art, pd.DataFrame):
        raise TypeError(f"in display_chart_and_output_result(): {df_art} should be a data frame")
    if not isinstance(df_artist, pd.DataFrame):
        raise TypeError(f"in display_chart_and_output_result(): {df_artist} should be a data frame")
    if not isinstance(country, str):
        raise TypeError(f"in display_chart_and_output_result(): {country} should be a string")
    if not isinstance(category, str):
        raise TypeError(f"in display_chart_and_output_result(): {category} should be a string")

    # get the data for the selected country
    list_of_artist_objects, list_of_artwork_objects = read_data_into_objects_by_country(df_art, df_artist, country)
    

    # classify artworks by category/criterion and get a dict
    # This dict is used for drawing charts
    dict_of_artworks = classify_artworks_by_criterion(list_of_artwork_objects, category)

    # output the result, save the result in a dict
    print("The results of this user selection is:\n", dict_of_artworks, "\n")
    
    # display the chart
    
    if category == "year":
        display_bar_chart(dict_of_artworks, country, category)

    
    else:
        display_pie_chart(dict_of_artworks, country, category)

    
    



def display_pie_chart(dict_of_artworks, country, category):
    '''
    Function:
        display_pie_chart -- display a pie chart showing the distribution of artworks by a given category
    Parameters:
        dict_of_artworks -- a dictionary, containing the count of artworks by the given category.
        country -- a str, the name of the country for which the artworks are being displayed.
        category -- a str, the category by which the artworks are being classified.
    Returns:
        nothing
    Error handling:
        raise TypeError if dict_of_artworks is not a dictionary
        raise TypeError if country is not a string
        raise TypeError if category is not a string
    '''
    if not isinstance(dict_of_artworks, dict):
        raise TypeError(f"in display_pie_chart(): {dict_of_artworks} should be a dictionary")
    if not isinstance(country, str):
        raise TypeError(f"in display_pie_chart(): {country} should be a string")
    if not isinstance(category, str):
        raise TypeError(f"in display_pie_chart(): {category} should be a string")

    fig, ax = plt.subplots(figsize=(10, 7))
    autopct_format = "%1.1f%%"
    ax.pie(dict_of_artworks.values(), labels=dict_of_artworks.keys(), autopct=autopct_format,)
    ax.set_title(f"Artworks of Artists from {country} by {category.capitalize()} ")
    plt.show()

    


def display_bar_chart(dict_of_artworks, country, category):
    '''
    Function:
        display_bar_chart -- display a bar chart of the number of artworks of artists from a specific country sorted by year.
    Parameters:
        dict_of_artworks -- a dictionary, containing the number of artworks of artists from a specific country sorted by year.
        country -- a string, representing the country of the artists.
        category -- a string, representing the category to classify the artworks, in this case, it is always "year".
    Returns:
        nothing
    Error handling:
        raise TypeError if dict_of_artworks is not a dictionary
        raise TypeError if country is not a string
        raise TypeError if category is not a string
    '''

    if not isinstance(dict_of_artworks, dict):
        raise TypeError(f"in display_pie_chart(): {dict_of_artworks} should be a dictionary")
    if not isinstance(country, str):
        raise TypeError(f"in display_pie_chart(): {country} should be a string")
    if not isinstance(category, str):
        raise TypeError(f"in display_pie_chart(): {category} should be a string")

    # Create and show the bar chart
    fig, ax = plt.subplots(figsize=(12, 8))

    # Sort the dictionary items by key
    sorted_items = sorted(dict_of_artworks.items())
    # Unpack the sorted dictionary items into separate lists for x and y values
    x_values, y_values = zip(*sorted_items)
    ax.bar(x_values, y_values)

    # Set the x-axis label
    ax.set_xlabel("Year")

    # Set the y-axis label
    ax.set_ylabel("Artwork Count")

    # Set the title of the chart
    ax.set_title(f"Artwork of Artist from {country} Counts by {category.capitalize()}")

    # Set the y-axis range and interval
    max_value = max(y_values)
    ax.set_yticks(range(0, max_value + 1, 1))

    plt.show()





# def draw_line_chart(dict_of_artworks_by_criterion, country):

#     fig, ax = plt.subplots()

#     # plot the data as a line chart
#     ax.plot(year, counts)

#     # set the title and labels for the chart
#     ax.set_title(f"Line Chart of artworks from {country}")
#     ax.set_xlabel("year")
#     ax.set_ylabel("counts")
    
#     # show the chart
#     plt.show()


# def display_scatter_plot(dict_of_artworks_by_criterion):


#     # Create a scatter plot
#     plt.plot(dict_of_artworks_by_criterion.keys(), dict_of_artworks_by_criterion.values(), linestyle='--', marker='o', color='b')
#     plt.xlabel('X Axis')
#     plt.ylabel('Y Axis')

#     # Set the title of the chart
#     plt.title('Scatter Plot')

#     # Show the plot
#     plt.show()

