

from class_of_artist import Artist
from class_of_art import ArtWork

from create_dataframe_from_dataset import create_dataframe


# def get_original_data():
#     artist_data = combine_data_of_artist_table()
#     art_data =  combine_data_of_art_table()
#     return artist_data, art_data


def read_data_into_objects_by_country(chosen_country):
    '''
    根据df_artist

    '''
    # chosen_country may be "USA"
    df_artist, df_art = create_dataframe()

    # print(len(df_art))
    # print(len(df_artist))

    # create a list of Artist instances for the selected country
    list_of_artist_objects = []

    # 根据国籍建artist objects
    for i in range(len(df_artist["country"])):
        if df_artist["country"][i] == chosen_country:
            artist = Artist(df_artist["artist id"][i], df_artist["first name"][i], df_artist["last name"][i], df_artist["country"][i])
            list_of_artist_objects.append(artist)
    
    # for i in list_of_artist_objects:
        # print(i.id)

    # 根据artist objects来建artwork objects，连接点是id
    list_of_artwork_objects = []

    for i in range(len(df_art["artist id"])):
        for artist in list_of_artist_objects:
            if (artist.id == df_art["artist id"][i]) or (artist.id in df_art["artist id"][i].split(",")):
                # 让生成的 artwork object 的 id 与artist id 一一对应
                artwork = ArtWork(df_art["work title"][i], artist.id, df_art["type"][i], df_art["status"][i], df_art["material"][i], df_art["year"][i])
                # 错误的，会影响后面根据artist id 填充属性，造成重复
                # artwork = ArtWork(df_art["work title"][i], df_art["artist id"][i], df_art["type"][i], df_art["status"][i], df_art["material"][i], df_art["year"][i])
                list_of_artwork_objects.append(artwork)



    # 同时artwork objects与artist objects互为对方的属性
    # 此时的list_of_artist_objects, list_of_artwork_objects是已经筛选后的list
    # 这一步很关键，相当于往class里面填充属性
    for artist in list_of_artist_objects:
        for artwork in list_of_artwork_objects:
            # artist.id 和 artwork.id一一对应
            if artist.id == artwork.id:
            # 错误的会造成重复
            # if (artist.id == artwork.id) or (artist.id in artwork.id.split(",")):
                artist.artworks.append(artwork)
                artwork.artists.append(artist)

    return list_of_artist_objects, list_of_artwork_objects
    # print(len(artists))








    
# 测试测试测试
# list_of_artist_objects, list_of_artwork_objects = read_data_into_objects_by_country("USA")
# print(list_of_artist_objects)
# print(len(list_of_artist_objects))
# print(list_of_artwork_objects)
# print(len(list_of_artwork_objects))

# for i in list_of_artist_objects:
#     print(i.id)
#     for j in i.artworks:
#         print(j.title)
#         print(j.id)
#         print()
#     print("\n\n")

# for i in list_of_artist_objects:
#     if i.id == "555":
#         print(i.artworks)



# def read_data_into_objects(artist_data, art_data):

    # 把所有数据放进object里面
    # object instantiation
    # A list to hold all the artist objects
    
    # list_of_artist_objects = []
    # for artist in artist_data:
    #     list_of_artist_objects.append(Artist(artist[0], artist[1], artist[2], artist[3]))
  
    # print(list_of_artist_objects)


    # A list to hold all the artwork objects
    # list_of_artwork_objects = []

    # for art in art_data:

    #     artwork = ArtWork(art[0], art[1], art[2], art[3], art[4], art[5])
    #     list_of_artwork_objects.append(artwork)



    # for artist in list_of_artist_objects:
    #     for artwork in list_of_artwork_objects:
            # 考虑艺术家的合作
            # if (artist.id == artwork.id) or (artist.id in artwork.id.split(",")):
            #     artist.artworks.append(artwork)
            #     artwork.artists.append(artist)


    # 后面的代码不需要
    # 此时的list_of_artist_objects会拥有artworks这个属性
    # print(list_of_artist_objects)


    # # 让artwork object也拥有 artist的属性
    # for artwork in list_of_artwork_objects:
    #     for aritst in list_of_artist_objects:
    #         # 考虑艺术家的合作
    #         if (artwork.id == aritst.id) or (artist.id in artwork.id.split(",")):
    #             artwork.author.append(artist)
    #             break

    # print(list_of_artwork_objects[1])
    # print(list_of_artist_objects[1])

    # return list_of_artist_objects, list_of_artwork_objects

                

    # print(list_of_artwork_objects)

    # 自己生成的object没有属性，是因为封装，自己生成的object和数据里面的object不是同一个
    # he = Artist("131", "Douglas", "Senft", "Canada")
    
    # for artist in list_of_artist_objects:
    #     if artist.id == "131":
    #         print(artist.last_name)
    # print(type(he.id))

    # 这就是为什么找不到he的artworks
    # print(he.artworks)

    # for artwork in list_of_artwork_objects:
    #     if artwork.id == "131":
    #         print(tartwork.id)




    # print(list_of_artist_objects)



    
