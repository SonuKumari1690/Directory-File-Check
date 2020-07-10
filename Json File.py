#!/usr/bin/env python
# coding: utf-8

# In[28]:


import json as jsn
import os


file_names = list(os.listdir(r'C:\Users\admin\Downloads\test123.json'))
file_names = [i for i in file_names if i.endswith('.json')]


ftw = open(r'C:\Users\admin\Downloads\result.csv','a')
ftw.write('file_name'+','+'row_number'+','+'column_name'+'\n')

for file in file_names:
    row_number = 0
    f = open(r'C:\Users\admin\Downloads\test123.json\\'+file)
    for i in f:
        row_number+=1
        dictionary = jsn.loads(i)
        for key,item in dictionary.items():
                
            if(item==False and type(item)==bool):
                ftw.write(file+','+str(row_number)+','+key+'\n')
            
ftw.close()


# In[ ]:




