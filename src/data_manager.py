
def data_create(input_vars, check_vars, radio_vars, drawing_vars, directory_vars,num_windows_var,window_vars_list):
    data= dict()
    tpw = dict()
    tplate = dict()
    tholes = list()
    tglass = list()

    try:
        tpw["aE_TM"] = float(input_vars["tpw - aE_TM:"].get())
        tpw["af"] = float(input_vars["tpw - af:"].get())
        tpw["atheta0"] = float(input_vars["tpw - atheta0:"].get())
        tpw["aphi0"] = float(input_vars["tpw - aphi0:"].get())
        data["tpw"] = tpw
        tplate["aLx"] = float(input_vars["tplate - aLx:"].get())
        tplate["aLy"] = float(input_vars["tplate - aLy:"].get())
        tplate["aLz"] = float(input_vars["tplate - aLz:"].get())
        data["tplate"] = tplate
        data["iNumberWindows"] = int(num_windows_var.get())
    except (TypeError, ValueError, KeyError) as e:
        print(f"Error in data_create(): {e}")
    for i in range(data['iNumberWindows']):
        window_vars=window_vars_list[i]
        thole=dict()
        tg=dict()
        for key in ['aa', 'ab', 'ac', 'adx', 'ady', 'adz']:
            if key in window_vars:
                try:
                    thole[key] = float(window_vars[key].get())
                except (TypeError, ValueError):
                    print(f"Error converting {window_vars[key].get()} to float in draw_object() function.")
        if 'positionHole' in window_vars:
            thole["positionHole"] = window_vars['positionHole'].get()  # Assuming holes_position is indexed similarly
        tholes.append(thole)
        for key in ['ac1', 'aGlassThickness', 'avarepsilon_rr', 'avarepsilon_ri']:
            if key in window_vars:
                tg[key]=float(window_vars[key].get())
        tglass.append(tg)
    data["tholes"]=tholes
    data["tglass"]=tglass

    # Update drawing option fields
    for key, var in drawing_vars.items():
        if key in ["ibonusFrEvMod", "ibonusSlEvMod"]:
            data[key]=int(var.get())
        else:
            data[key]=float(var.get())

    # Update check option fields
    for key, var in check_vars.items():
        data[key]=var.get()
    
    # Update radio option fields
    for key, var in radio_vars.items():
        data[key]=var.get()
    
    # Update directory fields
    for key, var in directory_vars.items():
        data[key]=var.get()

    return data
