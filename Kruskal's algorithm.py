#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

gp = pd.read_csv('graph6.csv')


N=gp['Starting-node'].max()
M=gp['Ending-node'].max()
N=max(N,M)

    

gp=gp.sort_values(by='Cost')
gp=gp.reset_index()
gp=gp.reset_index()
gp['tree label']=gp['level_0']
index=gp['index'].max()
gp.drop('index',axis=1,inplace=True)
gp.drop('level_0',axis=1,inplace=True)


for n in range(index+1):
    Count=[]
    Visit=[]
    Visit2=[]
    for i in range(11):
        Count.append(0)
        
    for m in range(n):

        if gp.iloc[n]['Starting-node']==gp.iloc[m]['Starting-node']:
            if gp.iloc[n]['Starting-node'] not in Visit2:
                Count[gp.iloc[m,3]]+=1
                Visit2.append(gp.iloc[n]['Starting-node'])
            Visit.append(gp.iloc[m,3])

        if gp.iloc[n]['Starting-node']==gp.iloc[m]['Ending-node']:
            if gp.iloc[n]['Starting-node'] not in Visit2:
                Count[gp.iloc[m,3]]+=1
                Visit2.append(gp.iloc[n]['Starting-node'])
            Visit.append(gp.iloc[m,3])

        if gp.iloc[n]['Ending-node']==gp.iloc[m]['Starting-node']:
            if gp.iloc[n]['Ending-node'] not in Visit2:
                Count[gp.iloc[m,3]]+=1
                Visit2.append(gp.iloc[n]['Ending-node'])
            Visit.append(gp.iloc[m,3])

        if gp.iloc[n]['Ending-node']==gp.iloc[m]['Ending-node']:
            if gp.iloc[n]['Ending-node'] not in Visit2:
                Count[gp.iloc[m,3]]+=1
                Visit2.append(gp.iloc[n]['Ending-node'])
            Visit.append(gp.iloc[m,3])
    if max(Count)==2:

        gp.iloc[n,0]=0
        gp.iloc[n,1]=0
        gp.iloc[n,2]=0
        gp.iloc[n,3]=0
#         gp.drop(n,axis=0,inplace=True)  
    if max(Count)!=2:
        for k in range(n):
            if gp.iloc[k,3] in Visit:
                gp.iloc[k,3]=n
gp.head(11)


# In[ ]:




