
import tkinter as tk
from tkinter import ttk


import pandas as pd
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


def create_the_top_level_window():

    # create the top-level window
    root = tk.Tk()

    # set the window title
    root.title("Artwork Viewer")

    # set the window size
    root.geometry("980x700")

    # start_page = ttk.Frame(root)
    # page_one = ttk.Frame(root)
    # page_two = ttk.Frame(root)

    # create child frames and store them in a list
    frames = []
    frames.append(ttk.Frame(root))  # add start_page to index 0
    frames.append(ttk.Frame(root))  # add page_one to index 1
    frames.append(ttk.Frame(root))  # add page_two to index 2

    # show the start page initially
    frames[0].pack()

    return frames



 



def create_start_page(df_art, df_artist):
    

    # If you are using pack() to organize widgets on page_two,
    # you do not need to call page_two.pack() to arrange the widgets on a pack.

    # start_page.pack(row=0, column=0, sticky="nsew")
    # page_one.pack(row=0, column=0, sticky="nsew")
    # page_two.pack(row=0, column=0, sticky="nsew")

    s = ttk.Style()
    s.configure('TButton', foreground='blue')

    title_of_start_page = ttk.Label(start_page, text="Start Page")
    title_of_start_page.pack(padx=10, pady=10)
    title_font = ("Arial", 20, "bold")
    title_of_start_page.config(font=title_font)

    # widgets on the start page
    explanation_on_start_page = "\nSelect the country you are interested in \n\nYou will see the distribution of all artworks created by artists from that country by type, status, material, neighbourhood, and year\n"
    label_explanation = ttk.Label(start_page, text = explanation_on_start_page)
    label_explanation.pack()

    label_country = ttk.Label(start_page, text="Select a country:")
    label_country.pack(padx=10, pady=10)

    options_country = df_artist["country"].unique()
    options_country = [option.replace("[", "").replace("]", "") for option in options_country]

    combo_country = ttk.Combobox(start_page, values=options_country, state="readonly")
    combo_country.pack(padx=10, pady=5)

    label_category = ttk.Label(start_page, text="Select a category:")
    label_category.pack(padx=10, pady=10)

    # get coloums's names except for the first two items
    options_category = df_art.columns.tolist()
    options_category = options_category[2:]

    combo_category = ttk.Combobox(start_page, values=options_category, state="readonly")
    combo_category.pack(padx=10, pady=5)


    button = ttk.Button(start_page, text="Show chart", command=lambda: generate_first_output(df_art, df_artist, combo_country.get(), combo_category.get(), options_category))
    button.pack(padx=10, pady=10)

    start_page.pack()

    root.mainloop()




def generate_first_output(df_art, df_artist, country, category, options_category):

    '''
    controller?
    
    '''

    print("first output category:", category)
    # get the data for the selected country
    list_of_artist_objects, list_of_artwork_objects = read_data_into_objects_by_country(df_art, df_artist, country)
    

    # classify artworks by category/criterion and get a dict
    # This dict is used for drawing charts
    dict_of_artworks = classify_artworks_by_criterion(list_of_artwork_objects, category)
    

    # output the result, save the result in a dict
    # print("The results of this user selection is:\n", dict_of_artworks, "\n")
    
    # display the chart
    
    if category == "year":

        display_bar_chart_on_page_one(dict_of_artworks, list_of_artwork_objects, country, category, options_category)

    else:
        display_pie_chart_on_page_one(dict_of_artworks, list_of_artwork_objects, country, category, options_category)








def display_bar_chart_on_page_one(dict_of_artworks, list_of_artwork_objects, country, first_category, options_category):

    # test
    print("on Page One the dict used to draw chart is: ", dict_of_artworks, "\n")

    for widget in page_one.winfo_children():
        widget.destroy()

    # set the title of page one
    title_of_page_one = ttk.Label(page_one, text="Page One: Preliminary Analysis")
    title_of_page_one.pack()
    title_font = ("Arial", 20, "bold")
    title_of_page_one.config(font=title_font)

    # set a Return button
    button_of_return_start_page = ttk.Button(page_one, text="Back to start page", command=lambda: (start_page.pack(), page_one.pack_forget()))
    button_of_return_start_page.pack(padx=10, pady=10, side="bottom")

    # set the button of executing the second operation
    button_of_second_execution = ttk.Button(page_one, text="Show chart", command=lambda: generate_second_output(list_of_artwork_objects, country, first_category, second_specific_value.get(), second_category_choice.get()))
    button_of_second_execution.pack(padx=10, pady=10, side="bottom")
    
    # the keys of the dictionary (generated after the first user selection) form the list for the second selection
    second_option_list = list(dict_of_artworks.keys())
    
    # select a classification criterion for the second time
    second_category_choice = ttk.Combobox(page_one, values=options_category, state="readonly")
    second_category_choice.pack(padx=10, pady=5, side="bottom")

    
    prompt_second_category = ttk.Label(page_one, text=f"Select a new category:")
    prompt_second_category.pack(side="bottom") 

    
    # select a specific value from the second_option_list
    second_specific_value = ttk.Combobox(page_one, values=second_option_list, state="readonly")
    second_specific_value.pack(padx=10, pady=5, side="bottom")

    prompt_specific_value = ttk.Label(page_one, text=f"Select a specific {first_category}:")
    prompt_specific_value.pack(side="bottom")
    
    # prompt the user to reselect
    prompt_of_info = ttk.Label(page_one, text="If you want to see more specific information, please select again:\n")
    prompt_of_info.pack(side="bottom")
    title_font = ("Arial", 16, "bold")
    prompt_of_info.config(font=title_font)

    # the canvas after the first selection
    fig, ax = plt.subplots(figsize=(12, 8))
    sorted_items = sorted(dict_of_artworks.items())
    x_values, y_values = zip(*sorted_items)

    ax.bar(x_values, y_values)
    ax.set_xlabel("Year")
    ax.set_ylabel("Artwork Count")
    ax.set_title(f"Artwork of Artist from {country} Counts by {first_category.capitalize()}")

    max_value = max(y_values)
    ax.set_yticks(range(0, max_value + 1, 1))

    # Create a Matplotlib canvas and toolbar
    canvas = FigureCanvasTkAgg(fig, master = page_one)
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, page_one)
    toolbar.update()

    # Create a label with the canvas and toolbar
    canvas.get_tk_widget().pack()
    toolbar.pack()

    start_page.pack_forget()
    page_one.pack()




def display_pie_chart_on_page_one(dict_of_artworks, list_of_artwork_objects, country, first_category, options_category):

    # test
    print("on Page One the dict (used to draw chart) is: ", dict_of_artworks, "\n")

    for widget in page_one.winfo_children():
        widget.destroy()

    # set the title of page one
    title_of_page_one = ttk.Label(page_one, text="Page One: Preliminary Analysis")
    title_of_page_one.pack()
    title_font = ("Arial", 20, "bold")
    title_of_page_one.config(font=title_font)

    # set a Return button
    button_of_return_start_page = ttk.Button(page_one, text="Back to start page", command=lambda: (start_page.pack(), page_one.pack_forget()))
    button_of_return_start_page.pack(padx=10, pady=10, side="bottom")

    # set the button of executing the second operation
    button_of_second_execution = ttk.Button(page_one, text="Show chart", command=lambda: generate_second_output(list_of_artwork_objects, country, first_category, second_specific_value.get(), second_category_choice.get()))
    button_of_second_execution.pack(padx=10, pady=10, side="bottom")
    

    # the keys of the dictionary (generated after the first user selection) form the list for the second selection
    second_option_list = list(dict_of_artworks.keys())
    
    # select a classification criterion for the second time
    second_category_choice = ttk.Combobox(page_one, values=options_category, state="readonly")
    second_category_choice.pack(padx=10, pady=5, side="bottom")

    
    prompt_second_category = ttk.Label(page_one, text=f"Select a new category:")
    prompt_second_category.pack(side="bottom") 

    
    # select a specific value from the second_option_list
    second_specific_value = ttk.Combobox(page_one, values=second_option_list, state="readonly")
    second_specific_value.pack(padx=10, pady=5, side="bottom")

    prompt_specific_value = ttk.Label(page_one, text=f"Select a specific {first_category}:")
    prompt_specific_value.pack(side="bottom")
    

    # prompt the user to reselect
    prompt_of_info = ttk.Label(page_one, text="If you want to see more specific information, please select again:\n")
    prompt_of_info.pack(side="bottom")
    title_font = ("Arial", 16, "bold")
    prompt_of_info.config(font=title_font)

    # the canvas after the first selection
    fig, ax = plt.subplots(figsize=(10, 7))
    autopct_format = "%1.1f%%"
    ax.pie(dict_of_artworks.values(), labels=dict_of_artworks.keys(), autopct=autopct_format, normalize=True)
    ax.set_title(f"Artworks of Artists from {country} by {first_category.capitalize()} ")

    # Create a Matplotlib canvas and toolbar
    canvas = FigureCanvasTkAgg(fig, master=page_one)
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, page_one)
    toolbar.update()

    # Create a label with the canvas and toolbar
    canvas.get_tk_widget().pack()
    toolbar.pack()


    start_page.pack_forget()
    page_one.pack()
  
         

    
    

def generate_second_output(list_of_artwork_objects, country, first_category, value, second_category):


    for widget in page_two.winfo_children():
        widget.destroy()

    new_list_of_artwork_objects = filter_artworks_by_attribute_value(list_of_artwork_objects, first_category, value)


    new_dict_of_artworks = classify_artworks_by_criterion(new_list_of_artwork_objects, second_category)

    display_bar_chart_on_page_two(new_dict_of_artworks, country, second_category)




     
def display_bar_chart_on_page_two(dict_of_artworks, country, category):

    print("on page two the dict (used to draw chart) is:", dict_of_artworks, "\n")

    # set the title of page two
    title_of_page_two = ttk.Label(page_two, text="Page Two: Further Analysis")
    title_of_page_two.pack()
    title_font = ("Arial", 20, "bold")
    title_of_page_two.config(font=title_font)

    # set the back button (back to page one)
    button_of_return_page_one = ttk.Button(page_two, text="Back to page one", command=lambda: (page_one.pack(), page_two.pack_forget()))
    button_of_return_page_one.pack(padx=10, pady=10, side="bottom")

    # 背景图
    fig, ax = plt.subplots(figsize=(12, 8))

    sorted_items = sorted(dict_of_artworks.items())
    x_values, y_values = zip(*sorted_items)
    ax.bar(x_values, y_values)

    ax.set_xlabel(category)
    ax.set_ylabel("Artwork Count")
    ax.set_title(f"Artwork of Artist from {country} Counts by {category.capitalize()}")
    max_value = max(y_values)
    ax.set_yticks(range(0, max_value + 1, 1))

    # Create a Matplotlib canvas and toolbar
    canvas = FigureCanvasTkAgg(fig, master=page_two)
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, page_two)
    toolbar.update()

    # Create a label with the canvas and toolbar
    canvas.get_tk_widget().pack()
    toolbar.pack()
    

    page_one.pack_forget()
    page_two.pack()

    


