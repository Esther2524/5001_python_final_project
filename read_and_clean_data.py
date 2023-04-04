
import requests
import re
import pandas as pd


download_arts = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/public-art/exports/csv?lang=en&timezone=America%2FLos_Angeles&use_labels=true&delimiter=%3B"
download_artists = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/public-art-artists/exports/csv?lang=en&timezone=America%2FLos_Angeles&use_labels=true&delimiter=%3B"

response_artists_website = requests.get(download_artists)
response_arts_website = requests.get(download_arts)


if response_artists_website.status_code == 200 and response_arts_website.status_code == 200:
    # 转为一个大的string
    content_of_artists = response_artists_website.content.decode('utf-8')
    content_of_arts = response_arts_website.content.decode('utf-8')

    # print(content_of_artists.split("\t"))

    # 看看内容是啥
    # print(content_of_artists[:8000:])
    # 从614开始的

    # print(len(content_of_artists))
    # output 300115

    # print(content_of_artists[-200:-1].split(";"))

    # print(content_of_artists[0:600].split(";"))

    # 以下代码都可以省略
    # artists 数据里面一共有575行
    # regex这么写的原因:artist id前面是new line后面跟着;
    # 有些网站的数据后面也跟着;所以前面的\n不能少
    # pattern_of_artist_id = r"\n(\d{1,3});"
    # list_of_artist_id = re.findall(pattern_of_artist_id, content_of_artists)
    # print(list_of_artist_id)
    # 刚好575
    # print(len(list_of_artist_id))

    # 提取名字 last name

    # 错误的 pattern
    # pattern = r"\n(\d{1,3});([A-Z][\w]*)?;([A-Z][\w]+);"

    # 基本信息的匹配

    # pattern_of_basic_info = r"\n(\d{1,3});([^;]*)?;([^;]*);(http.*?)\d{1,3};"

    # pattern = r";([^;]*)?;([^;]*)?;([^;]*)?;\n"


    # matches = re.findall(pattern_of_basic_info, content_of_artists)

    
    # print(matches)
    # print(len(matches))

    # list_of_basic_info = []

    # if matches:
    #     for match in matches:
    #         artist_id = match[0]
    #         first_name = match[1]
    #         last_name = match[2]
    #         porfile_url = match[3]
    #         list_of_basic_info.append([match[0], match[1], match[2], match[3]])

            # matches_list.append([match[0], match[1], match[2], match[3], match[4]])
            # matches_list.append(match[0])

    # print(list_of_basic_info)
    # print(len(list_of_basic_info))

    # country = r";\b([CUGIJPSAFEGNT][^;]*)\b;"
    # country = r";([CUGIJPSAFEGNT]*[^;]*?);"
    # matches = re.findall(country, content_of_artists)
 

    #  除了最后一行以外，其他都能匹配
    # pattern_of_country_apart_from_last_line = r";([^;]*)?;[^;]*;[^;]*;[^;]*\r\n\d{1,3};" 
    # pattern_of_country_of_last_line = r";([^;]*)?;[^;]*;[^;]*;[^;]*\r$"

    pattern_of_country = r";([^;]*)?;[^;]*;[^;]*;[^;]*(?:\r\n\d{1,3};|\r$)"

    

    matches_of_country = re.findall(pattern_of_country, content_of_artists)
    # print(matches2)
    # print(len(matches2))
    list_of_country = matches_of_country[1:]

    # count = 0

    # for i in range(len(list_of_country)):
    #     if list_of_country[i] == "Canada":
    #         count += 1
            # print(i)
    # print(count)

    # for i in matches:
    #     if i == "Canada":
    #         count +=1

    # print(count)

    # if matches2:
    #     for match in matches2:
    #         list_of_country.append(match)

    print(list_of_country)
    print(len(list_of_country))

    # 检查文件最后面的数据是什么样子
    # print(content_of_artists[-50:-1:])

    # pattern_of_last_line_country = r";([^;]*)?;[^;]*;[^;]*;[^;]*\r\n$"
    # pattern = r";([^;]*)?;[^;]*;[^;]*;[^;]*\r\n$"
    # pattern = r";([^;]*)?;[^;]*;[^;]*;[^;]*\r\n\d{1,3};"
  
    # match_of_last_line = re.findall(pattern_of_last_line_country, content_of_artists)
    # print(match_of_last_line)


    # 合并起来
            






else:
    print("failed")




