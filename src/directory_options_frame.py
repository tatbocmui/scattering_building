
import tkinter as tk
from tkinter import ttk

def create_directory_options_frame(parent):
    directory_frame = ttk.Frame(parent, padding="10 10 10 10")
    # directory_frame.grid(row=1, column=0, columnspan=4, sticky="nw")

    labels = [
        "directoryPath",
        "historyFolderPath"
    ]

    # Create a dictionary to hold the variables associated with each path
    directory_vars = {}

    # Create labels and entry widgets for the paths
    for i, label_text in enumerate(labels):
        label = ttk.Label(directory_frame, text=label_text + ":")
        label.grid(row=i, column=0, sticky="w")
        var = tk.StringVar()  # Initialize variable without a default value
        directory_vars[label_text] = var  # Store the variable with label as key
        entry = ttk.Entry(directory_frame, width=100, textvariable=var)
        entry.grid(row=i, column=1, sticky="w")

    return directory_frame, directory_vars
