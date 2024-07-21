import numpy as np
import matplotlib.pyplot as plt

from CompareSignals5 import *
from Read_Files_Func import Read_Files

# def Read_Files():
#         f_input= open('Task 5 Test Cases\Remove DC component\DC_component_input.txt','r')

#         file_content=f_input.readlines()
#         num_samples=file_content[2]
#         sample_list=[]
#         index_list=[]
#         for i in range(3,len(file_content)):
#             line=file_content[i].strip()
#             line=line.split(' ')
#             index_list.append(int(line[0]))
#             sample_list.append(float(line[1]))

# #         print(index_list)
# #         print(sample_list)
                
#         return num_samples,index_list,sample_list



def indexs_after_Avg(n_sample_in,input_indexs):
    summtion=np.sum(input_indexs)
    avg=summtion/int(n_sample_in)
    
    new_sample_list=[]
    for i in range(len(input_indexs)):
        new_sample_list.append(round(input_indexs[i]-avg,3))
    return new_sample_list

def plot_signal(title,i,v):
    plt.figure()
    plt.title(title)
    plt.plot(i, v,'ro')
    plt.plot(i, v)
    plt.grid()
    plt.show()    


def Run_Remove_Dc_Comp():
    num_samples,index_list,sample_list=Read_Files('Task 5 Test Cases\Remove DC component\DC_component_input.txt')
    avg_samples=indexs_after_Avg(num_samples,sample_list)
    SignalSamplesAreEqual('Task 5 Test Cases\Remove DC component\DC_component_output.txt',avg_samples)
    # plot_signal('After subtraction Avg',index_list,sample_list)
    # plot_signal('Before subtraction Avg',index_list,avg_samples)
    
    
#Run_Remove_Dc_Comp()   
    