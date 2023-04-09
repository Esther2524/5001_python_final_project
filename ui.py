
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

# create the data frame
data_artwork = {
    "id": [1, 2, 3, 4, 5, 6, 7],
    "artist_id": [1, 2, 2, 2, 3, 3, 4],
    "country": ["Canada", "China", "China", "China", "Canada", "Canada", "USA"],
    "type": ["Painting", "Sculpture", "Painting", "Drawing", "Sculpture", "Painting", "Drawing"]
}
df_artwork = pd.DataFrame(data_artwork)

# define a function to display the pie chart
def display_pie_chart(country):
    # create a subset of the data frame for the selected country
    df_country = df_artwork[df_artwork["country"] == country]
    # group by artwork type and count the number of artworks
    df_counts = df_country.groupby("type").size().reset_index(name="count")
    # create a pie chart
    fig, ax = plt.subplots()
    ax.pie(df_counts["count"], labels=df_counts["type"], autopct='%1.1f%%')
    ax.axis('equal')
    ax.set_title(f"Artwork types in {country}")
    plt.show()

# create the GUI window
root = tk.Tk()
root.title("Artwork Viewer")

# create a label and dropdown menu for the countries
label = ttk.Label(root, text="Select a country:")
label.pack(padx=10, pady=10)
options = df_artwork["country"].unique()
combo = ttk.Combobox(root, values=options)
combo.pack(padx=10, pady=5)

# create a button to display the pie chart
button = ttk.Button(root, text="Show pie chart", command=lambda: display_pie_chart(combo.get()))
button.pack(padx=10, pady=10)

# start the GUI event loop
root.mainloop()
