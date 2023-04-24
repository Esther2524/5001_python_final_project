'''
CS5001
Final Project
Spring 2023
MyName: Zhixiao Wang

This is a file of filtering data with two functions:
    classify_artworks_by_criterion (list -> dict)
        from a list of artwork objects (same country), obtain a dict of categories and numbers of artworks based on the attribute entered by the user
        This function will be called in both the first and the second selections, because the generated dict will be used for drawing charts

    filter_artworks_by_attribute_value (list -> list)
        obtain a list of artwork objects from the original list of artwork objects, according to specific value of the attribute
        This function will be called only in the second selection.
        
'''


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

    for artwork in unique_artworks:

        # getattr function to get the value of the attribute specified by the criterion parameter from the artwork object
        # in this case, artwork_criterion is like artwork.type
        # getattr(object, attribute) is equal to object.attribute, like "sculpture" = artwork.type = getattr(artwork, "type")
        
        artwork_criterion = getattr(artwork, criterion)

        if artwork_criterion in dic_of_artworks_by_criterion:
            dic_of_artworks_by_criterion[artwork_criterion] += 1
        else:
            dic_of_artworks_by_criterion[artwork_criterion] = 1
    
    return dic_of_artworks_by_criterion




def filter_artworks_by_attribute_value(artworks, attribute, value):
    '''
    Function:
        filter_artworks_by_attribute_value -- return a list of artwork objects from the input list that have the specified attribute set to the specified value.

    Parameter:
        artworks -- a list of artwork objects to filter.
        attribute -- a string, specifying the attribute to filter on.
        value -- a string, the value to match the specified attribute against.

    Return:
        filtered_artworks -- a list of artwork objects, that have the specified attribute set to the specified value.

    Error handling:
        raise TypeError if artworks is not a list
        raise TypeError if attribute is not a str
        raise TypeError if value is not a str
        
    Note:
    This function is mainly used for the second selection
    Attribute and value are user-selected
    If attribute is year and the value is 2016, then the filtered_artworks is a list of artwork objects that all objects' 'year' attribute is equal to 2016
    '''

    if not isinstance(artworks, list):
        raise TypeError(f"{artworks} should be a list")
    
    if not isinstance(attribute, str):
        raise TypeError(f"{attribute} should be a str")
    
    if not isinstance(value, str):
        raise TypeError(f"{value} should be a str")
    
    # when the user doesn't select anything in the drop-down box
    if attribute == "":
        raise AttributeError("artwork's attribute cannot be empty")
    
    filtered_artworks = []

    for artwork in artworks:
        artwork_attribute = getattr(artwork, attribute)
        if artwork_attribute == value:
            filtered_artworks.append(artwork)

    return filtered_artworks