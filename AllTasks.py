import tkinter as tk

def choose_task():
    if vall.get()==1:
       from Task1_Read_Signal import Run_Read_Signal
       Run_Read_Signal()
       
    elif vall.get()==2: 
        from Task1_Generate_Signal import Run_Generate_Signal
        Run_Generate_Signal()
   
    else: 
        
        if vall.get()==3: 
                from Task2_Add_Sub_Mul_Squ import plot_add
                plot_add()    
                
        elif vall.get()==4: 
                from Task2_Add_Sub_Mul_Squ import plot_sub
                plot_sub()    
                
        elif vall.get()==5: 
                from Task2_Add_Sub_Mul_Squ import plot_mul
                plot_mul()
                
        elif vall.get()==6: 
                from Task2_Add_Sub_Mul_Squ import plot_squ
                plot_squ()
                
        elif vall.get()==7: 
                from Task2_OtherOperations import Run_Shifting_OR_Normalization_OR_Accumlation
                Run_Shifting_OR_Normalization_OR_Accumlation()
                
        elif vall.get()==8: 
                from Task3_Quantize import Run_Quantize
                Run_Quantize()   
                
        elif vall.get()==9: 
                from Task4_Frequency_Domain import Run_Frequency_Domain
                Run_Frequency_Domain()
                
        elif vall.get()==10: 
              from Task5_DCT import  Run_DCT
              Run_DCT()     
              
        elif vall.get()==11: 
              from Task5_Remove_Dc_Comp import Run_Remove_Dc_Comp
              Run_Remove_Dc_Comp()
              
        elif vall.get()==12: 
              from Task6_Smoothing import Run_Smoothing
              Run_Smoothing() 
              
        elif vall.get()==13: 
             from Task6_Derivative_Signal import Run_Derivative_Signal
             Run_Derivative_Signal()
             
        elif vall.get()==14: 
            from Task6_Folding_Shifting import Run_Folding_Shifting
            Run_Folding_Shifting()
            
        elif vall.get()==15: 
            from Task6_Dc_Freq_Domain import Run_Dc_Freq_Domain
            Run_Dc_Freq_Domain() 
            
        elif vall.get()==16: 
            from Task7_Convolution import Run_Convolution
            Run_Convolution()   
            
        elif vall.get()==17: 
            from Task8_Correlation import Run_Task8_Correlation
            Run_Task8_Correlation() 
            
        elif vall.get()==18: 
            from Task9_Fast_Convolution import  Run_Fast_Convolution
            Run_Fast_Convolution()
            
        elif vall.get()==19:  
            from Task9_Fast_Correlation import Run_Fast_Correlation
            Run_Fast_Correlation()           
            
             
                    
              
             
def all_tasks_form():
    window = tk.Tk()
    window.geometry("700x600")
    window.title('Window')
    
    fram=tk.LabelFrame(window, text="Choose Task")
    fram.pack()
    
    global vall
    vall=tk.IntVar()
    Rbtn1=tk.Radiobutton(fram,text='Task1-> Read Samples',variable=vall,value=1)
    Rbtn1.pack(anchor='w')
    
    Rbtn2=tk.Radiobutton(fram,text='Task1-> Generate Wave',variable=vall,value=2)
    Rbtn2.pack(anchor='w')
    Rbtn3=tk.Radiobutton(fram,text='Task2-> Addition',variable=vall,value=3)
    Rbtn3.pack(anchor='w')
    
    Rbtn4=tk.Radiobutton(fram,text='Task2-> Subtraction',variable=vall,value=4)
    Rbtn4.pack(anchor='w')
    
    Rbtn5=tk.Radiobutton(fram,text='Task2-> Multiplication',variable=vall,value=5)
    Rbtn5.pack(anchor='w')
    
    Rbtn6=tk.Radiobutton(fram,text='Task2-> Squaring',variable=vall,value=6)
    Rbtn6.pack(anchor='w')
    
    Rbtn7=tk.Radiobutton(fram,text='Task2-> Shifting, Normalization, Accumlation',variable=vall,value=7)
    Rbtn7.pack(anchor='w')
    
    Rbtn8=tk.Radiobutton(fram,text='Task3-> Quantize',variable=vall,value=8)
    Rbtn8.pack(anchor='w')
    
    Rbtn9=tk.Radiobutton(fram,text='Task4-> Frequency Domain',variable=vall,value=9)
    Rbtn9.pack(anchor='w')
    
    Rbtn10=tk.Radiobutton(fram,text='Task5-> Computing DCT',variable=vall,value=10)
    Rbtn10.pack(anchor='w')
    
    Rbtn11=tk.Radiobutton(fram,text='Task5-> Remove Dc Component',variable=vall,value=11)
    Rbtn11.pack(anchor='w')
    
    Rbtn12=tk.Radiobutton(fram,text='Task6-> Smoothing',variable=vall,value=12)
    Rbtn12.pack(anchor='w')
    
    Rbtn13=tk.Radiobutton(fram,text='Task6-> Sharpening',variable=vall,value=13)
    Rbtn13.pack(anchor='w')
    
    Rbtn14=tk.Radiobutton(fram,text='Task6-> Folding & Shifting',variable=vall,value=14)
    Rbtn14.pack(anchor='w')
    
    Rbtn15=tk.Radiobutton(fram,text='Task6-> Remove DC Frequency Domain',variable=vall,value=15)
    Rbtn15.pack(anchor='w')
    
    Rbtn16=tk.Radiobutton(fram,text='Task7-> Convolution',variable=vall,value=16)
    Rbtn16.pack(anchor='w')
    
    Rbtn17=tk.Radiobutton(fram,text='Task8-> Correlation',variable=vall,value=17)
    Rbtn17.pack(anchor='w')
    
    Rbtn18=tk.Radiobutton(fram,text='Task9-> Fast Convolution',variable=vall,value=18)
    Rbtn18.pack(anchor='w')
    
    Rbtn19=tk.Radiobutton(fram,text='Task9-> Fast Correlation',variable=vall,value=19)
    Rbtn19.pack(anchor='w')
    
    btn=tk.Button(fram, text="Enter", command=choose_task)
    btn.pack()
    
   
    window.mainloop()

 
###############################################################################
all_tasks_form()  

###############################################################################

