#!/usr/bin/env python
# coding: utf-8

# ## 침몰하는 타이타닉(그리디)
# 
# #### 강의풀이1 : pop()이용

# In[6]:


n= 5
m= 140
w=[90, 50, 70, 100, 60]
cnt=0

w.sort()

while w:
    if len(w) ==1:
        cnt+=1
        break
    if w[0]+w[-1]>m:
        w.pop()
        cnt+=1
    else:
        w.pop(0)
        w.pop()
        cnt+=1
        


# In[7]:


print(cnt)


# #### 강의풀이2: deque() 이용
# 

# In[9]:


from collections import deque
n= 5
m= 140
w=[90, 50, 70, 100, 60]
cnt=0

w.sort()
w=deque(w)

while w:
    if len(w) ==1:
        cnt+=1
        break
    if w[0]+w[-1]>m:
        w.pop()
        cnt+=1
    else:
        w.popleft()
        w.pop()
        cnt+=1
print(cnt)


# In[ ]:




