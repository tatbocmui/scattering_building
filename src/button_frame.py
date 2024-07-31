from tkinter import ttk
from tkinter import filedialog
import json
from window_frame_manager import update_window_frames  # Ensure this import is correct
import json_manager as jm
import display_frame as df
import excute_calculation as ec
def create_button_frame(parent, input_vars, check_vars, radio_vars, drawing_vars, directory_vars, num_windows_var, window_vars_list, mother_window_frame, mother_display_frame, canvas):
    button_frame = ttk.Frame(parent, padding="10 10 10 10")
    
    buttons = [
        ("Load JSON", lambda: jm.load_json(input_vars, check_vars, radio_vars, drawing_vars, directory_vars,num_windows_var, window_vars_list)),
        ("Draw Object", lambda: df.draw_object(input_vars, check_vars, radio_vars, drawing_vars, directory_vars, num_windows_var, window_vars_list, mother_display_frame)),
        ("Save Json", lambda: jm.save_json(input_vars, check_vars, radio_vars, drawing_vars, directory_vars,num_windows_var, window_vars_list)),
        ("Execute Calculation", lambda: ec.start_process_thread(input_vars, check_vars, radio_vars, drawing_vars, directory_vars,num_windows_var, window_vars_list))
    ]
    
    for i, (text, command) in enumerate(buttons):
        button = ttk.Button(button_frame, text=text, command=command)
        button.grid(row=i, column=0, pady=5)
    
    return button_frame
