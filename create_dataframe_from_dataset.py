
import pandas as pd

from get_and_read_art_data import combine_data_of_art_table
from get_and_read_artist_data import combine_data_of_artist_table

def create_dataframe():
# 不需要全部列的数据？如果确实值怎么办？输出为空""
    artist_data = combine_data_of_artist_table()
    # print(artist_data)
    art_data = combine_data_of_art_table()
    # print(art_data)

    df_artist = pd.DataFrame(artist_data, columns=["artist id", "first name", "last name", "country"])
    df_art = pd.DataFrame(art_data, columns = ["work title", "artist id", "type", "status", "material", "year"])
    
    return df_artist, df_art

