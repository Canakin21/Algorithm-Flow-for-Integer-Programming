#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import math
gp = pd.read_csv('graph.csv')

Node=[]
N=gp['Starting-node'].max()
for i in range(1,N+1):
    Node.append(i)
Node
Node.insert(0,0)

global D
D = np.ones(N+1)
D = D * math.inf
D[1] = 0
D

S=[1]

def Dij(inS):
    SNM = [x for x in Node if x not in inS]
    d = math.inf
    cadidate = 0
    for i in inS:
        for j in gp[gp['Starting-node']==i]['Ending-node']:
            if (j in SNM) & (D[i] + gp[gp['Starting-node']==i][gp[gp['Starting-node']==i]['Ending-node']==j]['Arc-length'].sum() <= d):
                D[j] = D[i] + gp[gp['Starting-node']==i][gp[gp['Starting-node']==i]['Ending-node']==j]['Arc-length'].sum()
                cadidate = j
                d = D[i] + gp[gp['Starting-node']==i][gp[gp['Starting-node']==i]['Ending-node']==j]['Arc-length'].sum()
    D[cadidate] = d
    if cadidate==0:
        print('S=',Node)
        print('D=',D)
        return
    else:
        inS.append(cadidate)
        print('S=',Node)
        print('D=',D)
        print('cadidate=',cadidate)
        print('\n')
        Dij(inS)
        
Dij(S)


# In[ ]:




