import numpy as np
import math
import tkinter as tk

from CompareSignals5 import *
from Read_Files_Func import Read_Files

def DFT(sample_lst):
    harmonic_lst=[]

    N=len(sample_lst)
    for Hth in range(N):
        sgnl_no = -1
        term=[]
        
        for sgnl in sample_lst:
            sgnl_no = sgnl_no+1
            
            first_bracket=2*sgnl_no-1
            second_bracket=2*Hth-1
            
            angle= (np.pi/(4*N) )*first_bracket*second_bracket
            cos_angle= math.cos(angle)

            mul=np.dot(sgnl, cos_angle)

            term.append(mul)  
            summation=sum(term)
        result=round(np.sqrt(2/N)*summation,5)
        harmonic_lst.append(result)  

    return harmonic_lst


def write_txt(m,DFT_input_df,DFT_output):
    m=int(m)
    with open("Tasks_Write_Files/Task5/DCT.txt", 'w') as file:
        file.write(str(0)+'\n')
        file.write(str(1)+'\n')
        file.write(str(len(DFT_input_df))+'\n')
        for item in range(m):
            file.write("0 %s  \n" % DFT_output[item])
            
def call_write():
   m= m_entry.get()   
   num_samples,index_list,sample_list=Read_Files('Task 5 Test Cases\DCT\DCT_input.txt')     
   DFT_output= DFT(sample_list)
   write_txt(m,sample_list,DFT_output) 
   SignalSamplesAreEqual("Task 5 Test Cases\DCT\DCT_output.txt",DFT_output)
       
            
def Run_DCT():
       
       
     window = tk.Tk()
     window.geometry('200x200')
    
     frame = tk.LabelFrame(window, text="Enter M ")
     frame.pack(padx=10, pady=10)
     
    
     global m_entry
     m_entry = tk.Entry(frame)
     m_entry.pack(side=tk.LEFT, padx=5, pady=5)
     
     button = tk.Button(frame, text="Enter", command=call_write)
     button.pack(side=tk.LEFT, padx=5, pady=5)
     window.mainloop()
 