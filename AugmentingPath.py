#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
import math
gp = pd.read_csv('graph3.csv')

global list1
global Visit
list1=[1]
Visit=[1]
global Node
global Path
global Pred
Node=[]
Path=[]
Pred=[]
N=gp['Starting-node'].max()
M=gp['Ending-node'].max()
N=max(N,M)

for i in range(1,N+1):
    Node.append(i)
    Pred.append(0)

gp=gp.reset_index()
gp['Re-Arc-length']=0

def BSF(a,b):
    for i in gp[gp['Starting-node'] == a][gp[gp['Starting-node'] == a]['Arc-length'] > 0]['Ending-node']:
        if  (i in Visit) == False:
            list1.append(i)
            Visit.append(i)
            Pred[i-1] = a
    for i in gp[gp['Ending-node'] == a][gp[gp['Ending-node'] == a]['Re-Arc-length'] > 0]['Starting-node']:
        if  (i in Visit) == False:
            list1.append(i)
            Visit.append(i)
            Pred[i-1]=a
    list1.remove(a)
    if list1!=[] and b not in Visit:
        a=list1[0] 
        BSF(a,b)
    if list1 == []:
        return 0
    else:
        return 1

def FINDPATH(c):
    Path.append(c)
    if c !=1 :
        FINDPATH(Pred[c-1])
    else:
        Path.reverse()
        return

def REGP(P,GP):
    Flow = []
    Index = []
    Sign = []
    i=0
    while i < len(Path)-1 :
        if  GP[GP['Starting-node'] == P[i]][GP[GP['Starting-node'] == P[i]]['Ending-node'] == P[i+1]].shape[0] == 1:
            Index.append(GP[GP['Starting-node'] == P[i]][GP[GP['Starting-node'] == P[i]]['Ending-node'] == P[i+1]]['index'].sum())
            Sign.append(1)
            Flow.append(GP[GP['Starting-node'] == P[i]][GP[GP['Starting-node'] == P[i]]['Ending-node'] == P[i+1]]['Arc-length'].sum())
        else:
            Index.append(GP[GP['Starting-node'] == P[i+1]][GP[GP['Starting-node'] == P[i+1]]['Ending-node'] == P[i]]['index'].sum())
            Sign.append(0)
            Flow.append(GP[GP['Starting-node'] == P[i]][GP[GP['Starting-node'] == P[i]]['Ending-node'] == P[i+1]]['Re-Arc-length'].sum())
        i+=1
    m=min(Flow)
    i=0
    while i < len(Path)-1 :
        if Sign[i] == 1:
            GP.loc[Index[i],'Arc-length']-=m
            GP.loc[Index[i],'Re-Arc-length']+=m
        else:
            GP.loc[Index[i],'Arc-length']+=m
            GP.loc[Index[i],'Re-Arc-length']-=m
        i+=1

def AP() :
    global list1
    global Visit
    global Node
    global Path
    global Pred
    y = BSF(1,N)
    while(y==1):
        FINDPATH(N)
        REGP(Path,gp)
        list1=[1]
        node=[1]
        Visit=[1]
        Path=[]
        Pred=[]
        for i in range(1,N+1):
            Pred.append(0)
        y = BSF(1,N)

AP()
gp


# In[ ]:




