'''
CS5001
Final Project
Spring 2023
MyName: Zhixiao Wang

This is a driver file.

Note:
The user interaction part is not finished yet and will be put in a separate file.
I will add some explanations for "category" later in the canvas.

If you want to test this program, I suggest you choose the USA because the data is moderate and easy to observe

'''

import tkinter as tk
from tkinter import ttk
import pandas as pd


from get_and_clean_art_data import *
from get_and_clean_artist_data import *
from filter_data_and_draw_charts import *


PADX_VALUE = 10
PADY_VALUE = 5

def main():

    try:

        # 1. Extract and clean the data we need from the website
        # finally we get two lists of lists, art_data and artist_data
        content_of_arts = get_art_csv_file()
        work_title = get_work_title_from_art_table(content_of_arts)
        type, status, material, neighbourhood = get_other_info_from_art_table(content_of_arts)
        artist_id, year = get_artist_id_and_year_from_art_table(content_of_arts)
        art_data = get_public_art_data(work_title, type, status, material, neighbourhood, artist_id, year)

        content_of_artists = get_artist_csv_file()
        id, first_name, last_name = get_basic_info_from_artist_table(content_of_artists)
        country = get_country_from_artist_table(content_of_artists)
        artist_data = get_public_arist_data(id, first_name, last_name, country)


        # 2.create two data frames according to these two lists of lists
        # used in user interaction to provide a sequence of options in the user interaction)
        df_artist = pd.DataFrame(artist_data, columns=["artist id", "first name", "last name", "country"])
        df_art = pd.DataFrame(art_data, columns = ["work title", "artist id", "type", "status", "material", "neighbourhood", "year"])

        # test
        # print(df_artist.head(4))
        # print(df_artist.describe())
        # print(df_art.head(4))
        # print(df_art.describe())
        # print(df_artist.info())
        # print(df_art.info())
        
        # class View (GUI class?)
        # put root in driver
        
        # 3. Start interacting with the user
        # user will choose the country of artists and the category of their artworks
        # create the GUI window
        root = tk.Tk()
        # print(tk.TkVersion)

        root.title("Artwork Viewer")
        root.geometry("800x400")
        

        # add some explanation
        explanation = "\nSelect the country you are interested in \n\nYou will see the distribution of all artworks created by artists from that country by type, material, status, and year\n"
        label_explanation = ttk.Label(root, text = explanation)
        label_explanation.pack()

        label_country = ttk.Label(root, text="Select a country:")
        label_country.pack(padx=PADX_VALUE, pady=PADX_VALUE)

        # options_country is a list
        options_country = df_artist["country"].unique()

        # remove special characters from option list
        options_country = [option.replace("[", "").replace("]", "") for option in options_country]

        # state="readonly" is used to prevent the user from manually editing the value of a Tkinter Combobox 
        combo_country = ttk.Combobox(root, values=options_country, state="readonly")
        combo_country.pack(padx=PADX_VALUE, pady=PADY_VALUE)


        label_category = ttk.Label(root, text="Select a category:")
        label_category.pack(padx=PADX_VALUE, pady=PADX_VALUE)

        # get coloums's names except for the first two items
        options_category = df_art.columns.tolist()
        options_category = options_category[2:]

        combo_category = ttk.Combobox(root, values=options_category, state="readonly")
        combo_category.pack(padx=PADX_VALUE, pady=PADY_VALUE)


        # create a button to display the pie chart
        # the model is display_chart_and_output_result()
        button = ttk.Button(root, text="Show chart", command=lambda: display_chart_and_output_result(df_art, df_artist, combo_country.get(), combo_category.get()))
        # use pack method to display it
        button.pack(padx=PADX_VALUE, pady=PADX_VALUE)
        
        # start the GUI event loop
        # the method that runs continuously and listens for events, including mouse clicks
        root.mainloop()

    except NameError as ne:
        print("NameError occurred")
    except TypeError as te:
        print(type(te), te)
    except ValueError as ve:
        print(type(te), te)
    except Exception as e:
        print("Other errors occurred", type(e), e)


if __name__ == "__main__":
    main()