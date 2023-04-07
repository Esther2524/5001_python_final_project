
# from create_data_frame import convert_data_to_dataframe

class Artist:
    # class variable为啥我不能access到
   
    
    def __init__(self, artist_id, first_name, last_name, country):

        self.id = artist_id
        self.first_name = first_name
        self.last_name = last_name
        
        self.country = country

        # A list to hold all the artworks for this artist
        self.artworks = []

    def __repr__(self):
        return f"{self.last_name} ({self.country}) ({self.artworks})"


    # def first_name(self):

    # def country(self):
    #     country = df_artist.loc[]
    #     return country

    # self.art = 

    
