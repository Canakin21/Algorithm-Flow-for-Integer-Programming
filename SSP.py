#!/usr/bin/env python
# coding: utf-8

# In[24]:


import numpy as np
import pandas as pd
import math
gp = pd.read_csv('graph5.csv')
#####################################
global list1
global Visit
list1=[1]
Visit=[1]
global Node
global Path
global Pred
global Pi
global b
global D

b=5
Node=[]
Path=[]
Pred=[]
Pi=[]
N=gp['Starting-node'].max()
M=gp['Ending-node'].max()
N=max(N,M)

for i in range(N+1):
    Node.append(i)
    Pred.append(0)
    Pi.append(0)
    
Pred[1] = 0
gp=gp.reset_index()

################Que##################
D = np.ones(N+1)
D = D * math.inf
D[1] = 0

Que=[1]

#####################################

def deque(inS):
    global D
    if inS != []:
        i = inS.pop(0)
        print('i=',i)
        #Arc
        for j in gp[gp['Starting-node']==i]['Ending-node']:
            print('j=',j)
            if (D[j] > D[i] + gp[gp['Starting-node']==i][gp[gp['Starting-node']==i]['Ending-node']==j]['CostPi'].sum()) and (gp[gp['Starting-node']==i][gp[gp['Starting-node']==i]['Ending-node']==j]['Arc-capacity'].sum()>0):
                D[j] = D[i] + gp[gp['Starting-node']==i][gp[gp['Starting-node']==i]['Ending-node']==j]['CostPi'].sum()
                print('Pred=',Pred)
                Pred[j] = i
                print('Yooooo')
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
        print('cur')
        print('D=',D)
        deque(inS)
    else:
        return

def FINDPATH(c):
    Path.append(c)
    if c !=1 :
        FINDPATH(Pred[c])
    else:
        Path.reverse()
        return

def REGP(P,GP):
    global b
    Flow = []
    Index = []
    Sign = []
    i=0
    while i < len(P)-1 :
        if  GP[GP['Starting-node'] == P[i]][GP[GP['Starting-node'] == P[i]]['Ending-node'] == P[i+1]].shape[0] == 1:
            Index.append(GP[GP['Starting-node'] == P[i]][GP[GP['Starting-node'] == P[i]]['Ending-node'] == P[i+1]]['index'].sum())
            Sign.append(1)
            Flow.append(GP[GP['Starting-node'] == P[i]][GP[GP['Starting-node'] == P[i]]['Ending-node'] == P[i+1]]['Arc-capacity'].sum())
        else:
            Index.append(GP[GP['Starting-node'] == P[i+1]][GP[GP['Starting-node'] == P[i+1]]['Ending-node'] == P[i]]['index'].sum())
            Sign.append(0)
            Flow.append(GP[GP['Starting-node'] == P[i]][GP[GP['Starting-node'] == P[i]]['Ending-node'] == P[i+1]]['Re-Arc-capacity'].sum())
        i+=1
    m=min(Flow)
    m=min(m,b)
    b-=m
    i=0
    while i < len(P)-1 :
        if Sign[i] == 1:
            GP.loc[Index[i],'Arc-capacity']-=m
            GP.loc[Index[i],'Re-Arc-capacity']+=m
        else:
            GP.loc[Index[i],'Arc-capacity']+=m
            GP.loc[Index[i],'Re-Arc-capacity']-=m
        i+=1

def COSTPI():
    for i in range(gp.shape[0]):
        gp.loc[i,'CostPi'] = gp.loc[i,'Cost'] - Pi[gp.loc[i,'Starting-node']] + Pi[gp.loc[i,'Ending-node']]



def SSP():
    global list1
    global Visit
    global Node
    global Path
    global Pred
    global Pi
    global b
    global D
    while b > 0 :
        Que=[1]
        D = np.ones(N+1)
        D = D * math.inf
        D[1] = 0
        deque(Que)#output D and Pred
        print('afterdeque')
        print('D=',D)
        print('Pred=',Pred)
        FINDPATH(N)
        REGP(Path,gp)
        Pi=[Pi[i]-D[i] for i in range(N+1)]
        COSTPI()
        list1=[1]
        Visit=[1]
        Path=[]
        Pred=[]
        print('b=',b)
        for i in range(N+1):
            Pred.append(0)

SSP()
gp


# In[25]:


gp.head()


# In[ ]:




