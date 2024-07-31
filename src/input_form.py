import tkinter as tk
from tkinter import ttk

def validate_number(P):
    if P.isdigit() or P == "":
        return True
    try:
        float(P)
        return True
    except ValueError:
        return False

def create_input_form(parent):
    input_frame = ttk.Frame(parent, padding="10 10 10 10")
    # input_frame.grid(row=0, column=0, sticky="nw")

    # Standardized list of input labels with empty default values if you want consistency
    labels = [
        ("tpw - aE_TM:", ""),
        ("tpw - af:", ""),
        ("tpw - atheta0:", ""),
        ("tpw - aphi0:", ""),
        ("tplate - aLx:", ""),
        ("tplate - aLy:", ""),
        ("tplate - aLz:", ""),
        ("iNumberWindows:", "2")
    ]

    # Dictionary to hold the variables associated with each input
    input_vars = {}

    # Register validation command
    vcmd = (parent.register(validate_number), '%P')

    # Create labels and entry widgets for the inputs
    for i, (label_text, default_value) in enumerate(labels):
        label = ttk.Label(input_frame, text=label_text)
        label.grid(row=i, column=0, sticky="w")
        var = tk.StringVar(value=default_value)  # Initialize with empty string for each input
        input_vars[label_text] = var  # Store the variable with label as key
        entry = ttk.Entry(input_frame, width=20, textvariable=var, validate='key', validatecommand=vcmd)
        entry.grid(row=i, column=1, sticky="w")

    return input_frame, input_vars
