import tkinter as tk

from CompareSignals1 import *

def Read_Files(path):
        f_input= open(path,'r')
        file_content=f_input.readlines()
        num_samples=file_content[2]
        sample_list=[]
        index_list=[]
        for i in range(3,len(file_content)):
            line=file_content[i].strip()
            line=line.split(' ')
            index_list.append(int(line[0]))
            sample_list.append(float(line[1]))
             
        return index_list,sample_list

def compute_smothing():
    w=int(w_entry.get())
    
    lst=[]
    index=[]
    output_file_path=''
    if  w==3:
        index,lst=Read_Files('Task 2 Test Cases\input signals\Signal1.txt')
        output_file_path='Task 6 Test Cases\Moving Average\OutMovAvgTest1.txt'
    elif w==5 :
        index,lst=Read_Files('Task 2 Test Cases\input signals\Signal2.txt') 
        output_file_path='Task 6 Test Cases\Moving Average\OutMovAvgTest2.txt'
       
    n=len(lst) # numbers of samples in list    
    end =n-w+1
    smothing_lst=[]
    for i in range(end):
        summtion=0
        step=0
        while(step<w):
            summtion+=lst[i+step]
            step+=1
        smothing_lst.append(summtion/w) 
         
    SignalSamplesAreEqual(output_file_path,index,smothing_lst) 
    print('----------------------------------')


def Run_Smoothing():
    window = tk.Tk()
    window.geometry('200x200')
    window.title('Smothing window')
    frame = tk.LabelFrame(window, text="Enter W ")
    frame.pack(padx=10, pady=10)
    
   
    global w_entry
    w_entry = tk.Entry(frame)
    w_entry.pack(side=tk.LEFT, padx=5, pady=5)
    button = tk.Button(frame, text="Enter", command=compute_smothing)
    button.pack(side=tk.LEFT, padx=5, pady=5)
    window.mainloop()
    
    