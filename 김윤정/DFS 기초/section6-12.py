#itertoole를 이용한 수열 추측하기

import itertools as it

n,f = map(int, input())
b=[1]*n
for i in range(1, n):
    b[i]=b[i-1]*(n-i)/i
a= list(range(1, n+1))
for tmp in it.permutations(a):
    sum=0
    for L, x in enumerate(tmp):
        sum+=(x*b[L])
    if sum==f:
        for x in tmp:
            print(x, end=" ")
        break

