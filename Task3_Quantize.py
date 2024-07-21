import pandas as pd
import re
import math
from CompareSignals3_1 import QuantizationTest1
from CompareSignals3_2 import QuantizationTest2
import matplotlib.pyplot as plt
import tkinter as tk

# import numpy as np
# from tkinter import filedialog
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from tkinter import * 

###############################################################################
def read_txt_file(path):
    with open(path, "r") as f:
        file_lines = f.readlines()[3:]  
    return file_lines

###############################################################################
Quan1_input = read_txt_file("Task 3 Test Cases\Test 1\Quan1_input.txt")
Quan2_input = read_txt_file("Task 3 Test Cases\Test 2\Quan2_input.txt")

Quan1_input_df = pd.DataFrame(Quan1_input)
Quan2_input_df = pd.DataFrame(Quan2_input)

Quan1_input_df[['Indx', 'Sgnl']] = Quan1_input_df[0].str.split(' ', expand=True)
Quan2_input_df[['Indx', 'Sgnl']] = Quan2_input_df[0].str.split(' ', expand=True)

Quan1_input_df['Sgnl'] = Quan1_input_df['Sgnl'].astype(float)
Quan2_input_df['Sgnl'] = Quan2_input_df['Sgnl'].astype(float)

###############################################################################
def get_min(df):
    m=float(df['Sgnl'].min())
    return m

def get_max(df):
    m=float(df['Sgnl'].max())
    return m

minimum1=get_min(Quan1_input_df)
minimum2=get_min(Quan2_input_df)

maximum1=get_max(Quan1_input_df)
maximum2=get_max(Quan2_input_df)

###############################################################################
def get_lvl_or_bts(path, para_name):
    with open(path, "r") as f:
        content = f.read()

    pattern = r"{} = (\d+)".format(para_name)
    match = re.search(pattern, content)

    if match:
        parameter_value = match.group(1)
        if para_name=="Number of levels":
            return int(parameter_value)
        elif para_name=="Number of bits":
            return 2**(int(parameter_value))
    else:
        return None
###############################################################################
def get_input():

    lvl_or_bts1 = 2**(int(entry1.get()))
    lvl_or_bts2 = int(entry2.get()) 

    window.destroy()

