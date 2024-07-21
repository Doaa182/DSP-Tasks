import pandas as pd
import matplotlib.pyplot as plt

from CompareSignals7 import ConvTest

###############################################################################
def read_txt_file(path):
    with open(path, "r") as f:
        file_lines = f.readlines()[3:]  
    return file_lines
def plot_signal(x_values, y_values, x_label,y_label,title):

    plt.plot(x_values, y_values)
    plt.grid()
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    plt.show()  
def get_min(df,col):
    m=int(df[col].min())
    return m

def get_max(df,col):
    m=int(df[col].max())
    return m
###############################################################################
def Run_Convolution():
    sgnl1_input = read_txt_file("Task 7 & 9 Test Cases\input_conv_sig1.txt")
    sgnl1_input_df = pd.DataFrame(sgnl1_input)
    sgnl1_input_df[['n', 'x(n)']] = sgnl1_input_df[0].str.strip().str.split(' ', n=1, expand=True)
    sgnl1_input_df['n'] = sgnl1_input_df['n'].astype(int)
    sgnl1_input_df['x(n)'] = sgnl1_input_df['x(n)'].astype(int)

    sgnl2_input = read_txt_file("Task 7 & 9 Test Cases\input_conv_sig2.txt")
    sgnl2_input_df = pd.DataFrame(sgnl2_input)
    sgnl2_input_df[['n', 'h(n)']] = sgnl2_input_df[0].str.strip().str.split(' ', n=1, expand=True)
    sgnl2_input_df['n'] = sgnl2_input_df['n'].astype(int)
    sgnl2_input_df['h(n)'] = sgnl2_input_df['h(n)'].astype(int)
    
    minimum1=get_min(sgnl1_input_df,'n')
    maximum1=get_max(sgnl1_input_df,'n')

    minimum2=get_min(sgnl2_input_df,'n')
    maximum2=get_max(sgnl2_input_df,'n')

    new_min=minimum1+minimum2
    new_max=maximum1+maximum2
    
    indx=[]
    y=[]
    
    for n in range(new_min, new_max+1):
        indx.append(n)
        term=[]
        
        for k in range(minimum1,maximum2+1):
            # filter df based on col 'n' 
            sgnl1_filtered = sgnl1_input_df[sgnl1_input_df['n'] == k]
            sgnl2_filtered = sgnl2_input_df[sgnl2_input_df['n'] == n-k]
            
            # check filtered df not empty
            if not sgnl1_filtered.empty and not sgnl2_filtered.empty:
                product = sgnl1_filtered['x(n)'].values[0] * sgnl2_filtered['h(n)'].values[0]
                term.append(product)  
                summation=sum(term)
                
            # Handle the case where one or both df are empty
            else:
                term.append(0)
    
        y.append(summation)
    
    ###############################################################################  
    plot_signal(indx, y, 'index','signal','Convlution Plot')
    ConvTest(indx,y)
    
