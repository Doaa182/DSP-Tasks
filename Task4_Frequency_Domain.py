import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import re

from CompareSignals4 import * 

###############################################################################
import tkinter as tk
###############################################################################
def read_txt_file(path):
    with open(path, "r") as f:
        file_lines = f.readlines()[3:]  
    return file_lines

###############################################################################
def sine(a):
    if a  % 180 == 0:
        return 0
    else:
        result = math.sin(a * (np.pi / 180))
        return result
    
###############################################################################   
def cosine(a):
    
    # if  a==0 :
    #      return 1
    if  a % 180 ==0:
        result = math.cos(a * (np.pi / 180))
        return result
    elif  a % ((180 / 2) + (180)) == 0 :
            return 0
    elif a==90:
        return 0
    else:
        result = math.cos(a * (np.pi / 180))
        return result
    
###############################################################################
DFT_input = read_txt_file("Task 4 Test Cases\DFT\input_Signal_DFT.txt")
# DFT_input = read_txt_file("DFT\input_sheet.txt")
DFT_input_df = pd.DataFrame(DFT_input)

DFT_input_df[['Indx', 'Sgnl']] = DFT_input_df[0].str.split(' ', expand=True)
DFT_input_df['Sgnl'] = DFT_input_df['Sgnl'].astype(float)

###############################################################################
IDFT_input = read_txt_file("Task 4 Test Cases\IDFT\Input_Signal_IDFT_A,Phase.txt")
IDFT_input_df = pd.DataFrame(IDFT_input)
IDFT_input_df[['amp', 'phase']] = IDFT_input_df[0].str.split(',', expand=True)

IDFT_input_df['amp'] = IDFT_input_df['amp'].str.replace('f', '').str.replace('\n', '').astype(float)
IDFT_input_df['phase'] = IDFT_input_df['phase'].str.replace('f', '').str.replace('\n', '').astype(float)

IDFT_input_df['amp'] = IDFT_input_df['amp'].apply(lambda x: f"{float(x):.13f}")
IDFT_input_df['phase'] = IDFT_input_df['phase'].apply(lambda x: f"{float(x):.14f}")

# IDFT_input_df['amp'] = IDFT_input_df['amp'] .astype(float)
# IDFT_input_df['phase'] = IDFT_input_df['amp'] .astype(float)

###############################################################################    
def get_phase_shift_rad(r, img):
    return f"{(np.angle(complex(r, img), deg=True))*(np.pi/180):.14f}f"  

###############################################################################
def get_amp_phase(lst1,lst2,fs):
    amp_phase_df = pd.DataFrame(
        {'r': lst1,
          'img': lst2
        })
    
    amp_phase_df['Amplitude'] = amp_phase_df.apply(lambda row: math.sqrt(row['r'] ** 2 + row['img'] ** 2), axis=1)
    amp_phase_df['Amplitude 13f'] = amp_phase_df.apply(lambda row:  f"{math.sqrt(row['r'] ** 2 + row['img'] ** 2):.13f}f", axis=1)

    amp_phase_df['Phase Shift'] = amp_phase_df.apply(lambda row:math.degrees(math.atan(row['img'] / row['r'])), axis=1)
    # amp_phase_df['Phase Shift rad'] = amp_phase_df.apply(lambda row:math.atan(row['img'] / row['r']), axis=1)
    amp_phase_df['Phase Shift rad'] = amp_phase_df.apply(lambda row: get_phase_shift_rad(row['r'], row['img']), axis=1)
    
    
    omega=(2*np.pi)/(len(DFT_input_df['Sgnl'])*(1/fs))
    amp_phase_df['omega'] = omega * (amp_phase_df.index + 1)
    
    amp_phase_df['real Phase Shift'] = amp_phase_df.apply(lambda row: 
    abs(math.degrees(math.atan(row['img'] / row['r']))) if row['r'] >= 0 and row['img'] >= 0 else
    180 - abs(math.degrees(math.atan(row['img'] / row['r']))) if row['r'] <= 0 and row['img'] >= 0 else
    180 + abs(math.degrees(math.atan(row['img'] / row['r']))) if row['r'] <= 0 and row['img'] <= 0 else
    360 - abs(math.degrees(math.atan(row['img'] / row['r']))) if row['r'] >= 0 and row['img'] <= 0 else
    None, axis=1)

    return amp_phase_df
   
