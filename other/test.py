
class Library:
    def __init__(self, name, neighbourhood):
        self.name = name
        self.neighbourhood = neighbourhood
    def __repr__(self):
        return f"{self.name} in {self.neighbourhood}"
    
class Park:
    def __init__(self, name, neighbourhood, washroom):
        self.name = name
        self.neighbourhood = neighbourhood
        self.washroom = washroom

    def __repr__(self):
        return f"{self.name}"
        
   


def main():
    # library 的原始数据
    library_data = [["Library1", "West End"], ["Library2", "Downtown"], ["Library3", "Downtown"]]

    # 用户选择library
    user_input = "Library2"

    list_of_library_objects = []
    for i in range(len(library_data)):
        # lst1[i][1]就是neighborhood
        if library_data[i][0] == user_input:
            library = Library(library_data[i][0], library_data[i][1])
            list_of_library_objects.append(library)

    print(list_of_library_objects)

    # park的原始数据
    park_data = [["Park1", "West End", "yes"], ["Park2", "Downtown", "yes"], ["Park3", "Downtown", "yes"], ["Park4", "Downtown", "no"]]
   
    list_of_park_objects = []
    for i in range(len(park_data)):
        for object in list_of_library_objects:
            # 这一步可以优化
            if park_data[i][1] == object.neighbourhood:
                park = Park(park_data[i][0], park_data[i][1], park_data[i][2])
                list_of_park_objects.append(park)

    print(list_of_park_objects)

    # 统计数据
    dict = {}
    dict["have washroom"] = 0
    dict["no washroom"] = 0

    for obj in list_of_park_objects:
        if obj.washroom == "yes":
            dict["have washroom"] += 1
        else:
            dict["no washroom"] += 1

    print(dict)

    # output:
    # [Library2 in Downtown]
    
    # [Park2, Park3, Park4]

    # {'have washroom': 2, 'no washroom': 1}
    # 根据这个作图



    

main()