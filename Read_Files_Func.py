def Read_Files(path):
        # f_input= open('Task_files5\Remove DC component\DC_component_input.txt','r')
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

#         print(index_list)
#         print(sample_list)
                
        return num_samples,index_list,sample_list