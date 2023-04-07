


import pandas as pd
import matplotlib.pyplot as plt

from get_and_read_art_data import combine_data_of_art_table
from get_and_read_artist_data import combine_data_of_artist_table
from read_data_into_objects import read_data_into_objects





def main():

    # 1.从网站获得两张表的数据，此时是list of lists
    artist_data = combine_data_of_artist_table()
    art_data = combine_data_of_art_table()

    # 2.生成两个 data frame
    df_artist = pd.DataFrame(artist_data, columns=["artist id", "first name", "last name", "country"])
    df_art = pd.DataFrame(art_data, columns = ["work title", "artist id", "type", "status", "material", "year"])
    
    # 2.1 print dataframe的前四列以及info
    # print(df_artist.head(4))
    # print(df_artist.describe())


    # 2.2 print dataframe的前四列以及info
    # print(df_art.head(4))
    # print(df_art.describe())

    # 需要合并df1和df2吗？
    # 为什么我的datatype全是object

    # print(df_artist.info())
    # print(df_art.info())

    
    
    # 3.read data into objects
    # list_of_artist_objects里面既有艺术家本身的属性，也有艺术品以及艺术品这个class的属性
    list_of_artist_objects = read_data_into_objects(artist_data, art_data)

    
    # 4.开始与用户交互

    # 用户选择国家(Canada, USA, China, Germany, Italy, Japan)
   
    # 4.1 展示可选项，也就是所有国籍
    # display_menu()

    # 4.2 用户输入某个国籍
    # user_input = input("Which country's artists are you most interested in?")

    # 假设
    user_input = "USA"

    # 4.3 根据用户的输入进行 filtering
    # Filter out the artworks that belong to the country entered by the user
    # 这个国籍的艺术家的所有艺术品
    country_artworks = []

    for artist in list_of_artist_objects:
        if artist.country == user_input:
            # 这里extend与append的区别是？
            country_artworks.extend(artist.artworks)

    # print(country_artworks)
    # print(len(country_artworks))


    # 4.3.1 艺术品的种类
    # Create two lists for the types and corresponding counts of artwork

    type_counts = {}

    # artwork是一个object 遍历country_artworks里面的所有object
    for artwork in country_artworks:
        artwork_type = artwork.type
        if artwork_type in type_counts:
            type_counts[artwork_type] += 1
        else:
            type_counts[artwork_type] = 1

    types = []
    counts = []
    for key, value in type_counts.items():
        types.append(key)
        counts.append(value)

    print(types)
    print(counts)

    # 饼图(type)、折线图(year)

    # Create and show the bar chart
    fig, ax = plt.subplots()
    ax.bar(types, counts)
    ax.set_xlabel('Type of Artwork')
    ax.set_ylabel('Number of Artworks')
    ax.set_title('Artworks in ' + f'{user_input}')
    plt.show()




if __name__ == "__main__":
    main()