###############################################################################
    # lvl_or_bts1= get_lvl_or_bts("TestCases Inputs.txt", "Number of bits")
    # lvl_or_bts2= get_lvl_or_bts("TestCases Inputs.txt", "Number of levels")
    
    ###############################################################################
    def get_delta(maxi,mini,lvl):
        d=(maxi-mini)/lvl
        d = round(d, 2)
        return d
    
    delta1=get_delta(maximum1,minimum1,lvl_or_bts1)
    delta2=get_delta(maximum2,minimum2,lvl_or_bts2)
    
    ###############################################################################
    def intervals(mini,dlta,lvl):
        intrvls_lst=[]
        lvl_no=0
        z=mini
        for _ in range(lvl):
            intrvls_lst.append([z, (z + dlta),lvl_no,((z+ (z + dlta))/2),0])
            z = z + dlta
            lvl_no = lvl_no+1
            intrvls_lst[-1][1] = intrvls_lst[-1][1] + 0.01  
        intrvls_df = pd.DataFrame(intrvls_lst, columns=["z", "z+d","level no.","midpoint","error"])
        return intrvls_df
    
    
    intervals_df1= intervals(minimum1,delta1,lvl_or_bts1)
    intervals_df2= intervals(minimum2,delta2,lvl_or_bts2)
    
    ###############################################################################
    def interval_no1(df1, df2, column_name1, column_name2, column_name22,column_name222,column_name2222,column_name22222,lvls):
        interval_no_lst = []
        bits=int(math.log(lvls,2))
        for value in df1[column_name1]:
            for _,row in df2.iterrows():
                    if row[column_name2] <= value <= row[column_name22] :
                        interval_no_lst.append([row[column_name222], row[column_name2222]])
                        break
    
        intrvls_df = pd.DataFrame(interval_no_lst, columns=["level no.","midpoint"]) 
        intrvls_df["level no."] = intrvls_df[column_name222].astype(int).apply(lambda x: bin(x)[2:].zfill(bits))
        return intrvls_df
    
    
    def interval_no2(df1, df2, column_name1, column_name2, column_name22,column_name222,column_name2222,column_name22222,lvls):
        interval_no_lst = []
        bits=int(math.log(lvls,2))
        for value in df1[column_name1]:
            for _,row in df2.iterrows():
                if row[column_name2] <= value <= row[column_name22] :
                      row[column_name22222]=row[column_name2222]-value
                      interval_no_lst.append([(row[column_name222]+1),0,row[column_name222],row[column_name2222],row[column_name22222]])
                      break
                
        intrvls_df = pd.DataFrame(interval_no_lst, columns=["dec. level no.","bin. level no.","dec. level no.-1","midpoint","error"])
        intrvls_df["bin. level no."] = intrvls_df["dec. level no.-1"].astype(int).apply(lambda x: bin(x)[2:].zfill(bits))
        intrvls_df=intrvls_df.drop(["dec. level no.-1"], axis=1)
        return intrvls_df
    
    
    df1_out=interval_no1(Quan1_input_df,intervals_df1,"Sgnl","z", "z+d","level no.","midpoint","error",lvl_or_bts1)
    df2_out=interval_no2(Quan2_input_df,intervals_df2,"Sgnl","z", "z+d","level no.","midpoint","error",lvl_or_bts2)
    ###############################################################################
    QuantizationTest1("Task 3 Test Cases\Test 1\Quan1_Out.txt",df1_out["level no."],df1_out["midpoint"])
    QuantizationTest2("Task 3 Test Cases\Test 2\Quan2_Out.txt",df2_out["dec. level no."],df2_out["bin. level no."],df2_out["midpoint"],df2_out["error"])
    
    ###############################################################################
    def display_quantization(df1, df2):
        plt.figure(figsize=(10, 6))
        plt.scatter(df1['Indx'], df1['Sgnl'], color='blue', label='Original Signal')
        def binary_to_decimal(binary):
            return int(binary, 2)
        
        df2['dec. level no.'] = df2['level no.'].apply(binary_to_decimal)
        plt.scatter(df2['dec. level no.'], df2['midpoint'], color='red', label='Quantized Signal')
        plt.xlabel('Index')
        plt.ylabel('Signal Value')
        plt.title('Quantized Signal vs Original Signal')
        plt.legend()
        plt.show()
        
    ###############################################################################
    def display_quantization2(df1, df2):
        plt.figure(figsize=(10, 6))
        plt.scatter(df1['Indx'], df1['Sgnl'], color='blue', label='Original Signal')
        plt.scatter(df2["dec. level no."], df2['midpoint'], color='red', label='Quantized Signal')
        plt.xlabel('Index')
        plt.ylabel('Signal Value & Quantization Error')
        plt.title('Quantized Signal vs Original Signal & Quantization Error')
        # plt.show()
    
        # plt.figure(figsize=(10, 4))
        plt.scatter(df1['Indx'], df2['error'], color='green',label='Error')
        # plt.xlabel('Index')
        # plt.ylabel('Quantization Error')
        # plt.title('Quantization Error')
        plt.legend()
        plt.show()
    ###############################################################################
    display_quantization(Quan1_input_df, df1_out)
    display_quantization2(Quan2_input_df, df2_out)

###############################################################################

window = tk.Tk()

def Run_Quantize():
    label1 = tk.Label(window, text="Enter the number of levels for Quan1:")
    label1.pack()
    
    label2 = tk.Label(window, text="Enter the number of bits for Quan2:")
    label2.pack()
    
    global entry1
    entry1 = tk.Entry(window)
    entry1.pack()
    
    global entry2
    entry2 = tk.Entry(window)
    entry2.pack()
    
    button = tk.Button(window, text="Submit", command=get_input)
    button.pack()
    
    window.mainloop()


#Run_Quantize()















