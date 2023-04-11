

class ArtWork:
    '''
    Note that the uniqueness of the artworks is determined by their attributes, so artworks with the same title, type, and year would be considered duplicates 
    even if they have different IDs.

    '''

    def __init__(self, title, id, type, status, material, year):
        # id 是一个数字，和artist id完全一样
        self.title = title
        self.id = id
        self.type = type
        self.status = status
        self.material = material
        self.year = year

        # 用artist objects去填充
        self.artists = []

    def __str__(self):
        return f"{self.title} (from id {self.id})"
    
    def __hash__(self):
        #  Note that the id attribute is not used in these methods, 
        # so artworks with different ids but the same title, type, status, material, and year will be considered equal.
        return hash((self.title, self.type, self.status, self.material, self.year))
        # 千万别加上id

        # The __hash__ method is used to generate a hash value that can be used to quickly look up an object in a dictionary or set. When a new ArtWork object is added to the set unique_artworks, Python will use the __hash__ method to compute a hash value for the object, and then check if there are any other objects in the set with the same hash value. 
        # If there are, Python will call the __eq__ method to compare the objects for equality.
        # Together, the __hash__ and __eq__ methods allow ArtWork objects to be stored in a set 
        # while ensuring that duplicate objects are not added to the set based on their attribute values.
    
    def __eq__(self, other):
        if isinstance(other, type(self)):
            if self.title == other.title:
                return True
            else:
                return False
        else:
            return False
            
        


    # self.author = list [objects of artists] #id name country

    # def get_author():

    #     return self.author[0].first_name

    # self.type



        

    

        