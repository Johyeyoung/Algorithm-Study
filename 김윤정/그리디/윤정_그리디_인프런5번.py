#!/usr/bin/env python
# coding: utf-8

# ## 회의실 배정(그리디)
# 
# #### 강의 풀이
# #### 보통 그리디문제는 정렬!
# #### 이 문제에서는 회의가 끝나는 시간을 기준으로 정렬해야함

# In[1]:


n=5
meeting=[(1,4),(2,3),(3,5),(4,6),(5,7)]


# In[4]:


# 튜플의 앞자리 기준으로 sorting은
#meeting.sort()

# 튜플의 뒷자리를 기준으로 sorting하려면
meeting.sort(key=lambda x : (x[1], x[0]))

endtime=0
cnt=0

for s, e in meeting:
    if s>=endtime:
        endtime=e
        cnt+=1

print(cnt)
        


# In[ ]:




