
import tkinter as tk
from tkinter import *
from tkinter import ttk


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


from read_data_into_objects import *
from filter_data import *



# view里面有 input 和 visulization

root = tk.Tk()

# start_page, page_one, and page_two are created as child frames of the root window.
start_page = Frame(root)
page_one = Frame(root)
page_two = Frame(root)

 



def create_start_page(df_art, df_artist):
    # set the window title
    root.title("Artwork Viewer")

    # set the window size
    root.geometry("980x700")

    # If you are using pack() to organize widgets on page_two,
    # you do not need to call page_two.pack() to arrange the widgets on a pack.

    # start_page.pack(row=0, column=0, sticky="nsew")
    # page_one.pack(row=0, column=0, sticky="nsew")
    # page_two.pack(row=0, column=0, sticky="nsew")

    title_of_start_page = Label(start_page, text="Start Page")
    title_of_start_page.grid(row=0, column=0, sticky="nsew")
    title_font = ("Helvetica", 20, "bold")
    title_of_start_page.config(font=title_font)

    # widgets on the start page
    explanation_on_start_page = "\nSelect the country you are interested in \n\nYou will see the distribution of all artworks created by artists from that country by type, status, material, neighbourhood, and year\n"
    label_explanation = ttk.Label(start_page, text = explanation_on_start_page)
    label_explanation.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    label_country = ttk.Label(start_page, text="Select a country:")
    label_country.pack(row=2, column=0, sticky="w", padx=10, pady=10)

    options_country = df_artist["country"].unique()
    options_country = [option.replace("[", "").replace("]", "") for option in options_country]

    combo_country = ttk.Combobox(start_page, values=options_country, state="readonly")
    combo_country.grid(row=2, column=1, sticky="ew", padx=10, pady=5)

    label_category = ttk.Label(start_page, text="Select a category:")
    label_category.grid(row=3, column=0, sticky="w", padx=10, pady=10)

    # get coloums's names except for the first two items
    options_category = df_art.columns.tolist()
    options_category = options_category[2:]

    combo_category = ttk.Combobox(start_page, values=options_category, state="readonly")
    combo_category.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)


    button = ttk.Button(start_page, text="Show chart", command=lambda: generate_first_output(df_art, df_artist, combo_country.get(), combo_category.get(), options_category))
    button.pack(padx=10, pady=10)
    
    # pack the start page
    start_page.grid()

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

    for widget in page_one.winfo_children():
        widget.destroy()

    title_of_page_one = Label(page_one, text="Page One: Preliminary Analysis")
    title_of_page_one.pack()
    title_font = ("Helvetica", 20, "bold")
    title_of_page_one.config(font=title_font)
    
    label = Label(page_one, text="select again:")
    label.pack()

    # 第二次选择的下拉框要放在canvas前面。。。
    keys_list = list(dict_of_artworks.keys())

    # year = 2016
    combo_second_choice = ttk.Combobox(page_one, values=keys_list, state="readonly")
    combo_second_choice.pack(padx=10, pady=5)


    combo_second_category_choice = ttk.Combobox(page_one, values=options_category, state="readonly")
    combo_second_category_choice.pack(padx=10, pady=5)

    
    # 用来执行第二次作图
    button = ttk.Button(page_one, text="Show chart again", command=lambda: generate_second_output(list_of_artwork_objects, country, first_category, combo_second_choice.get(), combo_second_category_choice.get()))
    button.pack(padx=10, pady=10)

    # 返回按钮
    button_of_return_start_page = ttk.Button(page_one, text="Return Start Page", command=lambda: (start_page.pack(), page_one.pack_forget()))
    button_of_return_start_page.pack(padx=10, pady=10)

    print("on page one 画图用的字典是:", dict_of_artworks)

    # 第一次画的图是背景
    # 放最下面
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
    canvas = FigureCanvasTkAgg(fig, master=page_one)
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, page_one)
    toolbar.update()

    # Create a label with the canvas and toolbar
    canvas.get_tk_widget().pack()
    toolbar.pack()

    start_page.pack_forget()
    page_one.pack()




def display_pie_chart_on_page_one(dict_of_artworks, list_of_artwork_objects, country, first_category, options_category):

    for widget in page_one.winfo_children():
        widget.destroy()

    Label_of_page_one = Label(page_one, text="Page One")
    Label_of_page_one.pack()
    
    label = Label(page_one, text="select again:")
    label.pack()

    # 第二次选择的下拉框要放在canvas前面。。。
    keys_list = list(dict_of_artworks.keys())
    # year = 2016
    combo_second_choice = ttk.Combobox(page_one, values=keys_list, state="readonly")
    combo_second_choice.pack(padx=10, pady=5)

    combo_second_category_choice = ttk.Combobox(page_one, values=options_category, state="readonly")
    combo_second_category_choice.pack(padx=10, pady=5)

    

    # 用来执行第二次作图
    button = ttk.Button(page_one, text="Show chart again", command=lambda: generate_second_output(list_of_artwork_objects, country, first_category, combo_second_choice.get(), combo_second_category_choice.get()))
    button.pack(padx=10, pady=10)

    # 返回按钮
    button_of_return_start_page = ttk.Button(page_one, text="Return Start Page", command=lambda: (start_page.pack(), page_one.pack_forget()))
    button_of_return_start_page.pack(padx=10, pady=10)
    
    fig, ax = plt.subplots(figsize=(10, 7))
    autopct_format = "%1.1f%%"
    ax.pie(dict_of_artworks.values(), labels=dict_of_artworks.keys(), autopct=autopct_format, normalize=True)
    ax.set_title(f"Artworks of Artists from {country} by {first_category.capitalize()} ")


    print("on page one 画图用的字典是", dict_of_artworks)

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

    # print("second 里面的内容")
    # print("list objects", list_of_artwork_objects)
    # print("value", value)
    # print("第一次选的category", first_category)
    # print("第二次选的category", second_category)

    for widget in page_two.winfo_children():
        widget.destroy()

    new_list_of_artwork_objects = filter_artworks_by_attribute_value(list_of_artwork_objects, first_category, value)

    # print("new list", new_list_of_artwork_objects)

    new_dict_of_artworks = classify_artworks_by_criterion(new_list_of_artwork_objects, second_category)

    # print("new dict", new_dict_of_artworks)


    display_bar_chart_on_page_two(new_dict_of_artworks, country, second_category)

    



     
def display_bar_chart_on_page_two(dict_of_artworks, country, category):

    print("on page two 画图用的字典是", dict_of_artworks)

    # 标题
    label = Label(page_two, text="Page Two: Further Analysis")
    label.pack()

    # 返回按钮
    button_of_return_page_one = ttk.Button(page_two, text="Return Page One", command=lambda: (page_one.pack(), page_two.pack_forget()))
    button_of_return_page_one.pack(padx=10, pady=10)

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

    


