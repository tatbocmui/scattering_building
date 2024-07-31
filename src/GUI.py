import tkinter as tk
import display_frame as df
from tkinter import ttk
from input_form import create_input_form
from check_option_frame import create_check_option_frame
from radio_option_frame import create_radio_option_frame
from drawing_options_frame import create_drawing_options_frame
from directory_options_frame import create_directory_options_frame
from window_frame_manager import create_child_window_frame
from button_frame import create_button_frame

def main():
    root = tk.Tk()
    root.title("Scalable GUI with 3D Graphics")
    root.state('zoomed')
 
     # Head frame setup
    head_frame = tk.Frame(root, pady=10)
    head_frame.grid(row=0, column=0, columnspan=2, sticky='ew')

    # Subframes inside head frame
    planewave_frame, input_vars = create_input_form(head_frame)
    planewave_frame.grid(row=0, column=0, padx=5)

    check_frame, check_vars = create_check_option_frame(head_frame)
    check_frame.grid(row=0, column=1, padx=5)

    radio_frame, radio_vars = create_radio_option_frame(head_frame)
    radio_frame.grid(row=0, column=2, padx=5)

    drawing_result_frame, drawing_vars = create_drawing_options_frame(head_frame)
    drawing_result_frame.grid(row=0, column=3, padx=5)

    # Directory frame below head frame
    directory_frame, directory_vars = create_directory_options_frame(root)
    directory_frame.grid(row=1, column=0, columnspan=4, sticky='ew', pady=10)

    # Window frame with scrollbar
    window_frame = ttk.Frame(root, borderwidth=4, relief='solid')
    window_frame.grid(row=2, column=0, sticky="nsew")

    # Create a canvas inside the window frame. This canvas will be scrollable
    # and will contain the scrollable frame.
    canvas = tk.Canvas(window_frame)
    
    # Create a scrollbar and associate it with the canvas. The scrollbar
    # will control the scrolling of the canvas.
    scrollbar = ttk.Scrollbar(window_frame, orient='vertical', command=canvas.yview)
    
    # Configure the canvas so that it scrolls when the associated scrollbar
    # is moved.
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Create a frame to contain the scrollable content.
    scrollable_frame = tk.Frame(canvas)
    
    # Add the scrollable frame to the canvas. The anchor is set to 'nw' so
    # that the top-left corner of the frame is positioned at (0,0) of the
    # canvas.
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    
    # Bind the 'Configure' event of the scrollable frame to a lambda function
    # that updates the scroll region of the canvas. This event is triggered
    # when the size of the scrollable frame changes.
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )


    # Create an empty list to store variables for each window
    window_vars_list = []

    # Set the maximum number of window frames to 100
    max_window_frames = 100

    # Loop through each window frame
    for i in range(max_window_frames):
        
        # Create a child frame for each window frame
        child_frame, vars_dict = create_child_window_frame(scrollable_frame, i)
        
        # Store the variables for each window in the window_vars_list
        window_vars_list.append(vars_dict)

    # Pack the canvas on the left side of the window frame
    canvas.pack(side="left", fill="both", expand=True)
    
    # Pack the scrollbar on the right side of the window frame
    scrollbar.pack(side="right", fill="y")
    

    # Display frame next to window frame
    display_frame = df.create_display_frame(root)
    display_frame.grid(row=2, column=1, sticky='nsew')

    num_windows_var=input_vars["iNumberWindows:"]
    button_frame = create_button_frame(head_frame, input_vars, check_vars, radio_vars, drawing_vars, directory_vars, num_windows_var, window_vars_list, window_frame, display_frame, canvas)
    button_frame.grid(row=0, column=4, padx=5)

    # Configuring the grid behavior
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1, uniform="group1")
    root.grid_columnconfigure(1, weight=1, uniform="group1")

    root.mainloop()

if __name__ == "__main__":
    main()
