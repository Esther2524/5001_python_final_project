


class Artist:

    def __init__(self, id, first_name, last_name, country):

        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        
        self.country = country

        # A list to hold all the artworks for this artist
        self.artworks = []


    def classify_artworks_by_criterion(self, criterion):
        '''
        criterion should be "type", "year", "material", or "status"

        if criterion == "type"
        dic_of_artworks_by_criterion may be like {'Socially engaged art': 2}

        if criterion == "year"
        dic_of_artworks_by_criterion may be like {'2010': 1, '2018': 1}

        if criterion == "material"
        dic_of_artworks_by_criterion may be like {'Unknown': 1, 'plants, soil': 1}
        
        '''
        
        dic_of_artworks_by_criterion = {}
        # artwork is an object of class ArtWork, so self.artworks is a list of artwork objects
        for artwork in self.artworks:
            # getattr function to get the value of the attribute specified by the criterion parameter from the artwork object
            # in this case, artwork_criterion is like artwork.type
            # getattr(object, attribute) is equal to object.attribute, like "sculpture" = artwork.type = getattr(artwork, "type")
            artwork_criterion = getattr(artwork, criterion)
            if artwork_criterion in dic_of_artworks_by_criterion:
                dic_of_artworks_by_criterion[artwork_criterion] += 1
            else:
                dic_of_artworks_by_criterion[artwork_criterion] = 1

        # the dic artworks_by_type is like 
        return dic_of_artworks_by_criterion
    

    def __eq__(self, other):
        if isinstance(other, type(self)):
            if self.id == other.id: #
                return True
            else:
                return False
        else:
            return False

    def __str__(self):
        # 可以不用str吗
        return f"{self.first_name} {self.last_name} from {self.country}"
    
    


    





    # 不用重复再写
    # def classify_artworks_by_year(self):
    #     artworks_by_year = {}
    #     for artwork in self.artworks:
    #         if artwork.year in artworks_by_year:
    #             artworks_by_year[artwork.year] += 1
    #         else:
    #             artworks_by_year[artwork.year] = 1

    #     # the dic artworks_by_year is like {'2010': 1, '2018': 1}
    #     return artworks_by_year

    # def classify_artworks_by_material(self):
    #     artworks_by_material = {}
    #     for artwork in self.artworks:
    #         if artwork.material in artworks_by_material:
    #             artworks_by_material[artwork.material] += 1
    #         else:
    #             artworks_by_material[artwork.material] = 1

    #     # the dic artworks_by_material is like {'Unknown': 1, 'plants, soil': 1}
    #     return artworks_by_material
