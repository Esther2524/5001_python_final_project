
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

from other.filter_data_and_draw_charts import *
from create_dataframe_from_dataset import *






# create the GUI window
root = tk.Tk()
root.title("Artwork Viewer")

def create_main_window():

    df_artist, df_art = create_dataframe()

    # create a label and dropdown menu for the countries
    label = ttk.Label(root, text="Select a country:")
    label.pack(padx=10, pady=10)
    options = df_artist["country"].unique()
    combo = ttk.Combobox(root, values=options)
    combo.pack(padx=10, pady=5)

    # create a button to display the pie chart
    button = ttk.Button(root, text="Show pie chart", command=lambda: draw_bar_chart(combo.get()))
    button.pack(padx=10, pady=10)

    # start the GUI event loop
    root.mainloop()

create_main_window()
