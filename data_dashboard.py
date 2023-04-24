'''
CS5001
Final Project
Spring 2023
MyName: Zhixiao Wang

This is a driver file of a program named Artwork Viewer.

If you want to test this program, I suggest you choose the USA, Germany because the data is moderate and easy to observe.
'''

import pandas as pd
import tkinter as tk

from get_and_clean_art_data import *
from get_and_clean_artist_data import *
from user_interaction import *

ART_URL = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/public-art/exports/csv?lang=en&timezone=America%2FLos_Angeles&use_labels=true&delimiter=%3B"
ARTIST_URL = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/public-art-artists/exports/csv?lang=en&timezone=America%2FLos_Angeles&use_labels=true&delimiter=%3B"

def main():

    try:

        # 1. Extract and clean the data we need from the website
        # finally we get two lists of lists, art_data and artist_data
        content_of_arts = get_art_csv_file(ART_URL)
        work_title = get_work_title_from_art_table(content_of_arts)
        type, status, material, neighbourhood = get_other_info_from_art_table(content_of_arts)
        artist_id, year = get_artist_id_and_year_from_art_table(content_of_arts)
        art_data = get_public_art_data(work_title, type, status, material, neighbourhood, artist_id, year)

        content_of_artists = get_artist_csv_file(ARTIST_URL)
        id, first_name, last_name = get_basic_info_from_artist_table(content_of_artists)
        country = get_country_from_artist_table(content_of_artists)
        artist_data = get_public_arist_data(id, first_name, last_name, country)

        # 2.Create two data frames according to these two lists of lists
        # data frames are used in user interaction to provide a sequence of options
        df_artist = pd.DataFrame(artist_data, columns=["artist id", "first name", "last name", "country"])
        df_art = pd.DataFrame(art_data, columns = ["work title", "artist id", "type", "status", "material", "neighbourhood", "year"])

                
        # 3. Interacting with the user
        # user will choose the country of artists and the category of their artworks
        # create the top-level window
        root = tk.Tk()
        frames = set_root_and_create_child_frames(root)

        # df_art and df_artist are only used to create a option list, not for data analysis
        create_start_page(df_art, df_artist, frames)

        root.mainloop()


    except NameError:
        print("NameError occurred")
    except TypeError as te:
        print(type(te), te)
    except ValueError as ve:
        print(type(ve), ve)
    except AttributeError as ae:
        print(type(ae), ae)
    except Exception as e:
        print("Other errors occurred", type(e), e)


if __name__ == "__main__":
    main()

    