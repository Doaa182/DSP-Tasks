import pandas as pd
import numpy as np
import math

from CompareSignals7 import ConvTest

###############################################################################
def read_txt_file(path):
    with open(path, "r") as f:
        file_lines = f.readlines()[3:]  
    return file_lines

###############################################################################
sgnl1_input = read_txt_file("Task 7 & 9 Test Cases\input_conv_sig1.txt")
sgnl1_input_df = pd.DataFrame(sgnl1_input)
sgnl1_input_df[['indx', 'sgnl']] = sgnl1_input_df[0].str.strip().str.split(' ', n=1, expand=True)
sgnl1_input_df['indx'] = sgnl1_input_df['indx'].astype(float)
sgnl1_input_df['sgnl'] = sgnl1_input_df['sgnl'].astype(float)

sgnl2_input = read_txt_file("Task 7 & 9 Test Cases\input_conv_sig2.txt")
sgnl2_input_df = pd.DataFrame(sgnl2_input)
sgnl2_input_df[['indx', 'sgnl']] = sgnl2_input_df[0].str.strip().str.split(' ', n=1, expand=True)
sgnl2_input_df['indx'] = sgnl2_input_df['indx'].astype(float)
sgnl2_input_df['sgnl'] = sgnl2_input_df['sgnl'].astype(float)

###############################################################################
sgnl1_input_df2 = pd.DataFrame()
sgnl2_input_df2 = pd.DataFrame()
length_diff = len(sgnl1_input_df) + len(sgnl2_input_df) - 1

# Pad the 'indx' column in both dataframes
sgnl1_input_df2['indx_pad'] = np.arange(sgnl1_input_df['indx'].min(), sgnl1_input_df['indx'].min() + length_diff)
sgnl2_input_df2['indx_pad'] = np.arange(sgnl2_input_df['indx'].min(), sgnl2_input_df['indx'].min() + length_diff)

# Pad the 'sgnl' column in both dataframes with zeros
sgnl1_input_df2['sgnl_pad'] = np.concatenate([sgnl1_input_df['sgnl'], np.zeros(length_diff - len(sgnl1_input_df))])
sgnl2_input_df2['sgnl_pad'] = np.concatenate([sgnl2_input_df['sgnl'], np.zeros(length_diff - len(sgnl2_input_df))])

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

            angle=2 *  np.pi   * Hth * sgnl_no / len(df[col_name])
            rule_r= math.cos(angle)
            rule_i = sign*math.sin(angle)
            
            rule=complex(rule_r,rule_i)
            mul=np.dot(sgnl, rule)/dinomenator

            term.append(mul)  
            summation=sum(term)
            
        harmonic_lst.append(summation)   
        real_lst.append(summation.real)  
        img_lst.append(summation.imag)     

    return harmonic_lst,real_lst,img_lst


###############################################################################   
def Run_Fast_Convolution():
    sgnl1_DFT_output,_,_=DFT_IDFT(sgnl1_input_df2,"sgnl_pad",-1,1)
    
    sgnl2_DFT_output,_,_=DFT_IDFT(sgnl2_input_df2,"sgnl_pad",-1,1)
    
    ###############################################################################
    multiplication = list(map(lambda x, y: x * y, sgnl1_DFT_output, sgnl2_DFT_output))
    
    ###############################################################################
    multiplication_df = pd.DataFrame(multiplication)
    y,_,_=DFT_IDFT(multiplication_df,0,1,len(multiplication_df))
    _,y_real,_=DFT_IDFT(multiplication_df,0,1,len(multiplication_df))
    
    ###############################################################################
    y_real = [round(value) for value in y_real]
    
    ###############################################################################
    ConvTest(sgnl1_input_df2['indx_pad'],y_real)











