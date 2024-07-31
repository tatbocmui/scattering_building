import tkinter as tk
from tkinter import ttk

# Function to validate numerical input
def validate_number(P):
    if P.isdigit() or P == "":
        return True
    try:
        float(P)
        return True
    except ValueError:
        return False

def create_drawing_options_frame(parent):
    # Create a container frame for drawing options
    drawing_frame = ttk.Frame(parent, padding="10 10 10 10")
    # drawing_frame.grid(row=2, column=0, columnspan=4, sticky="nw")

    # List of drawing option labels for display and keys for dictionary
    options = [
        ("ibonusFrEvMod", ""),
        ("ibonusSlEvMod", ""),
        ("aphiStep", ""),
        ("athetaStep", ""),
        ("athetaOP", ""),
        ("aDeltaAnglePhi0Phi", "")
    ]

    # Dictionary to hold the variables associated with each input
    drawing_vars = {}

    # Register validation command
    vcmd = (parent.register(validate_number), '%P')

    # Create labels and entry widgets for the inputs
    for i, (key, default_value) in enumerate(options):
        label_text = key + ":"  # Add colon for display purposes
        label = ttk.Label(drawing_frame, text=label_text)
        label.grid(row=i, column=0, sticky="w")
        var = tk.StringVar(value=default_value)  # Initialize with empty string for each input
        drawing_vars[key] = var  # Store the variable with key as key, without colon
        entry = ttk.Entry(drawing_frame, width=20, textvariable=var, validate='key', validatecommand=vcmd)
        entry.grid(row=i, column=1, sticky="w")

    return drawing_frame, drawing_vars
