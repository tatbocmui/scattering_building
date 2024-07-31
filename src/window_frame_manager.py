import tkinter as tk
from tkinter import ttk

import tkinter as tk
from tkinter import ttk

def create_mother_window_frame(parent, num_windows_var):
    # Create the mother frame
    mother_frame = ttk.Frame(parent, padding="10 10 10 10")
    # mother_frame.grid(row=2, column=0, sticky="nw")
    
    # Dictionary to hold all window variables for potential future updates via JSON
    window_vars_list = []
    max_window_frames= 100
    # Generate child windows
    for i in range(max_window_frames):
        child_frame, vars_dict = create_child_window_frame(mother_frame, i)
        window_vars_list.append(vars_dict)  # Store variables for each window
    return mother_frame, window_vars_list

def create_child_window_frame(parent, window_index):
    # Calculate the grid placement based on the window index
    child_frame = ttk.Frame(parent, padding="10 10 10 10", borderwidth=1, relief='solid')
    row = window_index // 3
    column = window_index % 3
    child_frame.grid(row=row, column=column, sticky="ew", padx=5, pady=5)
    child_frame.grid(row=row, column=column, sticky="ew", padx=5, pady=5)
    
    # Define labels for each window
    hole_labels = [
        "aa", "ab", "ac", "positionHole", "adx", "ady", "adz"
    ]
    glass_labels = [
        "ac1", "aGlassThickness", "avarepsilon_rr", "avarepsilon_ri"
    ]

    window_vars = {}

    # Create labels and entries for hole variables
    for i, label_key in enumerate(hole_labels):
        label_text = f"Hole {window_index + 1} - {label_key}:"
        label = ttk.Label(child_frame, text=label_text)
        label.grid(row=i, column=0, sticky="w")
        var = tk.StringVar(value="")
        window_vars[label_key] = var  # Using JSON keys directly as dictionary keys
        entry = ttk.Entry(child_frame, width=20, textvariable=var)
        entry.grid(row=i, column=1, sticky="w")

    # Create labels and entries for glass variables
    for j, label_key in enumerate(glass_labels):
        label_text = f"Glass {window_index + 1} - {label_key}:"
        label = ttk.Label(child_frame, text=label_text)
        label.grid(row=len(hole_labels) + j, column=0, sticky="w")
        var = tk.StringVar(value="")
        window_vars[label_key] = var  # Using JSON keys directly as dictionary keys
        entry = ttk.Entry(child_frame, width=20, textvariable=var)
        entry.grid(row=len(hole_labels) + j, column=1, sticky="w")

    return child_frame, window_vars


def update_window_frames(mother_frame, num_windows_var, canvas):
    # Try to parse the number of windows safely
    try:
        num_windows = int(num_windows_var.get())
    except ValueError:
        num_windows = 0  # Default to 0 if conversion fails

    current_frames = mother_frame.winfo_children()

    # Calculate the difference between current frames and desired number of windows
    difference = num_windows - len(current_frames)

    if difference > 0:
        # More frames are needed, add the additional frames
        for i in range(len(current_frames), num_windows):
            create_child_window_frame(mother_frame, i)
    elif difference < 0:
        # Less frames are needed, remove the surplus frames
        for frame in current_frames[num_windows:]:
            frame.destroy()

    # Update the scroll region to accommodate the new or existing frames
    mother_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))


