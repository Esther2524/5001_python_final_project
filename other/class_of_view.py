
import tkinter as tk
# from tkinter import *
from tkinter import ttk


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


from read_data_into_objects import *
from filter_data import *



class TkinterApp(tk.Tk):
    def __init__(self, df_artist, df_art, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("Artwork Viewer")
        self.geometry("980x700")
        
        self.start_page = StartPage(self, df_artist, df_art)
        # self.page_one = tk.Frame(self, df_artist, df_art)
        # self.page_two = tk.Frame(self, df_artist, df_art)
        
        self.show_start_page()

    def show_start_page(self):
        self.start_page.frame.tkraise()
        
    def show_page_one(self):
        self.page_one.frame.tkraise()
        
    def show_page_two(self):
        self.page_two.frame.tkraise()


class StartPage:
    def __init__(self, parent, df_artist, df_art):
        self.parent = parent
        self.frame = tk.Frame(parent)
        self.frame.pack(fill='both', expand=True)

        title_of_start_page = ttk.Label(self.frame, text="Start Page")
        title_of_start_page.grid(row=0, column=0, sticky="nsew")
        title_font = ("Helvetica", 20, "bold")
        title_of_start_page.config(font=title_font)

        # widgets on the start page
        explanation_on_start_page = "\nSelect the country you are interested in \n\nYou will see the distribution of all artworks created by artists from that country by type, status, material, neighbourhood, and year\n"
        label_explanation = ttk.Label(self.frame, text = explanation_on_start_page)
        label_explanation.grid(row=1, column=0, sticky="nsew")

        label_country = ttk.Label(self.frame, text="Select a country:")
        label_country.grid(row=2, column=0, sticky="nsew")


        options_country = df_artist["country"].unique()
        options_country = [option.replace("[", "").replace("]", "") for option in options_country]

        combo_country = ttk.Combobox(self.frame, values=options_country, state="readonly")
        combo_country.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")

        label_category = ttk.Label(self.frame, text="Select a category:")
        label_category.grid(row=4, column=0, sticky="nsew")

        options_category = df_art.columns.tolist()
        options_category = options_category[2:]

        combo_category = ttk.Combobox(self.frame, values=options_category, state="readonly")
        combo_category.grid(row=5, column=0, sticky="nsew")

        button = ttk.Button(self.frame, text="Show chart")
        button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.country_combo = combo_country
        self.category_combo = combo_category
        self.button = button

    def get_country(self):
        return self.country_combo.get()

    def get_category(self):
        return self.category_combo.get()
