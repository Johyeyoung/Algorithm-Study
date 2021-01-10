# 두 리스트 합치기

#방법 1
a=[1,3,5]
b=[2,3,6,7,9]

c=a+b

c.sort()

print(c)

#방법 2
n=3
m=5
a=[1,3,5]
b=[2,3,6,7,9]
p1=p2=0
d=[]

while p1<n and p2<m:
    if a[p1]<=b[p2]:
        d.append(a[p1])
        p1+=1
    else:
        d.append(b[p2])
        p2+=1

if p1<n:
    d=d+a[p1:]
if p2<m:
    d=d+b[p2:]

print(d)



