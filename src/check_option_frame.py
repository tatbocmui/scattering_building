import tkinter as tk
from tkinter import ttk

def create_check_option_frame(parent):
    # Create a container frame for check options
    check_frame = ttk.Frame(parent, padding="10 10 10 10")
    # check_frame.grid(row=0, column=1, sticky="nw")

    # Dictionary to hold the variables associated with each check option
    check_vars = {
        "iwriteFile": tk.IntVar(value=0),
        "ienableFinitePlate": tk.IntVar(value=0),
        "ienableTEPol": tk.IntVar(value=0),
        "ienableSlabEvMode": tk.IntVar(value=0),
        "ienablePOCalculation": tk.IntVar(value=0)
    }

    # List of check button options
    options = [
        "iwriteFile",
        "ienableFinitePlate",
        "ienableTEPol",
        "ienableSlabEvMode",
        "ienablePOCalculation"
    ]

    # Create checkbuttons for each option
    for option in options:
        checkbutton = ttk.Checkbutton(check_frame, text=option, variable=check_vars[option],
                                      onvalue=1, offvalue=0)
        checkbutton.grid(row=options.index(option), column=0, sticky="w")

    return check_frame, check_vars
