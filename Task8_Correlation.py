import pandas as pd
import numpy as np

from CompareSignals8 import Compare_Signals

###############################################################################
def read_txt_file(path):
    with open(path, "r") as f:
        file_lines = f.readlines()[3:]  
    return file_lines

###############################################################################
def Run_Task8_Correlation():
    sgnl1_input = read_txt_file("Task 8 Test Cases\input_corr_sig1.txt")
    sgnl1_input_df = pd.DataFrame(sgnl1_input)
    sgnl1_input_df[['indx', 'sgnl']] = sgnl1_input_df[0].str.strip().str.split(' ', n=1, expand=True)
    sgnl1_input_df['indx'] = sgnl1_input_df['indx'].astype(float)
    sgnl1_input_df['sgnl'] = sgnl1_input_df['sgnl'].astype(float)
    
    sgnl2_input = read_txt_file("Task 8 Test Cases\input_corr_sig2.txt")
    sgnl2_input_df = pd.DataFrame(sgnl2_input)
    sgnl2_input_df[['indx', 'sgnl']] = sgnl2_input_df[0].str.strip().str.split(' ', n=1, expand=True)
    sgnl2_input_df['indx'] = sgnl2_input_df['indx'].astype(float)
    sgnl2_input_df['sgnl'] = sgnl2_input_df['sgnl'].astype(float)
    
    ###############################################################################
    sgnl1_input_df['sgnl_squared']=sgnl1_input_df['sgnl']**2
    sgnl1_squared_sum=np.sum(sgnl1_input_df['sgnl_squared'])
    
    sgnl2_input_df['sgnl_squared']=sgnl2_input_df['sgnl']**2
    sgnl2_squared_sum=np.sum(sgnl2_input_df['sgnl_squared'])
    
    n=len(sgnl1_input_df)
    
    denominator_of_p=(1/n)*np.sqrt(sgnl1_squared_sum * sgnl2_squared_sum)
    
    ###############################################################################
    for i in range(1, n):
        col_name = f'sgnl_shifted_{i}'
        sgnl2_input_df[col_name] = np.roll(sgnl2_input_df['sgnl'], -i) 
    
    ###############################################################################
    result_df = pd.DataFrame()
    sgnl2_input_df2 = sgnl2_input_df.drop(columns=['indx','sgnl_squared',0], inplace=False)
    
    for col in sgnl2_input_df2.columns:
        result_df[col + '_product'] = sgnl1_input_df['sgnl'] * sgnl2_input_df2[col]
        
    sum_of_products = result_df.sum(axis=0).tolist()
    
    ###############################################################################
    r = [x * (1/n) for x in sum_of_products]
    
    p = [x /denominator_of_p for x in r]
    
    ###############################################################################
    Compare_Signals('Task 8 Test Cases\output_corr.txt',sgnl2_input_df['indx'] ,p)
