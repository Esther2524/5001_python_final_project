import tkinter as tk
from tkinter import *
# from tkinter import ttk

# from matplotlib import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from tkinter import messagebox

from read_data_into_objects import *
from get_and_clean_art_data import combine_data_of_art_table
from get_and_clean_artist_data import combine_data_of_artist_table

artist_data = combine_data_of_artist_table()
art_data = combine_data_of_art_table()
list_of_artist_objects, list_of_artwork_objects = read_data_into_objects(artist_data, art_data)

# the main window of the GUI application. By default, root is a global variable, 
# so it can be accessed and modified from anywhere in the code.
window = tk.Tk()

def generate_pie_chart():

    # Find the number of artworks in each country
    artworks_by_country = {}
    # artworks_by_country is a dictionary where the keys are the names of countries and the values are the number of artworks in that country.

    for artwork in list_of_artwork_objects:
        for artist in artwork.artists:
            country = artist.country
        if country in artworks_by_country:
            artworks_by_country[country] += 1
        else:
            artworks_by_country[country] = 1

    # Unknown不一定要去掉
    # Remove keys= "Unknown" from the dictionary
    # if "Unknown" in artworks_by_country.keys():
    #     del artworks_by_country["Unknown"]

    # Sort the country data by number of artworks
    sorted_countries = sorted(artworks_by_country.items(), key=lambda x: x[1], reverse=True)

    # Only include the top five countries in the chart
    top_five_countries = dict(sorted_countries[:5])

    # Generate the pie chart
    # fig, ax = plt.subplots()
    # 这里对dict的keys和values的运用很巧妙
    # ax.pie(top_five_countries.values(), labels=top_five_countries.keys(), autopct="%1.1f%%")
    # ax.set_title("Artworks by Country")
    # plt.show()
    # plt.close(fig)

    # 第一步展示分布的时候还是用直方图比较好
    fig, ax = plt.subplots()
    ax.bar(top_five_countries.keys(), top_five_countries.values())
    ax.set_xlabel('Name of Country')
    ax.set_ylabel('Number of Artworks')
    ax.set_title("Artworks of Artists from Different Countries")
    plt.show()

    # plt.close(fig) is a function from the matplotlib library that closes a figure window. 
    # In this case, it is being used to close the figure window after generating the pie chart so that the window does not remain open in the background while the program continues to run.
    plt.close(fig)

    return fig



# def on_submit_button_click(list_of_artist_objects, selected_country):
#     artworks_in_selected_country = [artist.artworks for artist in list_of_artist_objects if artist.country == selected_country]
#     num_artworks_in_selected_country = len(artworks_in_selected_country)
#     messagebox.showinfo("Result", f"There are {num_artworks_in_selected_country} artworks in {selected_country}.")



def create_main_window():
    # Create the main window
    # window = tk.Tk()
    # window.title("Artworks by Country")


    window.title("Artworks by Country")

    # create a label widget that can be added to a Tk window. 
    # It is used to provide a descriptive label for another widget,
    lbl_country = Label(window, text="Enter country:")

    # pack() is a method in tkinter that is used to place widgets in a parent widget. 
    # In this case, the lbl_country widget (which is a Label widget) is being placed in the root window using the pack() method.
    lbl_country.pack(side=LEFT)

    # Entry is a Tkinter widget that provides a single-line text box that allows the user to enter a string
    # the Entry widget is created within the window Tkinter instance, which means that the text box will appear within the main window when the program is run.
    entry_country = Entry(window)
    entry_country.pack(side=LEFT)

    # The Button widget is a clickable button that executes a command or function when pressed. 
    # The text parameter sets the label or text displayed on the button.
    # I should put the name of the function that you want to be executed when the button is clicked after the command parameter. 
    btn_generate = Button(window, text="Generate Pie Chart", command = generate_pie_chart)
    btn_generate.pack()

    # create a canvas to display the pie chart
    fig = plt.figure(figsize=(4, 4))
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=1)

    # Generate the pie chart showing the number of artworks in each country
    # pie_chart = generate_pie_chart()
    # canvas = FigureCanvasTkAgg(pie_chart, master=window)
    # canvas.draw()
    # canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)



    # Create a label and entry widget for the user to enter the country
    # label_country = tk.Label(window, text="Select a Country:")
    # label_country.pack(side=tk.LEFT, padx=10, pady=10)
    # entry_country = tk.Entry(window)
    # entry_country.pack(side=tk.LEFT, padx=10, pady=10)

    # Create a button for the user to submit their selection
    # button_submit = tk.Button(window, text="Submit", command=lambda: on_submit_button_click(entry_country.get()))
    # button_submit.pack(side=tk.LEFT, padx=10, pady=10)

    window.mainloop()


def generate_pie_chart():
    country = entry_country.get()

def main():


    create_main_window()

if __name__ == "__main__":
    main()


# # def main():

# #     # 创建窗口
# #     window = tk.Tk()
# #     # create labels

# #     button_country = tk.Button(window, text="Please choose one country")
# #     button_country.pack()

# #     # create a list of options
# #     options = ["Canada", "USA", "China", "Germany"]

# #     # create the OptionMenu widget
# #     variable = tk.StringVar(window)
# #     variable.set(options[0])  # set the default value
# #     option_menu = tk.OptionMenu(window, variable, *options)

# #     # display the OptionMenu widget
# #     option_menu.pack()


# #     # 事件循环
# #     window.mainloop()
    



# # main()


