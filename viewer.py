

import pandas as pd
import tkinter as tk
from tkinter import ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


from read_data_into_objects import *
from filter_data import *



# view里面有 input 和 visulization

# I don't want to make four global variables, I want just one global variable root
# but I need to change start_page, page_one, or page_two in my function if necessary
# how can I implement it?
# top-level window


# start_page, page_one, and page_two are created as child frames of the root window.



def create_child_frames(root):
    '''
    Function:
        create_child_frames -- Create child frames for the given root window.
    Parameters:
        root -- a object, the root window object
    Returns:
        frames -- a list of ttk.Frame objects representing the child frames. 
                  The first frame in the list is the "start_page", the second is "page_one", and the third is "page_two".
    Error handling:
        raise TypeError if root is not an object
    '''

    if not isinstance(root, object):
        raise TypeError(f"{root} should be an object")

    # set the window title
    root.title("Artwork Viewer")

    # set the window size
    root.geometry("1100x800")

    # set the style of all buttons
    s1 = ttk.Style()
    s1.configure('TButton', foreground='#19A7CE')


    # create child frames and store them in a list
    frames = []
    frames.append(ttk.Frame(root))  # add start_page to index 0
    frames.append(ttk.Frame(root))  # add page_one to index 1
    frames.append(ttk.Frame(root))  # add page_two to index 2

    return frames


def create_start_page(df_art, df_artist, frames):
    '''
    Function:
        create_start_page -- Creates the start page frame containing labels, comboboxes, and a button that when clicked,
                             calls generate_first_output() function to generate and display a chart based on user's input.
    Parameters:
        df_art -- a pandas dataframe, containing information about artworks
        df_artist -- a pandas dataframe, containing information about artists
        frames : a list of ttk.Frame objects, representing the child frames of the root window. The first frame in the list is the "start_page".
    Returns:
        None
    Error handling:
        raise TypeError if df_art is not a pandas dataframe
        raise TypeError if df_artist is not a pandas dataframe
        raise TypeError if frames is not a list
    '''

    if not isinstance(df_art, pd.DataFrame):
        raise TypeError(f"{df_art} should be a pandas dataframe")
    if not isinstance(df_artist, pd.DataFrame):
        raise TypeError(f"{df_artist} should be a pandas dataframe")
    if not isinstance(frames, list):
        raise TypeError(f"{frames} should be a  a list of ttk.Frame objects")


    title_of_start_page = ttk.Label(frames[0], text="Start Page", font = ("Arial", 24, "bold"), foreground = "#146C94")
    title_of_start_page.pack(padx = 10, pady = 10)

    # widgets on the start page
    text_one = "\nHi, welcome to Artwork Viewer!\n"
    text_two = "\nPlease select the country you are interested in and explore a variety of artworks.\n"
    text_three = "\nClicking the button, you will see the distribution of all artworks created by artists from that country by type, status, material, neighbourhood, and year\n"
    label_explanation = ttk.Label(frames[0], text = text_one + text_two + text_three, font=("Arial", 15))
    label_explanation.pack(padx = 10, pady = 15)

    

    label_country = ttk.Label(frames[0], text="Select a country:", font=("Arial", 15, "bold"))
    label_country.pack(padx=10, pady=10)

    options_country = df_artist["country"].unique()
    options_country = [option.replace("[", "").replace("]", "") for option in options_country]

    combo_country = ttk.Combobox(frames[0], values=options_country, state="readonly")
    combo_country.pack(padx=10, pady=5)

    label_category = ttk.Label(frames[0], text="Select a category:", font=("Arial", 15, "bold"))
    label_category.pack(padx=10, pady=10)

    # get coloums's names except for the first two items
    options_category = df_art.columns.tolist()
    options_category = options_category[2:]

    combo_category = ttk.Combobox(frames[0], values=options_category, state="readonly")
    combo_category.pack(padx=10, pady=5)


    button = ttk.Button(frames[0], text="Show chart", command=lambda: generate_first_output(df_art, df_artist, combo_country.get(), combo_category.get(), options_category, frames))
    button.pack(padx=10, pady=10)

    explanation1 = "\nNote:\n\n[country]: the nationality of the artist of the artworks.\n"
    explanation2 = "\n[category]: You can check the distribution of artworks according to many different categories.\n"
    explanation3 = "\n[type]: the type of the artwork, such as sculpture, mural, and so on.\n\n[status]: the status of the artwork, in palce, no longer in place or deaccessioned.\n"
    explanation4 = "\n[material]: the type of the artwork.\n\n[neighbourhood]: the location of the artwork.\n\n[year]: the year in which the artwork was created."
    label_explanation = ttk.Label(frames[0], text = explanation1 + explanation2 + explanation3 + explanation4, font=("Arial", 15))
    label_explanation.pack(padx=10, pady=15, side="left")

    frames[0].pack()

    




