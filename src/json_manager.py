import json
from tkinter import filedialog
from tkinter import filedialog, messagebox
import data_manager as dm

def load_json(input_vars, check_vars, radio_vars, drawing_vars, directory_vars,num_windows_var,window_vars_list):
    file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if not file_path:
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error reading JSON file: {e}")
        return
    
    # Update input fields
    # Mapping of input_vars keys to JSON paths
    key_mapping = {
        "tpw - aE_TM:": ("tpw", "aE_TM"),
        "tpw - af:": ("tpw", "af"),
        "tpw - atheta0:": ("tpw", "atheta0"),
        "tpw - aphi0:": ("tpw", "aphi0"),
        "tplate - aLx:": ("tplate", "aLx"),
        "tplate - aLy:": ("tplate", "aLy"),
        "tplate - aLz:": ("tplate", "aLz"),
        "iNumberWindows:": (None, "iNumberWindows")  # No parent key for iNumberWindows
    }

    for key, (parent_key, json_key) in key_mapping.items():
        if key in input_vars:
            # Retrieve the value from nested dictionaries if parent_key is provided
            json_value = data.get(parent_key, {}).get(json_key, "") if parent_key else data.get(json_key, "")
            input_vars[key].set(json_value)
    
    # Update check option fields
    for key, var in check_vars.items():
        var.set(data.get(key, 0))
    
    # Update radio option fields
    for key, var in radio_vars.items():
        var.set(data.get(key, 0))
    
    # Update drawing option fields
    for key, var in drawing_vars.items():
        var.set(data.get(key, ""))

    # Update directory fields
    for key, var in directory_vars.items():
        var.set(data.get(key, ""))
    
    # Update window frame values
    tholes_data = data.get("tholes", [])
    tglass_data = data.get("tglass", [])

    for index, window_vars in enumerate(window_vars_list):
        if index < len(tholes_data):
            # Update values from tholes_data
            for key in ['aa', 'ab', 'ac', 'positionHole', 'adx', 'ady', 'adz']:
                if key in window_vars:
                    window_vars[key].set(tholes_data[index].get(key, ""))

        if index < len(tglass_data):
            # Update values from tglass_data
            for key in ['ac1', 'aGlassThickness', 'avarepsilon_rr', 'avarepsilon_ri']:
                if key in window_vars:
                    window_vars[key].set(tglass_data[index].get(key, ""))

def save_json(input_vars, check_vars, radio_vars, drawing_vars, directory_vars,window_vars_list, num_windows_var):
    data=dm.data_create(input_vars, check_vars, radio_vars, drawing_vars, directory_vars,window_vars_list, num_windows_var)
    # Lưu dữ liệu vào tệp JSON
    try:
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if file_path:
            with open(file_path, "w", encoding='utf-8') as json_file:
                json.dump(data, json_file, indent=4, ensure_ascii=False)
        messagebox.showinfo("Save Status", "Save Successful")
    except Exception as e:
        messagebox.showerror("Save Status", f"Save Failed: {str(e)}")