import tkinter as tk
from tkinter import ttk

def update_vars(selected_var, vars_dict):
    # Reset all variables to 0
    for var in vars_dict.values():
        var.set(0)
    # Set the selected variable to 1
    selected_var.set(1)

def create_radio_option_frame(parent):
    # Create a container frame for radio options
    radio_frame = ttk.Frame(parent, padding="10 10 10 10")
    # radio_frame.grid(row=0, column=2, sticky="nw")

    # Dictionary to hold the variables associated with each radio option
    radio_vars = {
        "ienablePolarPlot": tk.IntVar(value=0),
        "ienable2DPlot": tk.IntVar(value=0),
        "ienable2DPlot_t90": tk.IntVar(value=0),
        "ienable3DPlot": tk.IntVar(value=0),
        "ienableMonoStaticPlot": tk.IntVar(value=0),
        "ienableMonoStaticRCSPlot": tk.IntVar(value=0),
        "ienableBiObjRotPlot": tk.IntVar(value=0)
    }

    # List of radio button options
    options = [
        "ienablePolarPlot",
        "ienable2DPlot",
        "ienable2DPlot_t90",
        "ienable3DPlot",
        "ienableMonoStaticPlot",
        "ienableMonoStaticRCSPlot",
        "ienableBiObjRotPlot"
    ]

    # Create radio buttons for each option
    for option in options:
        radio_button = ttk.Radiobutton(radio_frame, text=option, variable=radio_vars[option],
                                       value=1, command=lambda opt=option: update_vars(radio_vars[opt], radio_vars))
        radio_button.grid(row=options.index(option), column=0, sticky="w")

    return radio_frame, radio_vars
