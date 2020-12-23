#!/usr/bin/env python
# coding: utf-8

# ## 재귀, 메모이제이션 : Top-Down 방식 (DP)
# 
# 
# #### 강의 풀이

# In[7]:


n=7

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
    

