import matplotlib.pyplot as plt
import tkinter as tk

from CompareSignals6 import Shift_Fold_Signal

def Read_Files(path):
        f_input= open(path,'r')
        file_content=f_input.readlines()
        num_samples=file_content[2]
        sample_list=[]
        index_list=[]
        small_lst=[]
        for i in range(3,len(file_content)):
            line=file_content[i].strip()
            line=line.split(' ')
            small_lst.append(line)
            index_list.append(int(line[0]))
            sample_list.append(float(line[1]))  
        return index_list,sample_list,small_lst

def plot_signal(x_values, y_values, x_label,y_label,title):

    plt.plot(x_values, y_values)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    plt.show()  
    
def Folding():
  indices,signal,small_lst=Read_Files('Task 6 Test Cases\Shifting and Folding\input_fold.txt')
  plot_signal(indices,signal,'Indx', 'x(n)','input_fold')
  fold=[]
  for i in small_lst:
       index=int(i[0])*-1
       for j in small_lst:
           if(int(j[0])==index):
               fold.append(int(j[1]))
               break
   # print(fold)   
  plot_signal(indices,fold,'Indx', 'reversed x(n)','output_fold')     
  return indices,fold
def advance():
    k=int(k_entry.get())
    index,folded_signal=Folding()
    new_index=[]
    for i in index:
       value=i+k
       new_index.append(value)
    Shift_Fold_Signal('Task 6 Test Cases\Shifting and Folding\Output_ShifFoldedby500.txt',new_index,folded_signal) 
    plot_signal(new_index,folded_signal,'Shifted Indx', 'reversed x(n)','(Advanced) output_shift_fold_by 500')

def delay():
    k=int(k_entry.get())
    index,folded_signal=Folding()
    new_index=[]
    for i in index:
       value=i-k
       new_index.append(value)
    Shift_Fold_Signal('Task 6 Test Cases\Shifting and Folding\Output_ShiftFoldedby-500.txt',new_index,folded_signal) 
    plot_signal(new_index,folded_signal,'Shifted Indx', 'reversed x(n)','(Delayed) output_shift_fold_by -500')
      

def Run_Folding_Shifting():
    window = tk.Tk()
    window.geometry('280x200')
    window.title('Folding & Shifting window')
    frame = tk.LabelFrame(window, text="Enter k ")
    frame.pack(padx=10, pady=10)
    
   
    global k_entry
    k_entry = tk.Entry(frame)
    k_entry.pack(side=tk.LEFT, padx=5, pady=5)
    
    button1 = tk.Button(frame, text="Delay", command=delay)
    button1.pack(side=tk.LEFT, padx=5, pady=5)
    button2 = tk.Button(frame, text="Advance", command=advance)
    button2.pack(side=tk.LEFT, padx=6, pady=6)
    window.mainloop()
