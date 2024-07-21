import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from tkinter import * 

from Read_Files_Func import Read_Files
#from comparesignals import SignalSamplesAreEqual
from CompareSignals2 import SignalSamplesAreEqual

def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    Run_Shifting_OR_Normalization_OR_Accumlation(file_path)

def Plot_Signal(title,i, v2):
    plt.figure()
    plt.title(title)
    plt.plot(i, v2)
    plt.grid()
    plt.show()


def Shift_Signal():
    if shift_entry.get()=='':
        Plot_Signal('OutPut Signal',Fclmn, Sclmn)
    else:    
        shift_value = float(shift_entry.get())
        if shiftVar.get() == 1:
         newVal = Fclmn  +(-1* shift_value)
         SignalSamplesAreEqual('shifting by add 500','Task 2 Test Cases\output signals\output shifting by add 500.txt',newVal,Sclmn)
         Plot_Signal('Positive Shifted Signal',newVal,Sclmn)
         
        elif  shiftVar.get() == 2:
          newVal = Fclmn - (-1*shift_value)
          SignalSamplesAreEqual('shifting by minus 500','Task 2 Test Cases\output signals\output shifting by minus 500.txt',newVal,Sclmn)
          Plot_Signal('Negative Shifted Signal',newVal,Sclmn)
        else :
           tk.messagebox.showwarning("showwarning", "You Should Choose Sign")
           
           
def Normalize_Signal():
          if NormVar.get() == 1:
              normalized_signal = (Sclmn - np.min(Sclmn)) / (np.max(Sclmn) - np.min(Sclmn))
              # SignalSamplesAreEqual('normalized_signal2','Task 2 Test Cases\output signals\normalize of signal 2 output.txt',Fclmn,  normalized_signal)
              # SignalSamplesAreEqual('normalized_signal2','DSP2\normalize_of_signal_2_output.txt',Fclmn,  normalized_signal)
             
              Plot_Signal('Normalized Signal Range[0,1]',Fclmn,  normalized_signal)
          elif NormVar.get() == 2:
              normalized_signal = 2 * ((Sclmn - np.min(Sclmn)) / (np.max(Sclmn) - np.min(Sclmn))) - 1
              # SignalSamplesAreEqual('normalized_signal1','Task 2 Test Cases\output signals\normalize of signal 1 output.txt',Fclmn,  normalized_signal)
              # SignalSamplesAreEqual('normalized_signal1','Task 2 Test Cases\normalize_of_signal_1_output.txt',Fclmn,  normalized_signal)
             
              Plot_Signal('Normalized Signal Range[-1,1]',Fclmn, normalized_signal)
          else:
              Plot_Signal('OutPut Signal',Fclmn, Sclmn)          

def accumulate_signal():
    newVal = np.cumsum(Fclmn)
    # SignalSamplesAreEqual('accumulation for signal1','Task 2 Test Cases\output signals\output accumulation for signal1.txt',Sclmn,newVal)
    Plot_Signal('Accumlated Signal', Sclmn,newVal)
    plt.show()

def Run_Shifting_OR_Normalization_OR_Accumlation(file_path):
    
    n_samples,Fl,Sl=Read_Files(file_path)
    global Fclmn,Sclmn
    Fclmn=np.array(Fl)
    Sclmn=np.array(Sl)
    top = tk.Toplevel()
    top.title("Signal Processing")
    
    # Shifting operation
    shift_frame = tk.LabelFrame(top, text="Shifting")
    shift_frame.pack(padx=10, pady=10)

    shift_label = tk.Label(shift_frame, text="Shift value:")
    shift_label.pack(side=tk.LEFT, padx=5, pady=5)
    
    global shift_entry
    shift_entry = tk.Entry(shift_frame)
    
    shift_entry.pack(side=tk.LEFT, padx=5, pady=5)
    
    global shiftVar
    shiftVar=IntVar()
    shiftRdionBtn1=tk.Radiobutton(shift_frame,text='add',variable = shiftVar,
                    value = 1).pack(side=tk.LEFT)
    shiftRdionBtn2=tk.Radiobutton(shift_frame,text='minus',variable = shiftVar,
                    value = 2).pack(side=tk.LEFT)
    

    
    shift_button = tk.Button(top, text="Display", command=Shift_Signal)
    shift_button.pack()
    
    # Normalization operation
    normalize_frame = tk.LabelFrame(top, text="Normalization")
    normalize_frame.pack(padx=10, pady=10)

    global NormVar
    NormVar = IntVar()
    radBtn1 = Radiobutton(normalize_frame, text = "0 to 1", variable = NormVar,
                 value = 1).pack()
    radBtn2 = Radiobutton(normalize_frame, text = "-1 to 1", variable = NormVar,
                   value = 2).pack()
  
      

    normalize_button = tk.Button(normalize_frame, text="Normalize", command=Normalize_Signal)
    normalize_button.pack(side=tk.LEFT, padx=5, pady=5)
    
    accumulate_frame = tk.LabelFrame(top, text="Accumulation")
    accumulate_frame.pack(padx=10, pady=10)



    accumulate_button = tk.Button(accumulate_frame, text="Display", command=accumulate_signal)
    accumulate_button.pack(padx=5, pady=5)

    top.mainloop()



def Run_Shifting_OR_Normalization_OR_Accumlation():
    global root
    root = tk.Tk()
    root.title("File Selection")
    
    file_button = tk.Button(root, text="Choose File", command=choose_file)
    file_button.pack(padx=10, pady=10)
    root.mainloop()
  

