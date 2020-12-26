#!/usr/bin/env python
# coding: utf-8

# ## 증가수열 만들기(그리디)
# 
# #### 강의풀이
# 
# 문제가 잘 이해안감;;
# 참고 https://jason9319.tistory.com/113

# In[2]:


n=5
a=[2,4,5,1,3]
lt=0
rt=n-1
last=0
res=""
temp=[]

while lt<=rt:
    if a[lt]>last:
        temp.append((a[lt], 'L'))
    if a[rt]>last:
        temp.append((a[rt],'R'))
    temp.sort()
    if len(temp)==0:
        break
    else:
        res=res+temp[0][1]
        last=temp[0][0]
        if temp[0][1]=='L':
            lt+=1
        else:
            rt-=1
    temp.clear()
print(len(res))
print(res)
            


# In[ ]:




