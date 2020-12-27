import sys
sys.stdin=open("input.txt", "r")
n=int(input())
body=[]
for i in range(n):
    a, b=map(int, input().split())
    body.append((a, b))
    
# 키로 정렬을 해서 몸무게 변수만 고려하도록 한다.
body.sort(reverse=True) 

# 키순으로 정렬되어 있으므로 항상 다음 사람은 몸무게로 앞의 사람을 이겨야됨
# 앞의 몸무게를 ↓내려오면서 일일이 비교하는건 불필요
# 기존의 데이터 중 가장 큰 몸무게값을 기록해둔다. 그 값만 이기면 나머지는 다이김
# 이중 for문을 방지하고 하나의 for문으로 처리가 가능
largest=0
cnt=0
for x, y in body:
    if y>largest: # 몸무게가 앞의 기록의 최대보다 크면 
        largest=y
        cnt+=1
print(cnt)
