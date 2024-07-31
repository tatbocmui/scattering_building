import datetime
import subprocess
import threading
import data_manager as dm
def excute_calculation(input_vars, check_vars, radio_vars, drawing_vars, directory_vars,num_windows_var,window_vars_list):
    start_time  = datetime.datetime.now()
    current_time = start_time .strftime("%H:%M:%S")
    print("Start Time =", current_time)
    argument_list=create_argument_list(input_vars, check_vars, radio_vars, drawing_vars, directory_vars,num_windows_var, window_vars_list)
    argument = convert_list_to_string(argument_list)
    cmd_command = f'start cmd /k {argument}'# Lệnh để mở cửa sổ cmd riêng và thực thi lệnh
    process = subprocess.Popen(cmd_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Đợi quá trình kết thúc và nhận đầu ra và lỗi từ quá trình
    stdout, stderr = process.communicate()
    # Đọc đầu ra và lỗi từ quá trình
    end_time = datetime.datetime.now()
    current_time = end_time.strftime("%H:%M:%S")
    print("Finish Time =", current_time)
    print("--- %s seconds ---" % (end_time - start_time))

def start_process_thread(input_vars, check_vars, radio_vars, drawing_vars, directory_vars,num_windows_var, window_vars_list):
    # Tạo một thread mới để thực thi quá trình dài
    thread = threading.Thread(target=excute_calculation(input_vars, check_vars, radio_vars, drawing_vars, directory_vars,num_windows_var, window_vars_list))
    thread.start()

def create_argument_list(input_vars, check_vars, radio_vars, drawing_vars, directory_vars,num_windows_var, window_vars_list):
    
    data=dm.data_create(input_vars, check_vars, radio_vars, drawing_vars, directory_vars,num_windows_var, window_vars_list)
    #Create a list of input variable
    listInput = []
    listInput.extend((data["tpw"]["aE_TM"], data["tpw"]["af"], data["tpw"]["atheta0"],\
                    data["tpw"]["aphi0"], data["tplate"]["aLx"], data["tplate"]["aLy"],
                      data["tplate"]["aLz"], data["iNumberWindows"]))
    #Handle case with 0 hole
    if (data["iNumberWindows"] > 0):
        for i in range(data["iNumberWindows"]):
            #Get value of each hole
            all_values = [value for value in data["tholes"][i].values()]
            listInput.extend(all_values)
            #Assign glass to each hole
            all_values = [value for value in data["tglass"][i].values()]
            listInput.extend(all_values)
    listInput.extend((data["ibonusFrEvMod"], data["ibonusSlEvMod"], data["aphiStep"], data["athetaStep"], data["athetaOP"],data["aDeltaAnglePhi0Phi"],\
                        data["iwriteFile"], data["ienable2DPlot"],\
                        data["ienablePolarPlot"], data["ienableFinitePlate"], data["ienableTEPol"],\
                        data["ienableSlabEvMode"], data["ienable3DPlot"],\
                        data["ienablePOCalculation"],data["ienable2DPlot_t90"],data["ienableMonoStaticPlot"],\
                        data["ienableMonoStaticRCSPlot"],data["ienableBiObjRotPlot"],\
                        data["directoryPath"],data["historyFolderPath"]))

    #convert to string
    string_list = list(map(str, listInput))
    
    argument_list = [".\\multiple_windows.exe"]
    argument_list.extend(string_list)
    return argument_list

def convert_list_to_string(string_list):
    return ' '.join(string_list)
