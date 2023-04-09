


import pandas as pd

from get_and_read_art_data import combine_data_of_art_table
from get_and_read_artist_data import combine_data_of_artist_table

from create_dataframe_from_dataset import create_dataframe
from read_data_into_objects import *
from filter_data_and_draw_charts import *
# from user_interaction import *




def main():

    # 1.从网站获得两张表的数据，此时是list of lists
    # 不需要全部列的数据？如果确实值怎么办？输出为空""
    

    # 2.生成两个 data frame
    df_artist, df_art = create_dataframe()

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


    # 3.开始与用户交互

    # 用户选择国家(Canada, USA, China, Germany, Italy, Japan)
   
    # 3.1 展示可选项，也就是所有国籍
    # display_menu()

    # 3.2 用户输入某个国籍
    # user_input_country = input("Which country's artists are you most interested in?")
    # 做成一个下拉
    
    # 假设
    user_input_country = "USA"

    
    
    # 4. 根据用户输入建立对应country的list_of_objects
    # read specified data into objects

    # list_of_artist_objects里面既有艺术家本身的属性，也有艺术品以及艺术品这个class的属性
    list_of_artist_objects, list_of_artwork_objects = read_data_into_objects_by_country(user_input_country)
    
    # print(list_of_artwork_objects)
    # print(len(list_of_artwork_objects))

    # 测试id
    # for artist in list_of_artist_objects:
    #     if artist.id == "555":
    #         print(artist.artworks)
    #         for artwork in artist.artworks:
    #             print(artwork.title)
    # print(len(list_of_artwork_objects))

 
    # test method
    # 通过id获得一个艺术家的作品
    # for artist in list_of_artist_objects:
    #     if artist.id == "555":
    #         print(artist.artworks)
    #         print(artist.classify_artworks_by_criterion("type"))
    #         print(artist.classify_artworks_by_criterion("year"))
    #         print(artist.classify_artworks_by_criterion("status"))
    #         print(artist.classify_artworks_by_criterion("material"))



    # 4.3 再次与用户交互，也就是细分objects of artworks
    # 给予选择 type, year, material

    user_option = "year"
   
    # 4.3.1 根据种类来分类 (pie chart)
    # Create two lists for the types and corresponding counts of artwork
    # types, counts = categorize_artworks_by_type(list_of_artist_objects)
    # draw_pie_chart_by_country(list_of_artist_objects)



    # 4.4.1.2 种类里面的年份

    # 4.4.2 根据年份来分类 (line chart)
    # year, counts = classify_artworks_by_criterion(list_of_artist_objects, user_option)
    # draw_line_chart(year, counts, user_input_country)




    # 4.4.3 根据year来分类 (pie chart)
    artworks_by_criterion = classify_artworks_by_criterion(list_of_artwork_objects, user_option)
    
    # print(list_of_artwork_objects)
    # print(len(list_of_artwork_objects))

    # for i in list_of_artwork_objects:
    #     if i.year == "2016":
    #         print(i)

    # print("\n")
    
    # print(artworks_by_criterion)
    # print(len(artworks_by_criterion))
    # draw_bar_chart(artworks_by_criterion, user_input_country)
    # draw_scatter_plot(artworks_by_criterion)

      





if __name__ == "__main__":
    main()