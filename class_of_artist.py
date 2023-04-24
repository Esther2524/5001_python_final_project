'''
CS5001
Final Project
Spring 2023
MyName: Zhixiao Wang

This is a file to create a Artist class.
'''


class Artist:
    '''
    Artist -- A class representing an artist.
    Attributes:
        id -- A string representing the unique identifier of the artist.
        first_name -- A string representing the first name of the artist.
        last_name -- A string representing the last name of the artist.
        country -- A string representing the country of the artist.
        artworks -- A list containing all the artworks for this artist.
    Methods:
        __init__() -- constructor, create a new instance of a GuessingGame instance
            Parameter:
                self -- the current object
                id -- a string , the id of the artist
                first_name -- a string, the first name of the artist
                last_name -- a string, the last name of the artist
                country -- a string, the country of the artist
            Return:
                nothing
            Error handling:
                raise TypeError if id is not a string
                raise TypeError if first_name is not a string
                raise TypeError if last_name is not a string
                raise TypeError if country is not a string

        __eq__(): a method that compares the id of two artist objects and returns True if they are the same, False otherwise.
            Parameter:
                self -- the current object
                other_artist -- the other Artist instance
            Return:
                returns True if their ids are the same, False otherwise.
            Error handling:
                raise TypeError if other is not a Artist instance
            
        __str__(): a method that returns a string representation of the artist object, including their id and country.
            Parameter:
                self -- the current object
            Return:
                a string, represent a Artist instance
    '''

    def __init__(self, id, first_name, last_name, country):
        if not isinstance(id, str):
            raise TypeError(f"The id '{id}' should be a string")
        if not isinstance(first_name, str):
            raise TypeError(f"The first name '{first_name}' should be a string")
        if not isinstance(last_name, str):
            raise TypeError(f"The last name '{last_name}' should be a string")
        if not isinstance(country, str):
            raise TypeError(f"The country '{country}' should be a string")

        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.country = country

    def __eq__(self, other_artist):
        if not isinstance(other_artist, Artist):
            raise TypeError(f"The compared '{other_artist}' should be an Artist instance")
        if self.id == other_artist.id: 
            return True
        else:
            return False

    def __str__(self):
        return f"artist {self.id} from {self.country}"
    
    


  
