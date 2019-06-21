#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
#create adjacency matrix
adjmtr=np.zeros((10,10))
adjmtr[1][2]=adjmtr[1][3]=adjmtr[1][5]=1
adjmtr[2][4]=adjmtr[2][5]=1
adjmtr[3][5]=adjmtr[3][6]=1
adjmtr[4][5]=adjmtr[4][8]=1
adjmtr[5][6]=1
adjmtr[6][7]=adjmtr[6][9]=1
adjmtr[7][4]=adjmtr[7][5]=adjmtr[7][8]=1
adjmtr[9][7]=adjmtr[9][8]=1

list1=[1]
node=[1]

adjmtr




def BSF(a):
    for i in range(1,10):
        if adjmtr[a][i]==1 and (i in node)==False:
            list1.append(i)
            node.append(i)
            print(list1)
            print("next=%d" %len(node))
    list1.remove(a)
    print(list1)
    print("next=%d" %len(node))
    if list1!=[]:
        a=list1[0] 
        BSF(a)
BSF(1)


# In[ ]:





# In[ ]:




