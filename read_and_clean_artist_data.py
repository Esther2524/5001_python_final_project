
import requests
import re




def get_artist_csv_file():
    download_artists = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/public-art-artists/exports/csv?lang=en&timezone=America%2FLos_Angeles&use_labels=true&delimiter=%3B"
    # if response_artists_website.status_code == 200:
    response_artists_website = requests.get(download_artists)
    content_of_artists = response_artists_website.content.decode('utf-8')

    return content_of_artists



    

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



def get_basic_info_from_artist_table(content_of_artists):
    # 基本信息的匹配
    # id, first_name, last_name
    pattern_of_basic_info = r"\r\n(\d{1,3});([^;]*);([^;]*);http.*\d{1,3};"

    # 好像没有区别-加不加问号
    # pattern_of_basic_info = r"\r\n(\d{1,3});([^;]*)?;([^;]*);(http.*?)\d{1,3};"
    # pattern = r";([^;]*)?;([^;]*)?;([^;]*)?;\n"

    matches_of_basic_info = re.findall(pattern_of_basic_info, content_of_artists)
    # print(matches)
    # print(len(matches))

    list_of_artist_id = []
    list_of_first_name = []
    list_of_last_name = []
    

    # if not matches:
    #     raise 

    for match in matches_of_basic_info:
        list_of_artist_id.append(match[0])
        list_of_first_name.append(match[1])
        list_of_last_name.append(match[2])

    return list_of_artist_id, list_of_first_name, list_of_last_name

    # 包括id, first_name, last_last 的一个list of lists
    # print(list_of_basic_info)
    # print(len(list_of_basic_info))

    # country = r";\b([CUGIJPSAFEGNT][^;]*)\b;"
    # country = r";([CUGIJPSAFEGNT]*[^;]*?);"
    # matches = re.findall(country, content_of_artists)
 

    #  除了最后一行以外，其他都能匹配
    # pattern_of_country_apart_from_last_line = r";([^;]*)?;[^;]*;[^;]*;[^;]*\r\n\d{1,3};" 
    # pattern_of_country_of_last_line = r";([^;]*)?;[^;]*;[^;]*;[^;]*\r$"

def get_country_from_artist_table(content_of_artists):
    pattern_of_country = r";([^;]*);[^;]*;[^;]*;[^;]*(?:\r\n\d{1,3};|\r$)"
    matches_of_country = re.findall(pattern_of_country, content_of_artists)
    # print(matches2)
    # print(len(matches2))

    # if not matches_of_country:
        # raise

    # 以最后作为标准会匹配到第一行，所以要减掉
    list_of_country = matches_of_country[1:]

    # print(list_of_country)
    # print(len(list_of_country))

    return list_of_country
    

    # 检查文件最后面的数据是什么样子
    # print(content_of_artists[-50:-1:])

    # pattern_of_last_line_country = r";([^;]*)?;[^;]*;[^;]*;[^;]*\r\n$"
    # pattern = r";([^;]*)?;[^;]*;[^;]*;[^;]*\r\n$"
    # pattern = r";([^;]*)?;[^;]*;[^;]*;[^;]*\r\n\d{1,3};"
  
    # match_of_last_line = re.findall(pattern_of_last_line_country, content_of_artists)
    # print(match_of_last_line)


    # 把 list_of_basic_info 和 list_of_country 合并起来
    # 那么生成的 list_of_artist_profile 还是一个 list of lists

def combine_data_of_artist_table(artist_id, first_name, last_name, country):
    data_of_artist_table = []

    for i in range(len(artist_id)):
        data_of_artist_table.append([artist_id[i], first_name[i], last_name[i], country[i]])

    return data_of_artist_table


# def get_artist_dataframe(data_of_artist_table):
    # dataframe_of_artist = pd.DataFrame(data_of_artist_table, columns=["artist id", "first name", "last name", "country"])

    # print(dataframe_of_artist.head(8))
    # print(dataframe_of_artist.tail(8))
    # print(dataframe_of_artist.info())
    # print(dataframe_of_artist.describe())
    # print(dataframe_of_artist.shape)

    # return data_of_artist_table




# 这个是要写在driver file里面的


# def main():
#     content = get_artist_csv_file()
#     id, first_name, last_name = get_basic_info_from_artist_table(content)
#     country = get_country_from_artist_table(content)
#     data = combine_data_of_artist_table(id, first_name, last_name, country)
#     get_artist_dataframe(data)

# if __name__ == "__main__":
#     main()









