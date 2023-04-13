
import requests
import re



def get_art_csv_file():

    download_arts = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/public-art/exports/csv?lang=en&timezone=America%2FLos_Angeles&use_labels=true&delimiter=%3B"
    response_arts_website = requests.get(download_arts)

    if response_arts_website.status_code != 200:
        raise 

    # content_of_arts = response_arts_website.content.decode('utf-8')
    content_of_arts = response_arts_website.text

    # material里面有; 会导致错位,出现type里面有no longer in place和in place的选项
    content_of_arts = content_of_arts.replace("; ", " ")
    # print(content_of_arts)


    return content_of_arts

def replace_empty_with_unknown(original_list):
    '''
    used to clean data
    '''
    for i in range(len(original_list)):
        if original_list[i] == "":
            original_list[i] = "Unknown"

    return original_list


def get_work_title_from_art_table():

    content_of_arts = get_art_csv_file()

    # noid, title, no, type, status, no, no, material, http, no, no, neighborhood, no, no, no, no, id, no, year

    pattern_of_work_title = r"\r\n\d{1,};([^;]*);"

    # 提取work_title
    matches_of_work_title = re.findall(pattern_of_work_title, content_of_arts)
    # print(matches_of_work_title)
    # print(len(matches_of_work_title))
    list_of_work_title = matches_of_work_title

    list_of_work_title = replace_empty_with_unknown(list_of_work_title)
    
    return list_of_work_title
    

    # print(list_of_work_title)
    # print(len(list_of_work_title))
    # 670个

def get_other_info_from_art_table():

    content_of_arts = get_art_csv_file()

    # 遇到大段文字直接跳过 regex前面部分的 regex后面部分的


    # 提取type status site_address primary material art_url 
    # 从type status neighborhood artist_id year
    # 一次性提取虽然方便 但是bug实在太多 特别是最后几行 不知道是什么玩意
    # pattern_of_other_info = r";([^;]*);([^;]*);[^;]*;[^;]*;[^;]*;[^;]*;[^;]*;[^;]*;([^;]*);[^;]*;[^;]*;[^;]*;[^;]*;([^;]*);[^;]*;([^;]*);[^;]*(?:\r\n\d{1,3};|\r$)"
    # matches = re.findall(pattern_of_other_info, content_of_arts)
    # print(matches)
    # print(len(matches))
    # list_of_other_info = []
    # if matches:
    #     for match in matches:
    #         list_of_other_info.append([match[0]])
    # print(list_of_other_info)
    # print(len(list_of_other_info))


    # 分步操作
    # pattern_of_type_and_status_and_material = r";([^;]*);([^;]*);[^;]*;[^;]*;([^;]*);https[^;]*;[^;]*;[^;]*;([^;]*);"

    # 正确的
    pattern_of_type_and_status_and_material = r";([^;]*);([^;]*);[^;]*;[^;]*;([^;]*);https.*"

    # pattern_of_type_and_status_and_material = r";([^;]*);([IND][^;]*);[^;]*;[^;]*;((?:[^;]*[;][^;]*|[^;]*));https.*cova.*;"
    # pattern_of_type_and_status_and_material = r";([^;]*);([^;]*);[^;]*;[^;]*;(?:.*[;]\s.*|[^;]*);https.*cova.*;"

    matches_of_type_and_status_and_material = re.findall(pattern_of_type_and_status_and_material, content_of_arts)
    list_of_type_and_status_and_material = matches_of_type_and_status_and_material

    # print(matches_of_type_and_status_and_material)
    # print(len(matches_of_type_and_status_and_material))

    list_of_type = []
    list_of_status = []
    list_of_material = []

    for lst in list_of_type_and_status_and_material:
        list_of_type.append(lst[0])
        list_of_status.append(lst[1])
        list_of_material.append(lst[2])

    list_of_type = replace_empty_with_unknown(list_of_type)
    list_of_status = replace_empty_with_unknown(list_of_status)
    list_of_material = replace_empty_with_unknown(list_of_material)

    return list_of_type, list_of_status, list_of_material
    
    


# def get_neighborhood_from_art_table():
    # 放弃提取neighbourhood了 前后都是大段文本含; 根本提取不出来。。。
    # pattern_of_neighborhood = r";https.*;(?:https.*;|;)[^;]*;([^;]*);"
    # pattern_of_neighborhood = r';https.*covapp.*;(?:https.*opendata.*;|;)("{.*}")?;([^;]*);[^;]*;'
    # matches_of_neighborhood = re.findall(pattern_of_neighborhood, content_of_arts)

    # print(matches_of_neighborhood)
    # print(len(matches_of_neighborhood))

    # neighborhood_list = []
    # if matches_of_neighborhood:
    #     for match in matches_of_neighborhood:
    #         neighborhood_list.append(match[1])

    # print(neighborhood_list)
    # print(len(neighborhood_list))

    
    
def get_artist_id_and_year_from_art_table():

    content_of_arts = get_art_csv_file()
    
    pattern_of_id_and_year = r"([^;]*);[^;]*;([^;]*);[^;]*(?:\r\n\d{1,3};|\r$)"
    matches_of_id_and_year = re.findall(pattern_of_id_and_year, content_of_arts)

    # print(matches_of_artist_id)
    # print(len(matches_of_artist_id))

    # 每次以最后作为基准的时候 会把第一列也给算进去，所以需要-1
    list_of_id_and_year = matches_of_id_and_year[1::]

    list_of_artist_id = []
    list_of_year = []

    for lst in list_of_id_and_year:
        list_of_artist_id.append(lst[0])
        list_of_year.append(lst[1])
    
    # print(list_of_artist_id, list_of_year)
    # print(len(list_of_artist_id))

    list_of_artist_id = replace_empty_with_unknown(list_of_artist_id)
    list_of_year = replace_empty_with_unknown(list_of_year)

    return list_of_artist_id, list_of_year




def combine_data_of_art_table():

    # 如果不相等
    # for i in 

    work_title = get_work_title_from_art_table()
    type, status, material = get_other_info_from_art_table()
    artist_id, year = get_artist_id_and_year_from_art_table()


    data_of_art_table = []
    for i in range(len(artist_id)):
        data_of_art_table.append([work_title[i], artist_id[i], type[i], status[i], material[i], year[i]])
    # print(data_of_art_table) 


    return data_of_art_table


get_other_info_from_art_table()



