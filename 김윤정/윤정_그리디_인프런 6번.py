#!/usr/bin/env python
# coding: utf-8

# ## 씨름 선수 (그리디)
# 
# #### 나의 풀이
# 
# 소요시간 :12분

# In[2]:


fighter = [[172, 67], [183, 65], [180, 70], [170, 72], [181, 60]]


# In[3]:


fighter.sort(reverse=True)
print(fighter)


# In[11]:


lg = fighter[0][1]
cnt=1

for i in range(1, len(fighter)):
    if fighter[i][1] > lg:
        lg=fighter[i][1]
        cnt+=1

print(cnt)


# #### 강의 풀이

# In[14]:


body=[(172, 67), (183, 65), (180,70), (170,72), (181, 60)]

body.sort(reverse=True) #첫번째 자료를 기준으로 내림차순 정리

largest=0
cnt=0

for x,y in body:
    if y>largest:
        largest=y
        cnt+=1
print(cnt)


# In[ ]:




