'''
CS5001
Final Project
Spring 2023
MyName: Zhixiao Wang

This is a file to create a ArtWork class.
'''


class ArtWork:
    '''
    ArtWork -- A class representing an artwork.

    Attributes:
        title -- a string, representing the title of the artist
        id -- a string, representing the id of the artist of this artwork
        type -- a string, representing the type of the artist
        status -- a string, representing the status of the artwork
        material -- a string, representing  the material of the artwork
        neighbourhood -- a string, representing the neighbourhood where the artwork is located
        year -- a string,  representing the year in which the artwork was created

    Methods:
        __init__() -- constructor, create a new instance of a GuessingGame instance
            Parameter:
                self -- the current object
                title -- a string , the title of the artwork
                id -- a string, the id of the artist of this artwork
                type -- a string, the type of the artwork
                status -- a string, the status of the artwork
                material -- a string , the material of the artwork
                neighbourhood -- a string , the neighbourhood where the artwork is located
                year -- a string , the year of the artwork in which the artwork was created
            Return:
                nothing
            Error handling:
                raise TypeError if title is not a string
                raise TypeError if id is not a string
                raise TypeError if type is not a string
                raise TypeError if status is not a string
                raise TypeError if material is not a string
                raise TypeError if neighbourhood is not a string
                raise TypeError if year is not a string

         __eq__(): a method that compares the id of two Artwork instances and returns True if they are the same, False otherwise.
            Parameter:
                self -- the current object
                other_artwork -- the other Artwork instance
            Return:
                returns True if all the information (except for ids of their artists) of them is the same, False otherwise.
            Error handling:
                raise TypeError if other is not a Artwork instance
            
        __hash__(): a method is used to generate a hash value that can be used to quickly look up an object in a dictionary or set
            Parameter:
                self -- the current object
            Return:
                nothing

        __str__(): a method that returns a string representation of the artwork object, including their id and country.
            Parameter:
                self -- the current object
            Return:
                a string, representing a ArtWork instance

        Note that the uniqueness of the artworks is determined by their attributes, so artworks with the same title, type, and year would be considered duplicates 
        even if they have different artist id.
    '''

    def __init__(self, title, id, type, status, material, neighbourhood, year):
        if not isinstance(title, str):
            raise TypeError(f"The title '{title}' should be a string")
        if not isinstance(id, str):
            raise TypeError(f"The id '{id}' should be a string")
        if not isinstance(type, str):
            raise TypeError(f"The type '{type}' should be a string")
        if not isinstance(status, str):
            raise TypeError(f"The status '{status}' should be a string")
        if not isinstance(material, str):
            raise TypeError(f"The material '{material}' should be a string")
        if not isinstance(neighbourhood, str):
            raise TypeError(f"The neighbourhood '{neighbourhood}' should be a string")
        if not isinstance(year, str):
            raise TypeError(f"The year '{year}' should be a string")

        self.title = title
        self.id = id
        self.type = type
        self.status = status
        self.material = material
        self.neighbourhood = neighbourhood
        self.year = year

    def __str__(self):
        return f"{self.title} (from artist id {self.id})"
    
    def __eq__(self, other_artwork):
        if not isinstance(other_artwork, ArtWork):
            raise TypeError(f"The compared '{other_artwork}' should be an ArtWork instance")
        if self.title == other_artwork.title:
            return True
        else:
            return False

    def __hash__(self):
        # Note: artworks with different ids of its artists but the same title, type, status, material, and year will be considered equal.
        return hash((self.title, self.type, self.status, self.material, self.neighbourhood, self.year))
        # except for id




        # The __hash__ method is used to generate a hash value that can be used to quickly look up an object in a dictionary or set. 
        # When a new ArtWork object is added to the set unique_artworks, 
        # Python will use the __hash__ method to compute a hash value for the object, 
        # and then check if there are any other objects in the set with the same hash value. 

        # If there are, Python will call the __eq__ method to compare the objects for equality.
        # Together, the __hash__ and __eq__ methods allow ArtWork objects to be stored in a set 
        # while ensuring that duplicate objects are not added to the set based on their attribute values.
    
    
            
        





        

    
     