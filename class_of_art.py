

class ArtWork:

    def __init__(self, title, artist_id, type, status, material, year):
        self.title = title
        self.id = artist_id
        self.type = type
        self.status = status
        self.material = material
        self.year = year

    def __repr__(self):
        return f"{self.title} (from id {self.id})"
        
        


    # self.author = list [objects of artists] #id name country

    # def get_author():

    #     return self.author[0].first_name

    # self.type



        

    

        