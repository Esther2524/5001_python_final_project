
import matplotlib.pylab as plt


def classify_artworks_by_criterion(artworks, criterion):

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


def draw_pie_chart(artworks_by_criterion, country):

    fig, ax = plt.subplots()
    autopct_format = "%1.1f%%"
    ax.pie(artworks_by_criterion.values(), labels = artworks_by_criterion.keys(), autopct = autopct_format)
    ax.set_title(f"Artworks of artists from {country}")

    plt.show()





def draw_bar_chart(dict_of_artworks_by_criterion, country):
 

    # Create and show the bar chart
    fig, ax = plt.subplots()

    # Sort the dictionary items by key
    sorted_items = sorted(dict_of_artworks_by_criterion.items())
    # Unpack the sorted dictionary items into separate lists for x and y values
    x_values, y_values = zip(*sorted_items)
    ax.bar(x_values, y_values)

    # Set the x-axis label
    ax.set_xlabel("Year")

    # Set the y-axis label
    ax.set_ylabel("Artwork Count")

    # Set the title of the chart
    ax.set_title("Artwork Counts by Year")

    # Set the y-axis range and interval
    max_value = max(y_values)
    ax.set_yticks(range(0, max_value + 1, 1))

    plt.show()



# def draw_line_chart(dict_of_artworks_by_criterion, country):

#     fig, ax = plt.subplots()

#     # plot the data as a line chart
#     ax.plot(year, counts)

#     # set the title and labels for the chart
#     ax.set_title(f"Line Chart of artworks from {country}")
#     ax.set_xlabel("year")
#     ax.set_ylabel("counts")
    
#     # show the chart
#     plt.show()


def draw_scatter_plot(dict_of_artworks_by_criterion):


    # Create a scatter plot
    plt.plot(dict_of_artworks_by_criterion.keys(), dict_of_artworks_by_criterion.values(), linestyle='--', marker='o', color='b')

    # Set the x-axis label
    plt.xlabel('X Axis')

    # Set the y-axis label
    plt.ylabel('Y Axis')

    # Set the title of the chart
    plt.title('Scatter Plot')

    # Show the plot
    plt.show()

