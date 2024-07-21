#import libraries
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog

from CompareSignals2 import AddSignalSamplesAreEqual,SubSignalSamplesAreEqual,MultiplySignalByConst,SignalSamplesAreEqual
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
               


###############################################################################
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
        

##############################################################################################################################################################
##############################################################################################################################################################    
#read signal from txt file 
def read_w2(filename):

    with open(filename, 'r') as file:
        signal_samples = np.array([line.strip() for line in file])
    return signal_samples


###############################################################################
def plot_arth(x,y,title):
    #plot continuous data as a line plot
    plt.plot(x,y, label='Continuous')

    # #plot discrete data as points and verticle dashed lines
    # plt.plot(data[col1], res[col2], 'ro', label='Discrete')
    # plt.vlines(data[col1], [0], res[col2], colors='red', linestyles='dashed')

    #labels
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.title(title)
    plt.legend()
    plt.show()
from Read_Files_Func import Read_Files
#calling the read fn

n1,index1,signal1=   Read_Files('Task 2 Test Cases\input signals\Signal1.txt')
n2,index2,signal2=   Read_Files('Task 2 Test Cases\input signals\Signal2.txt')
n3,index3,signal3=   Read_Files('Task 2 Test Cases\input signals\Signal3.txt')


###############################################################################
sum12 = []
for x, y in zip(signal1, signal2):
    sum12.append( x + y)
sum13 = []
for x, y in zip(signal1, signal3):
    sum13.append( x + y)    
def plot_add():
    AddSignalSamplesAreEqual('Signal1.txt','Signal2.txt',index1,sum12)
    AddSignalSamplesAreEqual('Signal1.txt','Signal3.txt',index1,sum13)
    plot_arth(index1,sum12,'Sgnl1+Sgnl2')
    plot_arth(index1,sum13,'Sgnl1+Sgnl3')
        
###############################################################################    
sub12 = []
for x, y in zip(signal1, signal2):
    sub12.append( y-x)
sub13 = []
for x, y in zip(signal1, signal3):
    sub13.append( y-x)        
def plot_sub():
    SubSignalSamplesAreEqual('Signal1.txt','Signal2.txt',index1,sub12)
    SubSignalSamplesAreEqual('Signal1.txt','Signal3.txt',index1,sub13)
    plot_arth(index1,sub12,'Sgnl2-Sgnl1')
    plot_arth(index1,sub13,'Sgnl3-Sgnl1')
    
###############################################################################
def plot_mul():
 
    Sgnl1_plus5=[]
    Sgnl1_mius5=[]
    for x in signal1:
        Sgnl1_plus5.append(5*x)
        Sgnl1_mius5.append(-5*x)
   
    
    Sgnl2_plus10=[]
    Sgnl2_mius10=[]
    for x in signal2:
        Sgnl2_plus10.append(10*x)
        Sgnl2_mius10.append(-10*x)
    
    MultiplySignalByConst(5,index1,Sgnl1_plus5)
    
    MultiplySignalByConst(10,index1,Sgnl2_plus10)
  
    
    plot_arth(index1,Sgnl1_plus5,'Sgnl1 * +5')
    plot_arth(index1,Sgnl2_plus10,'Sgnl2 * +10')

    
###############################################################################
def plot_squ():
    sq=[]
    for x in signal1:
        sq.append(x**2)
    SignalSamplesAreEqual('Squre Signal 1','Task 2 Test Cases\output signals\Output squaring signal 1.txt',index1,sq)
    plot_arth(index1,sq,'Sgnl1 ^2')