###############################################################################
def DFT_IDFT(df,col_name,sign,dinomenator):
    harmonic_lst=[]
    real_lst=[]
    img_lst=[]
    
    for Hth in range(len(df[col_name])):
        sgnl_no = -1
        term=[]
        
        for sgnl in df[col_name]:
            sgnl_no = sgnl_no+1
            
            # angle=2 *  180   * Hth * sgnl_no / len(df[col_name])
            # rule_r= cosine(angle)
            # rule_i = sign*sine(angle)
            
            angle=2 *  np.pi   * Hth * sgnl_no / len(df[col_name])
            rule_r= math.cos(angle)
            rule_i = sign*math.sin(angle)
            
            rule=complex(rule_r,rule_i)
            mul=np.dot(sgnl, rule)/dinomenator
            # mul=sgnl*rule/dinomenator
            
            # print("n = ",sgnl_no)
            # print("k = ",Hth)
            # print("angle = ",angle)
            # print("rule = ",rule)
            # print("rule_r = ",rule_r)
            # print("rule_i = ",rule_i)
            # print("mul = ",mul)
            
    
            term.append(mul)  
            summation=sum(term)
            
        harmonic_lst.append(summation)   
        real_lst.append(summation.real)  
        img_lst.append(summation.imag)     
        # print("sum = ",summation)
        # print("*****************************************************")  

    return harmonic_lst,real_lst,img_lst