def generate_first_output(df_art, df_artist, country, first_category, options_category, frames):
    '''
    Function:
        generate_first_output -- Generates a chart based on the user's selected country and category.

    Paramters:
        df_art -- a pandas dataframe, containing information about artworks
        df_artist -- a pandas dataframe, containing information about artists
        frames -- a list of ttk.Frame objects, representing the child frames of the root window. The first frame in the list is the "start_page".
        country -- a string, the country selected by the user 
        first_category -- a string, the category selected by the user for the first time
        options_category -- a list of available categories
    Returns:
        nothing
    Error handling:
        raise TypeError if df_art is not a pandas dataframe
        raise TypeError if df_artist is not a pandas dataframe
        raise TypeError if country is not a str
        raise TypeError if first_category is not a str
        raise TypeError if options_category is not a list
        raise TypeError if frames is not a list
    '''

    if not isinstance(df_art, pd.DataFrame):
        raise TypeError(f"{df_art} should be a pandas dataframe")
    if not isinstance(df_artist, pd.DataFrame):
        raise TypeError(f"{df_artist} should be a pandas dataframe")
    if not isinstance(country, str):
        raise TypeError(f"{country} should be a str")
    if not isinstance(first_category, str):
        raise TypeError(f"{first_category} should be a str")
    if not isinstance(options_category, list):
        raise TypeError(f"{options_category} should be a list")
    if not isinstance(frames, list):
        raise TypeError(f"{frames} should be a list of ttk.Frame objects")

    print("first output category:", first_category)

    # get the data for the selected country
    list_of_artist_objects, list_of_artwork_objects = read_data_into_objects_by_country(df_art, df_artist, country)
    

    # classify artworks by category and save data in a dict
    # This dict is used for drawing charts
    dict_of_artworks = classify_artworks_by_criterion(list_of_artwork_objects, first_category)
    

    # output the result
    # print("The results of this user selection is:\n", dict_of_artworks, "\n")
    
    # display the chart
    if first_category == "year":
        display_bar_chart_on_page_one(dict_of_artworks, list_of_artwork_objects, country, first_category, options_category, frames)
    else:
        display_pie_chart_on_page_one(dict_of_artworks, list_of_artwork_objects, country, first_category, options_category, frames)





