
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

    # print(content_of_arts)

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
    pattern = r"\n(\d{1,3});([^;]*)?;([^;]*);"
    # 匹配的原则

    matches = re.findall(pattern, content_of_artists)

    # if the string is ;;, then I cannot match. But I want when ;;, the match can return something like none, instead of not matching

    # print(list_of_last_name)
    # print(len(list_of_last_name))
    print(matches)

    # matches_list = []

    # for match in matches:
    #     if match[1] == "":
    #         match_1 = None
    #     else:
    #         match_1 = match[1]
    #     matches_list.append([match[0], match_1, match[2]])

    # print(matches_list)
    # print(len(matches_list))

    # if matches:
    #     for match in matches:
    #         id = match[0]
    #         first_name = match[1]
    #         last_name = match[2]
    #         print(id, first_name, last_name)
            






else:
    print("failed")




