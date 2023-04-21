from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

def generate_plot(parent_frame):
    # Generate the plot using Matplotlib
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot([1, 2, 3, 4, 5], [10, 5, 20, 15, 25])

    # Create a Matplotlib canvas and toolbar
    canvas = FigureCanvasTkAgg(fig, master=parent_frame)
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, parent_frame)
    toolbar.update()

    # Create a label with the canvas and toolbar
    canvas.get_tk_widget().pack()
    toolbar.pack()
    label = Label(parent_frame, text="Page One")
    label.pack()

# Create the GUI window
root = Tk()

# Create the frames
start_page = Frame(root)
page_one = Frame(root)

# Generate the plot in page_one using the generate_plot() function
generate_plot(page_one)

# Create a button to switch to page_one
button = Button(start_page, text="Go to Page One", command=lambda: [start_page.pack_forget(), page_one.pack()])
button.pack()

# Create a button in page_one
button_page_one = Button(page_one, text="Click me!")
button_page_one.pack()

# Pack the frames
start_page.pack()
page_one.pack_forget()

# Start the GUI loop
root.mainloop()
