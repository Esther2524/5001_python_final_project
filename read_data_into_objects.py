

from class_of_artist import Artist
from class_of_art import ArtWork

def read_data_into_objects(artist_data, art_data):

    # 把所有数据放进object里面
    # object instantiation
    # A list to hold all the artist objects
    list_of_artist_objects = []

    

    for artist in artist_data:
        list_of_artist_objects.append(Artist(artist[0], artist[1], artist[2], artist[3]))
  

    # print(list_of_artist_objects)




    # A list to hold all the artwork objects
    list_of_artwork_objects = []

    for art in art_data:

        artwork = ArtWork(art[0], art[1], art[2], art[3], art[4], art[5])
        list_of_artwork_objects.append(artwork)



    for artist in list_of_artist_objects:
        for artwork in list_of_artwork_objects:
            if artist.id == artwork.id:
                artist.artworks.append(artwork)

    # 此时的list_of_artist_objects会拥有artworks这个属性
    # print(list_of_artist_objects)

    return list_of_artist_objects

                

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
