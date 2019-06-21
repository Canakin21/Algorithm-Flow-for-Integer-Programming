#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import math
gp = pd.read_csv('graph5.csv')
########################################
Node = []
N=gp['Starting-node'].max()
M=gp['Ending-node'].max()
N=max(N,M)
for i in range(N+1):
    Node.append(i)

Pred = []
for i in range(N+1):
    Pred.append(i)

Pred[1] = 0

D = np.ones(N+1)
D = D * math.inf
D[1] = 0

Que=[1]
########################################
def deque(inS):
    if inS != []:
        i = inS.pop(0)
        print('i=',i)
        #Arc
        for j in gp[gp['Starting-node']==i]['Ending-node']:
            print('j=',j)
            if (D[j] > D[i] + gp[gp['Starting-node']==i][gp[gp['Starting-node']==i]['Ending-node']==j]['CostPi'].sum()) and (gp[gp['Starting-node']==i][gp[gp['Starting-node']==i]['Ending-node']==j]['Arc-capacity'].sum()>0):
                D[j] = D[i] + gp[gp['Starting-node']==i][gp[gp['Starting-node']==i]['Ending-node']==j]['CostPi'].sum()
                Pred[j] = i
                if j not in inS :
                    for k in range(len(inS)):
                        if (k+1 == len(inS)) and (D[j] > D[inS[k]]):
                            inS.append(j)
                            break
                        if D[j] <= D[inS[k]]:
                            inS.insert(k,j)
                            break
                    if inS==[]:
                        inS.append(j)
                    print('Que=',inS)
        #Re-Arc
        for j in gp[gp['Ending-node']==i]['Starting-node']:
            print('j=',j)
            if (D[j] > D[i] - gp[gp['Ending-node']==i][gp[gp['Ending-node']==i]['Starting-node']==j]['CostPi'].sum()) and (gp[gp['Ending-node']==i][gp[gp['Ending-node']==i]['Starting-node']==j]['Re-Arc-capacity'].sum()>0):
                D[j] = D[i] - gp[gp['Ending-node']==i][gp[gp['Ending-node']==i]['Starting-node']==j]['CostPi'].sum()
                Pred[j] = i
                if j not in inS :
                    for k in range(len(inS)):
                        if (k+1 == len(inS)) and (D[j] > D[inS[k]]):
                            inS.append(j)
                            break
                        if D[j] <= D[inS[k]]:
                            inS.insert(k,j)
                            break
                    if inS==[]:
                        inS.append(j)
                    print('Que=',inS)
        deque(inS)
    else:
        return
    
deque(Que)
print(Node)
print(Pred)
print(D)


# In[5]:


gp


# In[ ]:





# In[ ]:




