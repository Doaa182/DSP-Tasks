#import libraries
import numpy as np
import matplotlib.pyplot as plt

import tkinter as tk
from tkinter import filedialog
from comparesignals import SignalSamplesAreEqual
import pandas as pd

##############################################################################################################################################################
##############################################################################################################################################################    
def plot_sample(splitted_arr):
  
    #extract t and f(t) values from the splitted array
    t = splitted_arr[:, 0].astype(float)
    f_of_t = splitted_arr[:, 1].astype(float)
    
    #plot continuous data as a line plot
    plt.plot(t, f_of_t, label='Continuous')
    
    #plot discrete data as points and verticle dashed lines
    plt.plot(t, f_of_t, 'ro', label='Discrete')
    plt.vlines(t, [0], f_of_t, colors='red', linestyles='dashed')
    
    #labels
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.axline((0, 0), slope=0, color="black", linestyle='solid')
    plt.legend()
    
    #show plot
    plt.show()     
           
###############################################################################
#read signal samples from txt file 
def read(filename):

    with open(filename, 'r') as file:
        signal_samples = np.array([line.strip() for line in file])
        
        #empty list to store row indices
        new_f_indices = []

        # Iterate over each row
        for i, str_row in enumerate(signal_samples):
            # Iterate over each char in the string
            for char in str_row:
            # Check if this row has a space or not
                if char == ' ':
                    new_f_indices.append(i)
        new_f = np.array([signal_samples[i] for i in new_f_indices])
        #split into two cols
        split_array = np.char.split(new_f)

        #convert the splitted array to a 2D array
        split_array = np.array(split_array.tolist())
        plot_sample(split_array)
               
##############################################################################################################################################################
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def plot_signal(title,t, signal):
 fig = plt.figure(figsize=(5, 4), dpi=100)
 plt.plot(t, signal,label='Continuous')
 plt.title(title)
 # plt.plot(t, signal, 'ro', label='Discrete')
 # plt.vlines(t, [0], signal, colors='red', linestyles='dashed')
 plt.xlabel('Time')
 plt.ylabel('Amplitude')
 plt.show()           
          
###############################################################################
def open_file_to_read_samples():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if file_path:
        read(file_path)
        
###############################################################################

        
##############################################################################################################################################################
##############################################################################################################################################################    
#read signal from txt file 
def read_w2(filename):

    with open(filename, 'r') as file:
        signal_samples = np.array([line.strip() for line in file])
    return signal_samples

###############################################################################
#calling the read fn
s1=read_w2('DSP\DSP2\Task 2 + Files\input signals\Signal1.txt')
s2=read_w2('DSP\DSP2\Task 2 + Files\input signals\Signal2.txt')
s3=read_w2('DSP\DSP2\Task 2 + Files\input signals\Signal3.txt')

###############################################################################
df1 = pd.DataFrame(s1).iloc[3:]
df2 = pd.DataFrame(s2).iloc[3:]
df3 = pd.DataFrame(s3).iloc[3:]

results=[]
results = pd.DataFrame(results)

###############################################################################
#split into two cols
df1[['Indx', 'Sgnl']] = df1[0].str.split(' ', expand=True)
df2[['Indx', 'Sgnl']] = df2[0].str.split(' ', expand=True)
df3[['Indx', 'Sgnl']] = df3[0].str.split(' ', expand=True)

###############################################################################
df1["Sgnl"] = df1["Sgnl"].astype(str).astype(int)
df2["Sgnl"] = df2["Sgnl"].astype(str).astype(int)
df3["Sgnl"] = df3["Sgnl"].astype(str).astype(int)

###############################################################################
results['Sgnl1+Sgnl2'] =df1['Sgnl']+df2['Sgnl']
results['Sgnl1+Sgnl3'] =df1['Sgnl']+df3['Sgnl']

###############################################################################
results['Sgnl2-Sgnl1'] =df2['Sgnl']-df1['Sgnl']
results['Sgnl3-Sgnl1'] =df3['Sgnl']-df1['Sgnl']

###############################################################################
results['Sgnl1*5'] =df1['Sgnl']*5
results['Sgnl2*10'] =df2['Sgnl']*10

results['Sgnl1*-5'] =df1['Sgnl']*-5
results['Sgnl2*-10'] =df2['Sgnl']*-10

###############################################################################
results['Sgnl1^2'] =df1['Sgnl']**2

###############################################################################
def plot_arth(data,res,col1,col2):
    #plot continuous data as a line plot
    plt.plot(data[col1], res[col2], label='Continuous')

    # #plot discrete data as points and verticle dashed lines
    # plt.plot(data[col1], res[col2], 'ro', label='Discrete')
    # plt.vlines(data[col1], [0], res[col2], colors='red', linestyles='dashed')

    #labels
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.title(col2)
    plt.legend()
    plt.show()
    
###############################################################################
def plot_add():
    plot_arth(df1,results,'Indx','Sgnl1+Sgnl2')
    plot_arth(df1,results,'Indx','Sgnl1+Sgnl3')
        
###############################################################################        
def plot_sub():
    plot_arth(df1,results,'Indx','Sgnl2-Sgnl1')
    plot_arth(df1,results,'Indx','Sgnl3-Sgnl1')
    
###############################################################################
def plot_mul():
    plot_arth(df1,results,'Indx','Sgnl1*5')
    plot_arth(df1,results,'Indx','Sgnl1*-5')

    plot_arth(df2,results,'Indx','Sgnl2*10')
    plot_arth(df2,results,'Indx','Sgnl2*-10')
    
###############################################################################
def plot_squ():
   plot_arth(df1,results,'Indx','Sgnl1^2')


##############################################################################################################################################################      


             
###############################################################################
def open_file_to_read_samples():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if file_path:
        read(file_path)
        

###############################################################################
def choose_task():
    if vall.get()==1:
       open_file_to_read_samples()
       
    elif vall.get()==2: 
        from UpdatedTask2 import Signal_Genrator_Gui
        Signal_Genrator_Gui()
    elif vall.get()==7: 
               from UpdatedTask3 import Use_Gui
               Use_Gui()
    else: 
        if vall.get()==3: 
                plot_add()    
        elif vall.get()==4: 
                plot_sub()    
        elif vall.get()==5: 
                    plot_mul()
        elif vall.get()==6: 
                  plot_squ()
             
def task1():
    window = tk.Tk()
    window.geometry("700x400")
    window.title('Window')
    
    fram=tk.LabelFrame(window, text="Choose Task")
    fram.pack()
    
    global vall
    vall=tk.IntVar()
    Rbtn1=tk.Radiobutton(fram,text='Read Samples',variable=vall,value=1)
    Rbtn1.pack(anchor='w')
    
    Rbtn2=tk.Radiobutton(fram,text='Generate Wave',variable=vall,value=2)
    Rbtn2.pack(anchor='w')
    Rbtn3=tk.Radiobutton(fram,text='Addition',variable=vall,value=3)
    Rbtn3.pack(anchor='w')
    
    Rbtn4=tk.Radiobutton(fram,text='Subtraction',variable=vall,value=4)
    Rbtn4.pack(anchor='w')
    
    Rbtn5=tk.Radiobutton(fram,text='Multiplication',variable=vall,value=5)
    Rbtn5.pack(anchor='w')
    
    Rbtn6=tk.Radiobutton(fram,text='Squaring',variable=vall,value=6)
    Rbtn6.pack(anchor='w')
    
    Rbtn7=tk.Radiobutton(fram,text='Other',variable=vall,value=7)
    Rbtn7.pack(anchor='w')
    
    btn=tk.Button(fram, text="Enter", command=choose_task)
    btn.pack()
    
    window.mainloop()

 
###############################################################################
task1()  

###############################################################################

