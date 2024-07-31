import tkinter as tk
from tkinter import font
def create_instruction_frame(parent):
    instruction_frame = ttk.Frame(parent, padding="10 10 10 10")
    custom_font = font.Font(size=12)
    instruction_label = tk.Label(instruction_frame, text="1) Click Load Json (Only one when begin)",\
    anchor="w", justify="left", wraplength=300, font=custom_font)
    instruction_label.grid(row=2, column=9, padx=10, pady=10)
    instruction_label = tk.Label(instruction_frame, text="2) Modify Input and click draw object",\
    anchor="w", justify="left", wraplength=300, font=custom_font)
    instruction_label.grid(row=3, column=9, padx=10, pady=10)
    instruction_label = tk.Label(instruction_frame, text="3) Save json",\
    anchor="w", justify="left", wraplength=300, font=custom_font)
    instruction_label.grid(row=4, column=9, padx=10, pady=10)
    instruction_label = tk.Label(instruction_frame, text="4) Click Execute to run",\
    anchor="w", justify="left", wraplength=300, font=custom_font)
    instruction_label.grid(row=5, column=9, padx=10, pady=10)
    instruction_label = tk.Label(instruction_frame, text="Repeat 2, 3 and 4 to run",\
    anchor="w", justify="left", wraplength=300, font=custom_font)
    instruction_label.grid(row=6, column=9, padx=10, pady=10)

def create_instruction_label(frame, text, row, column, wraplength=300):
    instructions = [
            ("1) Click Load Json (Only one when begin)", 2),
            ("2) Modify Input and click draw object", 3),
            ("3) Save json", 4),
            ("4) Click Execute to run", 5),
            ("Repeat 2, 3 and 4 to run", 6),
        ]
    custom_font = font.Font(size=12)  # Define the custom font inside the function if it doesn't change
    instruction_label = tk.Label(frame, text=text,
                                 anchor="w", justify="left",
                                 wraplength=wraplength, font=custom_font)
    instruction_label.grid(row=row, column=column, padx=10, pady=10)
    for text, row in instructions:
        create_instruction_label(frame, text, row, 9)    
        
