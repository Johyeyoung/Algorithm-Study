import sys
sys.stdin=open("input.txt", "r")
L=int(input())
a=list(map(int, input().split()))
m=int(input())
a.sort()
for _ in range(m): # 그냥 m바퀴만 돌면되니까 _로
    # 높이 조정을하고
    a[0]+=1
    a[L-1]-=1
    # 정렬을 한다
    a.sort()

print(a[L-1]-a[0])
