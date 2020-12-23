#!/usr/bin/env python
# coding: utf-8

# ## 계단 오르기 Top-Down : 메모이제이션 (DP)
# 

# In[1]:


# Top-Down 방식

n=4

def DFS(m):
    if dy[m]>0:
        return dy[m]
    
    if m == 1 or m == 2:
        return m
    else:
        dy[m]=DFS(m-1)+DFS(m-2)
        return dy[m]
    
if __name__=="__main__":
    dy=[0]*(n+1)
    print(DFS(n))
    


# In[2]:


# Bottom-Up 방식

n=4

dy=[0]*(n+1)
dy[1]=1
dy[2]=2

for i in range(3, n+1):
    dy[i] = dy[i-1]+ dy[i-2]
    
print(dy[n])


# In[ ]:




