


def classify_artworks_by_criterion(artworks, criterion):
    '''
    Function:
        classify_artworks_by_criterion -- classifies artworks by a given criterion and returns a dictionary where the keys are the unique values of the criterion found in the artworks, 
                                          and the values are the number of artworks that have each value of the criterion.
    Parameters:
        artworks -- a list of artwork objects
        criterion -- a string, the name of an attribute of the artwork objects to be used as the criterion for classification.
    Returns:
        dic_of_artworks_by_criterion -- a dictionary, where the keys are the unique values of the criterion found in the
                                        artworks, and the values are the number of artworks that have each value of the criterion.
    Error handling:
        raise TypeError if artworks is not a list
        raise TypeError if criterion is not a string
    '''

    if not isinstance(artworks, list):
        raise TypeError(f"in classify_artworks_by_criterion(): {artworks} should be a list")
    if not isinstance(criterion, str):
        raise TypeError(f"in classify_artworks_by_criterion(): {criterion} should be a string")

    # in the list of artwork objects, some artworks objects will be created many times
    # because one artwork may have many artists, and I use id of artists to create corresponding artwork objects

    # A set is an unordered collection of unique elements, meaning that it can only contain one copy of each element, and the order in which the elements were added to the set is not preserved.
    # unique_artworks is intended to store unique instances of the ArtWork class.
    # When we add an ArtWork instance to the unique_artworks set using the add() method, 
    # the __eq__ method of the ArtWork class is used to determine if the instance is already present in the set.
    
    unique_artworks = set()
    
    for artwork in artworks:
        unique_artworks.add(artwork)

    dic_of_artworks_by_criterion = {}
        # artwork is an object of class ArtWork, so self.artworks is a list of artwork objects

    for artwork in unique_artworks:
        # print(artwork)
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




def filter_artworks_by_attribute_value(artworks, attribute, value):
    '''
    Returns a list of artwork objects from the input list that have the specified attribute set to the specified value.
    '''

    filtered_artworks = []

    for artwork in artworks:
        artwork_attribute = getattr(artwork, attribute)
        # print(artwork_attribute)
        if artwork_attribute == value:
            filtered_artworks.append(artwork)

    return filtered_artworks