def display_bar_chart_on_page_one(dict_of_artworks, list_of_artwork_objects, country, first_category, options_category, frames):
    '''
    Function:
        display_bar_chart_on_page_one -- Displays a bar chart on the first page of the GUI based on the user's initial selection
    
    Parameters:
        dict_of_artworks -- a dictionary, containing the count of artworks from the selected country grouped by the first category selected by the user.
        list_of_artwork_objects -- a list of Artwork objects
        country -- a string, representing the selected country.
        first_category -- a string representing the first selected category.
        options_category -- a list of strings, representing the possible categories
        frames -- a list of ttk.Frame objects, representing the child frames of the root window
    
    Returns:
        nothing
    
    Error handling:
        raise TypeError if dict_of_artworks is not a dict
        raise TypeError if list_of_artwork_objects is not a list
        raise TypeError if country is not a str
        raise TypeError if first_category is not a str
        raise TypeError if options_category is not a list
        raise TypeError if frames is not a list

    '''

    if not isinstance(dict_of_artworks, dict):
        raise TypeError(f"{dict_of_artworks} should be a dict")
    if not isinstance(list_of_artwork_objects, list):
        raise TypeError(f"{list_of_artwork_objects} should be a list")
    if not isinstance(country, str):
        raise TypeError(f"{country} should be a str")
    if not isinstance(first_category, str):
        raise TypeError(f"{first_category} should be a str")
    if not isinstance(options_category, list):
        raise TypeError(f"{options_category} should be a list")
    if not isinstance(frames, list):
        raise TypeError(f"{frames} should be a list of ttk.Frame objects")
    

    # test
    print("on Page One the dict used to draw chart is: ", dict_of_artworks, "\n")

    # clear the previous widgets on the page one
    for widget in frames[1].winfo_children():
        widget.destroy()


    # The following widgets are ordered in such a way that they appear to be the opposite of logical, 
    # because I'm trying to keep the image from overwriting the widgets

    # set the title of page one
    title_of_page_one = ttk.Label(frames[1], text="Page One: Preliminary Analysis", font = ("Arial", 24, "bold"), foreground = "#146C94")
    title_of_page_one.pack()

    # set a back button
    button_of_return_start_page = ttk.Button(frames[1], text="Back to start page", command=lambda: (frames[0].pack(), frames[1].pack_forget()))
    button_of_return_start_page.pack(padx=10, pady=10, side="bottom")

    # create a button widget for executing the second operation and add it to the user interface
    button_of_second_execution = ttk.Button(frames[1], text="Show chart", command=lambda: generate_second_output(list_of_artwork_objects, first_category, second_specific_value.get(), second_category_choice.get(), frames))
    button_of_second_execution.pack(padx=10, pady=10, side="bottom")
    
    # the keys of the dictionary (generated after the first user selection) form the list for the second selection
    second_option_list = list(dict_of_artworks.keys())
    
    # select a classification criterion for the second time
    second_category_choice = ttk.Combobox(frames[1], values=options_category, state="readonly")
    second_category_choice.pack(padx=10, pady=5, side="bottom")

    # create a label prompting the user to select a new category for the second time
    prompt_second_category = ttk.Label(frames[1], text=f"Select a new category:", font=("Arial", 15, "bold"))
    prompt_second_category.pack(side="bottom") 

    # select a specific value from the second_option_list
    second_specific_value = ttk.Combobox(frames[1], values=second_option_list, state="readonly")
    second_specific_value.pack(padx=10, pady=5, side="bottom")

    # create a label prompting the user to select the specific value of the selected category
    prompt_specific_value = ttk.Label(frames[1], text=f"Select a specific {first_category}:", font=("Arial", 15, "bold"))
    prompt_specific_value.pack(side="bottom")
    
    # prompt the user to reselect
    prompt_of_info = ttk.Label(frames[1], text="If you want to see more specific information, please select again:\n", font = ("Arial", 16))
    prompt_of_info.pack(side="bottom")

    # create the canvas for the chart
    fig, ax = plt.subplots(figsize=(12, 8))
    sorted_items = sorted(dict_of_artworks.items())
    x_values, y_values = zip(*sorted_items)

    # draw the chart
    ax.bar(x_values, y_values)
    ax.set_xlabel("Year")
    ax.set_ylabel("Artwork Count")
    ax.set_title(f"Artwork of Artist from {country} Counts by {first_category.capitalize()}")

    max_value = max(y_values)
    ax.set_yticks(range(0, max_value + 1, 1))

    # create a new canvas on page one and embed a Matplotlib Figure object (fig) inside it. 
    # then the chart can be displayed in the graphical user interface (GUI) of the program
    canvas = FigureCanvasTkAgg(fig, master = frames[1])
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, frames[1])
    toolbar.update()

    # Create a label with the canvas and toolbar
    canvas.get_tk_widget().pack()
    toolbar.pack()

    frames[0].pack_forget()
    frames[1].pack()




def display_pie_chart_on_page_one(dict_of_artworks, list_of_artwork_objects, country, first_category, options_category, frames):
    '''
    Function:
        display_bar_chart_on_page_one -- Displays a pie chart on the first page of the GUI based on the user's initial selection
    
    Parameters:
        dict_of_artworks -- a dictionary, containing the count of artworks from the selected country grouped by the first category selected by the user.
        list_of_artwork_objects -- a list of Artwork objects
        country -- a string, representing the selected country.
        first_category -- a string representing the first selected category.
        options_category -- a list of strings, representing the possible categories
        frames -- a list of ttk.Frame objects, representing the child frames of the root window
    
    Returns:
        nothing

    Error handling:
        raise TypeError if dict_of_artworks is not a dict
        raise TypeError if list_of_artwork_objects is not a list
        raise TypeError if country is not a str
        raise TypeError if first_category is not a str
        raise TypeError if options_category is not a list
        raise TypeError if frames is not a list
    '''

    if not isinstance(dict_of_artworks, dict):
        raise TypeError(f"{dict_of_artworks} should be a dict")
    if not isinstance(list_of_artwork_objects, list):
        raise TypeError(f"{list_of_artwork_objects} should be a list")
    if not isinstance(country, str):
        raise TypeError(f"{country} should be a str")
    if not isinstance(first_category, str):
        raise TypeError(f"{first_category} should be a str")
    if not isinstance(options_category, list):
        raise TypeError(f"{options_category} should be a list")
    if not isinstance(frames, list):
        raise TypeError(f"{frames} should be a list of ttk.Frame objects")

    # test
    print("on Page One the dict (used to draw chart) is: ", dict_of_artworks, "\n")

    # clear the previous widgets on the page one
    for widget in frames[1].winfo_children():
        widget.destroy()

    # set the title of page one
    title_of_page_one = ttk.Label(frames[1], text="Page One: Preliminary Analysis", font = ("Arial", 24, "bold"), foreground = "#146C94")
    title_of_page_one.pack()

    # set a Return button
    button_of_return_start_page = ttk.Button(frames[1], text="Back to start page", command=lambda: (frames[0].pack(), frames[1].pack_forget()))
    button_of_return_start_page.pack(padx=10, pady=10, side="bottom")

    # set the button of executing the second operation
    button_of_second_execution = ttk.Button(frames[1], text="Show chart", command=lambda: generate_second_output(list_of_artwork_objects, first_category, second_specific_value.get(), second_category_choice.get(), frames))
    button_of_second_execution.pack(padx=10, pady=10, side="bottom")
    

    # the keys of the dictionary (generated after the first user selection) form the list for the second selection
    second_option_list = list(dict_of_artworks.keys())
    
    # select a classification criterion for the second time
    second_category_choice = ttk.Combobox(frames[1], values=options_category, state="readonly")
    second_category_choice.pack(padx=10, pady=5, side="bottom")

    # create a label prompting the user to select a new category for the second time
    prompt_second_category = ttk.Label(frames[1], text=f"Select a new category:", font=("Arial", 15, "bold"))
    prompt_second_category.pack(side="bottom") 

    
    # select a specific value from the second_option_list
    second_specific_value = ttk.Combobox(frames[1], values=second_option_list, state="readonly")
    second_specific_value.pack(padx=10, pady=5, side="bottom")

    # create a label prompting the user to select the specific value of the selected category
    prompt_specific_value = ttk.Label(frames[1], text=f"Select a specific {first_category}:", font=("Arial", 15, "bold"))
    prompt_specific_value.pack(side="bottom")
    

    # prompt the user to reselect
    prompt_of_info = ttk.Label(frames[1], text="If you want to see more specific information, please select again:\n", font = ("Arial", 16))
    prompt_of_info.pack(side="bottom")

    # the canvas after the first selection
    fig, ax = plt.subplots(figsize=(10, 7))
    autopct_format = "%1.1f%%"
    ax.pie(dict_of_artworks.values(), labels=dict_of_artworks.keys(), autopct=autopct_format, normalize=True)
    ax.set_title(f"Artworks of Artists from {country} by {first_category.capitalize()} ")

    # Create a Matplotlib canvas and toolbar
    canvas = FigureCanvasTkAgg(fig, master=frames[1])
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, frames[1])
    toolbar.update()

    # Create a label with the canvas and toolbar
    canvas.get_tk_widget().pack()
    toolbar.pack()

    frames[0].pack_forget()
    frames[1].pack()
  
         

    
    

def generate_second_output(list_of_artwork_objects, first_category, value, second_category, frames):
    '''
    Function:
        generate_second_output -- classify the resulting objects by a second category criterion, and display a bar chart of the classification results on a second page.
    
    Parameter:
        list_of_artwork_objects -- a list of artwork objects to filter and classify
        first_category -- a string, the category to use for filtering the artwork objects for the first time
        value -- a string, the specific attribute value selected by the user
        second_category -- a string, the category to use for classifying the artwork objects for the second time
        frames -- an integer, the number of frames to display the resulting bar chart on 
    
    Return:
        nothing
    '''

    if not isinstance(list_of_artwork_objects, list):
        raise TypeError(f"{list_of_artwork_objects} should be a list")
    if not isinstance(first_category, str):
        raise TypeError(f"{first_category} should be a str")
    if not isinstance(value, str):
        raise TypeError(f"{value} should be a list")
    if not isinstance(second_category, str):
        raise TypeError(f"{second_category} should be a str")
    if not isinstance(frames, list):
        raise TypeError(f"{frames} should be a list of ttk.Frame objects")


    # filter the list of artwork objects by the specified first category and attribue value chosen from the orginal list_of_artwork_objects
    # then we get the new list of artwork objects according to the second user selection
    new_list_of_artwork_objects = filter_artworks_by_attribute_value(list_of_artwork_objects, first_category, value)

    # get the dictionary by the specified second category
    new_dict_of_artworks = classify_artworks_by_criterion(new_list_of_artwork_objects, second_category)

    # display a bar chart of the classification results on a second page
    display_bar_chart_on_page_two(new_dict_of_artworks, second_category, value, frames)




     
def display_bar_chart_on_page_two(dict_of_artworks, second_category, value, frames):
    '''
    Function:
        display_bar_chart_on_page_two -- display a bar chart of the classification results on the second page
    
    Parameters:
        list_of_artwork_objects -- a list of artwork objects to filter and classify
        second_category -- a string, the category to use for filtering the artwork objects for the second time
        value -- a string, the specific attribute value selected by the user
        frames -- an integer, the number of frames to display the resulting bar chart on 

    Return:
        nothing
    
    Error handling:
        raise TypeError if dict_of_artworks is not a dict
        raise TypeError if second_category is not a str
        raise TypeError if value is not a str
        raise TypeError if frames is not a list
    '''

    if not isinstance(dict_of_artworks, dict):
        raise TypeError(f"{dict_of_artworks} should be a dict")
    if not isinstance(second_category, str):
        raise TypeError(f"{second_category} should be a str")
    if not isinstance(value, str):
        raise TypeError(f"{value} should be a str")
    if not isinstance(frames, list):
        raise TypeError(f"{frames} should be a list")

    # clear the previous widgets on the page one
    for widget in frames[2].winfo_children():
        widget.destroy()

    # print the dictionary used to draw the chart to the console
    print("on Page Two the dict (used to draw chart) is:", dict_of_artworks, "\n")

    # set the title of page two
    title_of_page_two = ttk.Label(frames[2], text="Page Two: Further Analysis", font = ("Arial", 24, "bold"), foreground = "#146C94")
    title_of_page_two.pack()


    # set the back button (back to page one)
    button_of_return_page_one = ttk.Button(frames[2], text="Back to page one", command=lambda: (frames[1].pack(), frames[2].pack_forget()))
    button_of_return_page_one.pack(padx=10, pady=10, side="bottom")

    # Create a Matplotlib figure and axes object
    fig, ax = plt.subplots(figsize=(12, 8))

    # Sort the dictionary items by key and unpack them into x and y values
    sorted_items = sorted(dict_of_artworks.items())
    x_values, y_values = zip(*sorted_items)

    # Plot the bar chart
    ax.bar(x_values, y_values)

    ax.set_xlabel(second_category)
    ax.set_ylabel("Artwork Count")
    ax.set_title(f"Artworks Counts of {value} by {second_category.capitalize()}")

    # set the y axis ticks based on the maximum value in y_values
    max_value = max(y_values)
    ax.set_yticks(range(0, max_value + 1, 1))

    # Create a Matplotlib canvas and toolbar
    canvas = FigureCanvasTkAgg(fig, master = frames[2])
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, frames[2])
    toolbar.update()

    # Create a label with the canvas and toolbar
    canvas.get_tk_widget().pack()
    toolbar.pack()
    
    # Show the second page and hide the first
    frames[1].pack_forget()
    frames[2].pack()

    


