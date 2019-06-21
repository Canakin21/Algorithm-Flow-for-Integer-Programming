#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np
import pandas as pd
import math
gp = pd.read_csv('graph.csv')

list1=[1]
node=[1]
Visit=[1]


Node=[]
N=gp['Starting-node'].max()
for i in range(1,N+1):
    Node.append(i)


def BSF(a,b):
    for i in gp[gp['Starting-node'] == a][gp[gp['Starting-node'] == a]['Arc-length'] > 0]['Ending-node']:
        if  (i in Visit) == False:
            list1.append(i)
            Visit.append(i)
#     for i in gp[gp['Starting-node'] == a][gp[gp['Starting-node'] == a]['Re-Arc-length'] < 0]['Ending-node']:
#         if  (i in Visit) == False:
#             list1.append(i)
#             Visit.append(i)
    list1.remove(a)
    print(list1)
    print("next=%d" %len(Visit))
    if list1!=[]:
        a=list1[0] 
        BSF(a,b)
    else:
        return


BSF(1,N)


# In[ ]:




