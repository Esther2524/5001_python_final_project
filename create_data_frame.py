import pandas as pd

from read_and_clean_artist_data import *
from read_and_clean_art_data import *

def get_final_data_of_artist():

    content_of_artist = get_artist_csv_file()
    id, first_name, last_name = get_basic_info_from_artist_table(content_of_artist)
    country = get_country_from_artist_table(content_of_artist)
    final_data_of_artist = combine_data_of_artist_table(id, first_name, last_name, country)

    return final_data_of_artist

def get_final_data_of_art():
    content_of_art = get_art_csv_file()
    artist_id, year = get_artist_id_and_year_from_art_table(content_of_art)
    type, status, material = get_other_info_from_art_table(content_of_art)
    title = get_work_title_from_art_table(content_of_art)
    final_data_of_art = combine_data_of_art_table(title, artist_id, type, status, material, year)
    return final_data_of_art


def convert_data_to_dataframe():
    final_data_of_artist = get_final_data_of_artist()
    final_data_of_art = get_final_data_of_art()

    dataframe_of_artist = pd.DataFrame(final_data_of_artist, columns=["artist id", "first name", "last name", "country"])
    dataframe_of_art = pd.DataFrame(final_data_of_art, columns = ["work title", "artist id", "type", "status", "material", "year"])
    return dataframe_of_artist, dataframe_of_art


def main():
    df1, df2 = convert_data_to_dataframe()
    # print(df1.head(4))
    print(df2.head(4))

if __name__ == "__main__":
    main()

    


