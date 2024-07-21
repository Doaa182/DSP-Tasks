#import libraries
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog


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
               


def Run_Read_Signal():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if file_path:
        read(file_path)
        