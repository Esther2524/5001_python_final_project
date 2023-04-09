

import matplotlib.pyplot as plt


def filter_data_by_country(input_country, list_of_artist_objects):

    # 这个国籍的艺术家的所有艺术品
    country_artworks = []

    for artist in list_of_artist_objects:
        if artist.country == input_country:
            # 这里extend与append的区别是？
            country_artworks.extend(artist.artworks)

    # print(country_artworks)
    # print(len(country_artworks))

    return country_artworks


def categorize_artworks_by_type(country_artworks):
    dict_of_type_counts = {}

    # artwork是一个object 遍历country_artworks里面的所有object
    for artwork in country_artworks:
        artwork_type = artwork.type
        if artwork_type in dict_of_type_counts:
            dict_of_type_counts[artwork_type] += 1
        else:
            dict_of_type_counts[artwork_type] = 1

    list_of_types = []
    list_of_counts = []
    for key, value in dict_of_type_counts.items():
        list_of_types.append(key)
        list_of_counts.append(value)

    # print(types)
    # print(counts)

    return list_of_types, list_of_counts
    
def categorize_artworks_by_materal(country_artworks):
    dict_of_material_counts = {}

    # artwork是一个object 遍历country_artworks里面的所有object
    for artwork in country_artworks:
        artwork_material = artwork.material
        if artwork_material in dict_of_material_counts:
            dict_of_material_counts[artwork_material] += 1
        else:
            dict_of_material_counts[artwork_material] = 1

    list_of_material = []
    list_of_counts = []
    for key, value in dict_of_material_counts.items():
        list_of_material.append(key)
        list_of_counts.append(value)

    # print(types)
    # print(counts)

    return list_of_material, list_of_counts


def categorize_artworks_by_year(country_artworks):
    dict_of_year_counts = {}

    # artwork是一个object 遍历country_artworks里面的所有object
    for artwork in country_artworks:
        artwork_year = artwork.year
        if artwork_year in dict_of_year_counts:
            dict_of_year_counts[artwork_year] += 1
        else:
            dict_of_year_counts[artwork_year] = 1

    list_of_year = []
    list_of_counts = []
    for key, value in dict_of_year_counts.items():
        list_of_year.append(key)
        list_of_counts.append(value)

    # print(types)
    # print(counts)

    return list_of_year, list_of_counts



