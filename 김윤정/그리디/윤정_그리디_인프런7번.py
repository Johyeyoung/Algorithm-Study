#!/usr/bin/env python
# coding: utf-8

# ## 창고 정리 (그리디)
# 
# #### 나의 풀이
# 
# 소요시간 : 18분

# In[26]:


l = 10
box = 69, 42, 68, 76, 40, 87, 14, 65, 76, 81
m = 50

box = list(box)



for _ in range(50):
    temp=min(box)
    box.append(temp+1)
    box.remove(temp)
    
    
    temp2=max(box)
    box.append(temp2-1)
    box.remove(temp2)
    

result = max(box) - min(box)


print(result)


# #### 강의 풀이
# 
# sort를 통해서 가장 앞에 있는 수에 +1 하고 가장 뒤에 있는 수에 -1 해준다.

# In[28]:


L = 10
a = [69, 42, 68, 76, 40, 87, 14, 65, 76, 81]
m = 50

a.sort()

for _ in range(m):
    a[0]+=1
    a[L-1]-=1
    a.sort()

print(a[L-1]-a[0])


# In[ ]:




