'''
CS5001
Final Project
Spring 2023
MyName: Zhixiao Wang

This is a file for user interaction using Tkinter.

There are three pages: 
    Start Page: frames[0]
    Page One: frames[1]
    Page Two: frames[2]

There are two functions responsible for processing data and calling display functions:
    generate_first_output():
        input: country, first_category 
        output: pie/bar chart
    generate_second_output():
        input: value of first_category, second_category 
        output: pie chart

There are four functions used to display widgets on specific pages/frames
    create_start_page():
        buttons to execute generate_first_output 
    display_bar_chart_on_page_one():
        the bar chart created by the first selection
        buttons to execute generate_second_output
    display_pie_chart_on_page_one():
        the pie chart created by the first selection
        buttons to execute generate_second_output
    display_bar_chart_on_page_two():
        the bar chart created by the second selection
'''



import pandas as pd
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from read_data_into_objects import *
from filter_data import *

START_PAGE_INDEX = 0
PAGE_ONE_INDEX = 1
PAGE_TWO_INDEX = 2

TITLE_FONT = ("Arial", 24, "bold")
PROMPT_FONT = ("Arial", 15, "bold")
COMMENT_FONT = ("Arial", 15)
TITLE_COLOR = "#146C94"
BUTTON_COLOR = "#19A7CE"
BIG_PADDING = 10
SMALL_PADDING = 5
BOTTOM = "bottom"
LEFT = "left"
EMPTY = ""
STATE_OF_DROPDOWN = "readonly"
CHART_SIZE =  (12, 8)
PIE_CHART_FORMAT = "%1.1f%%"
Y_START = 0
Y_SMALL_STEP = 1
Y_BIG_STEP = 5
ONE_STEP = 1
THRESHOLD = 15



def set_root_and_create_child_frames(root):
    '''
    Function:
        create_child_frames -- Create child frames for the given root window.
    Parameters:
        root -- an object, the root window object
    Returns:
        frames -- a list of ttk.Frame objects representing the child frames. The first frame in the list is the "start_page", the second is "page_one", and the third is "page_two".
    '''

    # set the window title
    root.title("Artwork Viewer")

    # set the window size
    root.geometry("1100x800")

    # set the style of all buttons
    style = ttk.Style()
    style.configure("TButton", foreground = BUTTON_COLOR)

    # start_page, page_one, and page_two are created as child frames of the root window.
    # create three child frames and store them in a list
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
    
    Return:
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


    title_of_start_page = ttk.Label(frames[START_PAGE_INDEX], text = "Start Page", font = TITLE_FONT, foreground = TITLE_COLOR)
    title_of_start_page.pack(padx = BIG_PADDING, pady = BIG_PADDING)

    # widgets on the start page
    text_one = "\nHi, welcome to Artwork Viewer! "
    text_two = "Please select the country you are interested in and explore a variety of artworks.\n"
    text_three = "\nClicking the button, you will see the distribution of all artworks created by artists from that country by type, status, material, neighbourhood, and year。\n"
    label_explanation = ttk.Label(frames[START_PAGE_INDEX], text = text_one + text_two + text_three, font = COMMENT_FONT)
    label_explanation.pack(padx = BIG_PADDING, pady = BIG_PADDING)

    
    label_country = ttk.Label(frames[START_PAGE_INDEX], text = "Select a country:", font = PROMPT_FONT)
    label_country.pack(padx = BIG_PADDING, pady = BIG_PADDING)
 
    options_country = df_artist["country"].unique()
    options_country = [option.replace("[", "").replace("]", "") for option in options_country]

    combo_country = ttk.Combobox(frames[START_PAGE_INDEX], values = options_country, state = STATE_OF_DROPDOWN)
    combo_country.pack(padx = BIG_PADDING, pady = BIG_PADDING)

    label_category = ttk.Label(frames[START_PAGE_INDEX], text = "Select a category:", font = PROMPT_FONT)
    label_category.pack(padx = BIG_PADDING, pady = BIG_PADDING)

    # get coloums's names except for the first two items
    options_category = df_art.columns.tolist()
    options_category = options_category[2:]

    combo_category = ttk.Combobox(frames[START_PAGE_INDEX], values = options_category, state = STATE_OF_DROPDOWN)
    combo_category.pack(padx = BIG_PADDING, pady = BIG_PADDING)

    
    button = ttk.Button(frames[START_PAGE_INDEX], text="Show chart", command = lambda: generate_first_output(df_art, df_artist, combo_country.get(), combo_category.get(), options_category, frames))
    button.pack(padx = BIG_PADDING, pady = BIG_PADDING)

    explanation1 = "\nNote:\n\n[country]: the nationality of the artist of the artworks.\n"
    explanation2 = "\n[category]: You can check the distribution of artworks according to many different categories.\n"
    explanation3 = "\n[type]: the type of the artwork, such as sculpture, mural, and so on.\n\n[status]: the status of the artwork, in palce, no longer in place or deaccessioned.\n"
    explanation4 = "\n[material]: the material of the artwork.\n\n[neighbourhood]: the location of the artwork.\n\n[year]: the year in which the artwork was created.\n"
    explanation5 = "\nSome categories contain many words, which can cause them to appear crowded on the image. \n\nTo view all the words clearly, please use the magnifying glass icon in the toolbar to zoom in on specific areas."
    label_explanation = ttk.Label(frames[START_PAGE_INDEX], text = explanation1 + explanation2 + explanation3 + explanation4 + explanation5, font = COMMENT_FONT)
    label_explanation.pack(padx = BIG_PADDING, pady = BIG_PADDING, side = LEFT)

    frames[START_PAGE_INDEX].pack()

    


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
    
    Return:
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

    
    if country == EMPTY or first_category == EMPTY:
        messagebox.showerror("Error", "Please select both a country and a category.")
        return
    
    # The return statement is used to immediately exit the function and prevent any further code from executing if either of the variables is empty. 
    # if the user did not select a country or a category, the function cannot proceed to the next steps as it needs these values to fetch the data.

    # get the data for the selected country
    list_of_artist_objects, list_of_artwork_objects = read_data_into_objects_by_country(df_art, df_artist, country)
    
    # classify artworks by category and save data in a dict
    # This dict is used for drawing charts
    dict_of_artworks = classify_artworks_by_criterion(list_of_artwork_objects, first_category)
    
    
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
    

    # track the generated dict
    print("on Page One, the dict used to draw chart is: ", dict_of_artworks, "\n")

    # clear the previous widgets on the page one
    for widget in frames[PAGE_ONE_INDEX].winfo_children():
        widget.destroy()

    # The following widgets are ordered in such a way that they appear to be the opposite of logical, 
    # because I'm trying to keep the image from overwriting the widgets

    # set the title of page one
    title_of_page_one = ttk.Label(frames[PAGE_ONE_INDEX], text = "Page One: Preliminary Analysis", font = TITLE_FONT, foreground = TITLE_COLOR)
    title_of_page_one.pack()

    # set a back button
    button_of_return_start_page = ttk.Button(frames[PAGE_ONE_INDEX], text = "Back to start page", command = lambda: (frames[START_PAGE_INDEX].pack(), frames[PAGE_ONE_INDEX].pack_forget()))
    button_of_return_start_page.pack(padx = BIG_PADDING, pady = BIG_PADDING, side = BOTTOM)

    # create a button widget for executing the second operation and add it to the user interface
    button_of_second_execution = ttk.Button(frames[PAGE_ONE_INDEX], text = "Show chart", command = lambda: generate_second_output(list_of_artwork_objects, first_category, second_specific_value.get(), second_category_choice.get(), frames))
    button_of_second_execution.pack(padx = BIG_PADDING, pady = BIG_PADDING, side = BOTTOM)
    
    # the keys of the dictionary (generated after the first user selection) form the list for the second selection
    second_option_list = list(dict_of_artworks.keys())
    
    # select a classification criterion for the second time
    second_category_choice = ttk.Combobox(frames[PAGE_ONE_INDEX], values=options_category, state = STATE_OF_DROPDOWN)
    second_category_choice.pack(padx = BIG_PADDING, pady = SMALL_PADDING, side = BOTTOM)

    # create a label prompting the user to select a new category for the second time
    prompt_second_category = ttk.Label(frames[PAGE_ONE_INDEX], text = "Select a new category:", font = PROMPT_FONT)
    prompt_second_category.pack(side = BOTTOM) 

    # select a specific value from the second_option_list
    second_specific_value = ttk.Combobox(frames[PAGE_ONE_INDEX], values = second_option_list, state = STATE_OF_DROPDOWN)
    second_specific_value.pack(padx = BIG_PADDING, pady = SMALL_PADDING, side = BOTTOM)

    # create a label prompting the user to select the specific value of the selected category
    prompt_specific_value = ttk.Label(frames[PAGE_ONE_INDEX], text = f"Select a specific {first_category}:", font = PROMPT_FONT)
    prompt_specific_value.pack(side = BOTTOM)
    
    # prompt the user to reselect
    prompt_of_info = ttk.Label(frames[PAGE_ONE_INDEX], text = "If you want to see more specific information, please select again:\n", font = COMMENT_FONT)
    prompt_of_info.pack(side = BOTTOM)

    # create the canvas for the chart
    fig, ax = plt.subplots(figsize = CHART_SIZE)
    sorted_items = sorted(dict_of_artworks.items())
    x_values, y_values = zip(*sorted_items)

    # draw the chart
    ax.bar(x_values, y_values)
    ax.set_xlabel("Year")
    ax.set_ylabel("Artwork Count")
    ax.set_title(f"Artwork of Artist from {country} Counts by {first_category.capitalize()}")

    max_value = max(y_values)

    if max_value < THRESHOLD:
        ax.set_yticks(range(Y_START, max_value + ONE_STEP, Y_SMALL_STEP))
    else:
        ax.set_yticks(range(Y_START, max_value + ONE_STEP, Y_BIG_STEP))
        

    # create a new canvas on page one and embed a Matplotlib Figure object (fig) inside it. 
    # then the chart can be displayed in the graphical user interface (GUI) of the program
    canvas = FigureCanvasTkAgg(fig, master = frames[PAGE_ONE_INDEX])
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, frames[PAGE_ONE_INDEX])
    toolbar.update()

    # Create a label with the canvas and toolbar
    canvas.get_tk_widget().pack()
    toolbar.pack()

    frames[START_PAGE_INDEX].pack_forget()
    frames[PAGE_ONE_INDEX].pack()




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
    print("on Page One, the dict (used to draw chart) is: ", dict_of_artworks, "\n")

    # clear the previous widgets on the page one
    for widget in frames[PAGE_ONE_INDEX].winfo_children():
        widget.destroy()

    # set the title of page one
    title_of_page_one = ttk.Label(frames[PAGE_ONE_INDEX], text = "Page One: Preliminary Analysis", font = TITLE_FONT, foreground = TITLE_COLOR)
    title_of_page_one.pack()

    # set a Return button
    button_of_return_start_page = ttk.Button(frames[PAGE_ONE_INDEX], text = "Back to start page", command = lambda: (frames[START_PAGE_INDEX].pack(), frames[PAGE_ONE_INDEX].pack_forget()))
    button_of_return_start_page.pack(padx = BIG_PADDING, pady = BIG_PADDING, side = BOTTOM)

    # set the button of executing the second operation
    button_of_second_execution = ttk.Button(frames[PAGE_ONE_INDEX], text = "Show chart", command = lambda: generate_second_output(list_of_artwork_objects, first_category, second_specific_value.get(), second_category_choice.get(), frames))
    button_of_second_execution.pack(padx = BIG_PADDING, pady = BIG_PADDING, side = BOTTOM)
    

    # the keys of the dictionary (generated after the first user selection) form the list for the second selection
    second_option_list = list(dict_of_artworks.keys())
    second_option_list = sorted(second_option_list)
    
    # select a classification criterion for the second time
    second_category_choice = ttk.Combobox(frames[PAGE_ONE_INDEX], values = options_category, state = STATE_OF_DROPDOWN)
    second_category_choice.pack(padx = BIG_PADDING, pady = SMALL_PADDING, side = BOTTOM)

    # create a label prompting the user to select a new category for the second time
    prompt_second_category = ttk.Label(frames[PAGE_ONE_INDEX], text = f"Select a new category:", font = PROMPT_FONT)
    prompt_second_category.pack(side = BOTTOM) 

    
    # select a specific value from the second_option_list
    second_specific_value = ttk.Combobox(frames[PAGE_ONE_INDEX], values = second_option_list, state = STATE_OF_DROPDOWN)
    second_specific_value.pack(padx = BIG_PADDING, pady = SMALL_PADDING, side = BOTTOM)

    # create a label prompting the user to select the specific value of the selected category
    prompt_specific_value = ttk.Label(frames[PAGE_ONE_INDEX], text = f"Select a specific {first_category}:", font = PROMPT_FONT)
    prompt_specific_value.pack(side = BOTTOM)
    

    # prompt the user to reselect
    prompt_of_info = ttk.Label(frames[PAGE_ONE_INDEX], text = "If you want to see more specific information, please select again:\n", font = COMMENT_FONT)
    prompt_of_info.pack(side = BOTTOM)

    # the canvas after the first selection
    fig, ax = plt.subplots(figsize = CHART_SIZE)

    # format the text to show the percentage with one decimal place, followed by a percent sign.
    autopct_format = PIE_CHART_FORMAT

    # The autopct parameter is used to format the text that is displayed inside each slice of the pie chart, to show the percentage or fraction of the total that each slice represents. 
    ax.pie(dict_of_artworks.values(), labels = dict_of_artworks.keys(), autopct = autopct_format, normalize = True)
    ax.set_title(f"Artworks of Artists from {country} by {first_category.capitalize()} ")

    # Create a Matplotlib canvas and toolbar
    canvas = FigureCanvasTkAgg(fig, master = frames[PAGE_ONE_INDEX])
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, frames[PAGE_ONE_INDEX])
    toolbar.update()

    # Create a label with the canvas and toolbar
    canvas.get_tk_widget().pack()
    toolbar.pack()

    frames[START_PAGE_INDEX].pack_forget()
    frames[PAGE_ONE_INDEX].pack()
  
         

    
    

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
    
    if value == EMPTY or second_category == EMPTY:
        messagebox.showerror("Error", f"Please select both a {first_category} and a category.")
        return

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
    for widget in frames[PAGE_TWO_INDEX].winfo_children():
        widget.destroy()

    # print the dictionary used to draw the chart to the console
    print("on Page Two, the dict (used to draw chart) is:", dict_of_artworks, "\n")

    # set the title of page two
    title_of_page_two = ttk.Label(frames[PAGE_TWO_INDEX], text = "Page Two: Further Analysis", font = TITLE_FONT, foreground = TITLE_COLOR)
    title_of_page_two.pack()


    # set the back button (back to page one)
    button_of_return_page_one = ttk.Button(frames[PAGE_TWO_INDEX], text = "Back to page one", command = lambda: (frames[PAGE_ONE_INDEX].pack(), frames[PAGE_TWO_INDEX].pack_forget()))
    button_of_return_page_one.pack(padx = BIG_PADDING, pady = BIG_PADDING, side = BOTTOM)

    explanation = ttk.Label(frames[PAGE_TWO_INDEX], text = "Go back to the previous page:", font = COMMENT_FONT)
    explanation.pack(padx = BIG_PADDING, pady = BIG_PADDING, side = BOTTOM)

    # Create a Matplotlib figure and axes object
    fig, ax = plt.subplots(figsize = CHART_SIZE)

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

    if max_value < THRESHOLD:
        ax.set_yticks(range(Y_START, max_value + ONE_STEP, Y_SMALL_STEP))
    else:
        ax.set_yticks(range(Y_START, max_value + ONE_STEP, Y_BIG_STEP))

    # Create a Matplotlib canvas and toolbar
    canvas = FigureCanvasTkAgg(fig, master = frames[PAGE_TWO_INDEX])
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, frames[PAGE_TWO_INDEX])
    toolbar.update()

    # Create a label with the canvas and toolbar
    canvas.get_tk_widget().pack()
    toolbar.pack()
    
    # Show the second page and hide the first
    frames[PAGE_ONE_INDEX].pack_forget()
    frames[PAGE_TWO_INDEX].pack()

    


