
import tkinter as tk
from tkinter import ttk

from filter_data_and_draw_charts import *

PADX_VALUE = 10
PADY_VALUE = 5

# view里面有 input 和 visulization

root = tk.Tk()

def create_start_page(df_art, df_artist):
        
        # class
        root.title("Artwork Viewer")
        root.geometry("800x400")
        
        # 一个root 两个frame
        # add some explanation
        explanation = "\nSelect the country you are interested in \n\nYou will see the distribution of all artworks created by artists from that country by type, status, material, neighbourhood, and year\n"
        label_explanation = ttk.Label(root, text = explanation)
        label_explanation.pack()


        label_country = ttk.Label(root, text="Select a country:")
        label_country.pack(padx=PADX_VALUE, pady=PADX_VALUE)

        # options_country is a list
        options_country = df_artist["country"].unique()

        # remove special characters from option list
        options_country = [option.replace("[", "").replace("]", "") for option in options_country]

        # state="readonly" is used to prevent the user from manually editing the value of a Tkinter Combobox 
        combo_country = ttk.Combobox(root, values=options_country, state="readonly")
        combo_country.pack(padx=PADX_VALUE, pady=PADY_VALUE)


        label_category = ttk.Label(root, text="Select a category:")
        label_category.pack(padx=PADX_VALUE, pady=PADX_VALUE)

        # get coloums's names except for the first two items
        options_category = df_art.columns.tolist()
        options_category = options_category[2:]

        combo_category = ttk.Combobox(root, values=options_category, state="readonly")
        combo_category.pack(padx=PADX_VALUE, pady=PADY_VALUE)


        # create a button to display the pie chart
        # the model is display_chart_and_output_result()
        button = ttk.Button(root, text="Show chart", command=lambda: display_chart_and_output_result(df_art, df_artist, combo_country.get(), combo_category.get()))
        # use pack method to display it
        button.pack(padx=PADX_VALUE, pady=PADX_VALUE)
        
        # start the GUI event loop
        # the method that runs continuously and listens for events, including mouse clicks
        root.mainloop()