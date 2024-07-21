import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

from CompareSignals5 import SignalSamplesAreEqual

def read_txt_file(path):
    with open(path, "r") as f:
        file_lines = f.readlines()[3:]  
    return file_lines

###############################################################################
def plot_signal(x_values, y_values, x_label,y_label,title):

    plt.plot(x_values, y_values)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    plt.show()
    
###############################################################################
def get_phase_shift_rad(r, img):
    return f"{(np.angle(complex(r, img), deg=True))*(np.pi/180):.14f}f" 

def get_phase_shift_rad2(r, img):
    return np.angle(complex(r, img), deg=True)*(np.pi/180)

###############################################################################
def get_amp_phase(lst1,lst2):
    amp_phase_df = pd.DataFrame(
        {'r': lst1,
          'img': lst2
        })
    
    amp_phase_df['Amplitude'] = amp_phase_df.apply(lambda row: math.sqrt(row['r'] ** 2 + row['img'] ** 2), axis=1)
    # amp_phase_df['Amplitude 13f'] = amp_phase_df.apply(lambda row:  f"{math.sqrt(row['r'] ** 2 + row['img'] ** 2):.13f}f", axis=1)

    # amp_phase_df['Phase Shift'] = amp_phase_df.apply(lambda row:math.degrees(math.atan(row['img'] / row['r'])), axis=1)
    # # amp_phase_df['Phase Shift rad'] = amp_phase_df.apply(lambda row:math.atan(row['img'] / row['r']), axis=1)
    # amp_phase_df['Phase Shift rad'] = amp_phase_df.apply(lambda row: get_phase_shift_rad(row['r'], row['img']), axis=1)
        
    amp_phase_df['Phase Shift rad2'] = amp_phase_df.apply(lambda row: get_phase_shift_rad2(row['r'], row['img']), axis=1)
       
    
    # amp_phase_df['real Phase Shift'] = amp_phase_df.apply(lambda row: 
    # abs(math.degrees(math.atan(row['img'] / row['r']))) if row['r'] >= 0 and row['img'] >= 0 else
    # 180 - abs(math.degrees(math.atan(row['img'] / row['r']))) if row['r'] <= 0 and row['img'] >= 0 else
    # 180 + abs(math.degrees(math.atan(row['img'] / row['r']))) if row['r'] <= 0 and row['img'] <= 0 else
    # 360 - abs(math.degrees(math.atan(row['img'] / row['r']))) if row['r'] >= 0 and row['img'] <= 0 else
    # None, axis=1)

    return amp_phase_df
###############################################################################
DC_input = read_txt_file("Task 5 Test Cases\Remove DC component\DC_component_input.txt")
DC_input_df = pd.DataFrame(DC_input)
DC_input_df[['Indx', 'Sgnl']] = DC_input_df[0].str.split(' ', expand=True)
DC_input_df['Sgnl'] = DC_input_df['Sgnl'].astype(float)

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

def Run_Dc_Freq_Domain():

    DFT_output,DFT_output_real,DFT_output_img=DFT_IDFT(DC_input_df,"Sgnl",-1,1)
    # DFT_amp_phase=get_amp_phase(DFT_output_real,DFT_output_img)
    
    ###############################################################################
    DFT_output[0]=complex(0, 0)
    DFT_output_df = pd.DataFrame(DFT_output)
    IDFT_output,IDFT_output_real,_=DFT_IDFT(DFT_output_df,0,1,len(DFT_output_df))
    IDFT_output_real = [round(value, 3) for value in IDFT_output_real]


###############################################################################
    SignalSamplesAreEqual('Task 5 Test Cases\Remove DC component\DC_component_output.txt',IDFT_output_real)