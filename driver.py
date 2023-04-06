
from create_data_frame import convert_data_to_dataframe





def main():

    # 在与用户交互之前就要处理好数据？
    df1, df2 = convert_data_to_dataframe()

    # print(df1.head(4))
    # print(df1.describe())

    # 每一行的内容是一个list不包括标题
    # print(df1.values)

    # print(df2.head(4))
    # print(df2.describe())

    # 需要合并df1和df2吗？

    # 开始与用户交互
    # print("Do you want to know xxx?")



if __name__ == "__main__":
    main()