###############################################################################   
def read_polar(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        
  
    numeric_values = []
    
    for line in lines:
        numbers = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", line)
        numeric_values.append(numbers)
        
        
        
    numeric_values_df = pd.DataFrame(numeric_values).astype(float)
    
    # amplitudes = numeric_values_df[0].astype(float)
    # angles = numeric_values_df[1].astype(float)
    
    numeric_values_df[0] = numeric_values_df[0].apply(lambda x: f"{x:.13f}f")
    numeric_values_df[1] = numeric_values_df[1].apply(lambda x: f"{x:.14f}f")
    
    numeric_values_df = pd.DataFrame(numeric_values).astype(float)
    
    
    
    complex_numbers = []
    for index, row in numeric_values_df.iterrows():
        amplitude = row[0]
        # print(amplitude)
        
        angle = row[1]
        # print(angle)
    
        # real_part = amplitude * cosine(angle)
        # real_part = amplitude * math.cos(angle*np.pi/180)
        real_part = amplitude * math.cos(angle)
        # print(real_part)
        
        # imag_part = amplitude * sine(angle)
        # imag_part = amplitude * math.sin(angle*np.pi/180)
        imag_part = amplitude * math.sin(angle)
        # print(imag_part)
    
        complex_num = complex(round(real_part), round(imag_part))
        complex_numbers.append(complex_num)
        
    complex_numbers_df = pd.DataFrame(complex_numbers)
    
    _,IDFT_output_real2,_=DFT_IDFT(complex_numbers_df,0,1,len(complex_numbers_df)) 
    IDFT_output2,_,_=DFT_IDFT(complex_numbers_df,0,1,len(complex_numbers_df)) 
    
    IDFT_output_real2 = [round(value) for value in IDFT_output_real2]


    return IDFT_output2

# draw_plot(DFT_amp_phase,"omega","Phase Shift rad")
# after_reading=read_polar('DFT2.txt')
#after_reading2=read_polar('Task 4 Test Cases\IDFT\Input_Signal_IDFT_A,Phase.txt')

###############################################################################
DFT_output,_,_=DFT_IDFT(DFT_input_df,"Sgnl",-1,1)
_,DFT_output_real,_=DFT_IDFT(DFT_input_df,"Sgnl",-1,1)
_,_,DFT_output_img=DFT_IDFT(DFT_input_df,"Sgnl",-1,1)

###############################################################################
DFT_output_df = pd.DataFrame(DFT_output )
IDFT_output,_,_=DFT_IDFT(DFT_output_df,0,1,len(DFT_output_df))
_,IDFT_output_real,_=DFT_IDFT(DFT_output_df,0,1,len(DFT_output_df))

IDFT_output_real = [round(value) for value in IDFT_output_real]

###############################################################################
def to_polar(r, angle):
    return f"{r}*(cos({angle}) + i*sin({angle}))"

###############################################################################
def to_polar2(r, angle):
    r = f"{r:.13f}f"
    angle = f"{angle:.14}f"
    return f"{r} {angle}"

###############################################################################
def draw_plot(df,col1,col2):
    plt.vlines(df[col1], ymin=0, ymax=df[col2], colors='blue', linewidth=1)
    plt.plot(df[col1], df[col2], 'o', color='blue')
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.axhline(y=0, color='red', linewidth=0.5)
    # plt.grid(axis='y')
    plt.show()
    
###############################################################################    
def get_fs():
    fs = float(sample_freq_entry.get())
    return fs

###############################################################################
def get_modify_paramters():
    index=int(index_entry.get())
    a=float(amplitude_entry.get())
    phase=float(theta_entry.get())
    IDFT_input_df['amp'][index]=a
    IDFT_input_df['phase'][index]=phase* (np.pi / 180)
    
###############################################################################   

def Run_DFT():
    fs=get_fs()
    
    DFT_amp_phase=get_amp_phase(DFT_output_real,DFT_output_img,fs)
    polar_forms = [to_polar(r, angle) for r, angle in zip(DFT_amp_phase['Amplitude'], DFT_amp_phase['Phase Shift rad'])]
    polar_forms2 = [to_polar2(r, angle) for r, angle in zip(DFT_amp_phase['Amplitude'], DFT_amp_phase['Phase Shift rad'])]

    with open("Tasks_Write_Files/Task4/DFT.txt", 'w') as file:
        for item in polar_forms:
            file.write("%s  \n" % item)
            
    with open("Tasks_Write_Files/Task4/DFT2.txt", 'w') as file:
        file.write(str(0)+'\n')
        file.write(str(1)+'\n')
        file.write(str(len(DFT_input_df))+'\n')
        for item in polar_forms2:
            file.write("%s  \n" % item)
    draw_plot(DFT_amp_phase,"omega","Amplitude")
    draw_plot(DFT_amp_phase,"omega","Phase Shift")
    #############################
    # SignalComapreAmplitude(IDFT_input_df['amp'] ,DFT_amp_phase['Amplitude'])
    # print(SignalComapreAmplitude(IDFT_input_df['amp'] ,DFT_amp_phase['Amplitude']))
    # SignalComaprePhaseShift(IDFT_input_df['phase'] ,DFT_amp_phase['Phase Shift rad'])
    # print(SignalComaprePhaseShift(IDFT_input_df['phase'] ,DFT_amp_phase['Phase Shift rad']))
    SignalOutput = read_txt_file("Task 4 Test Cases\DFT\Output_Signal_DFT_A,Phase.txt")
    SignalOutput_df = pd.DataFrame(SignalOutput)
    SignalOutput_df[['amp', 'phase']] = SignalOutput_df[0].str.split(' ', n=1, expand=True)
    SignalOutput_df['amp'] = SignalOutput_df['amp'].str.replace('f', '').astype(float)
    SignalOutput_df['phase'] = SignalOutput_df['phase'].str.replace('f', '').astype(float)
    DFT_amp_phase['Phase Shift rad'] = DFT_amp_phase['Phase Shift rad'].str.replace('f', '').astype(float)

    print(SignalComapreAmplitude(SignalInput = DFT_amp_phase['Amplitude'].round(3) ,SignalOutput=SignalOutput_df['amp'].round(3)))
    print(SignalComaprePhaseShift(SignalInput = DFT_amp_phase['Phase Shift rad'].round(3) ,SignalOutput=SignalOutput_df['phase'].round(3)))



###############################################################################
def Run_Frequency_Domain():
    window = tk.Tk()
    window.title('Task4 ')
    window.geometry('400x400')
    
    #############################
    sample_freq_label = tk.Label(window, text='Sample Frequency :')
    sample_freq_label.pack()
    

    global sample_freq_entry
    sample_freq_entry = tk.Entry(window)
    sample_freq_entry.pack()
     
    Fourier_btn=tk.Button(window, text="Fourier transform", command=Run_DFT)
    Fourier_btn.pack()
    
    
    fram=tk.LabelFrame(window, text="Modify signal component")
    fram.pack()
    
    index_label = tk.Label(fram, text='Enter Index :')
    index_label.pack()
    global index_entry
    index_entry = tk.Entry(fram)
    index_entry.pack()
    
    amplitude_label = tk.Label(fram, text='New Amplitude :')
    amplitude_label.pack()
    global amplitude_entry
    amplitude_entry = tk.Entry(fram)
    amplitude_entry.pack()
    
    theta_label = tk.Label(fram, text='New Phase :')
    theta_label.pack()
    global theta_entry
    theta_entry = tk.Entry(fram)
    theta_entry.pack()
    
   
    modify_signal_component_btn=tk.Button(fram, text="Modify Component", command=get_modify_paramters)
    modify_signal_component_btn.pack()

    
    window.mainloop()
    
    
#Run_Frequency_Domain()




















 




