import sys
n=int(input())

# meeting 정보입력하기 
meeting=[]
for i in range(n):
    a, b=map(int, input().split())
    meeting.append((a, b)) # (시작 시간, 끝나는 시간)

# 끝나는 시간이 중요하므로 x[1]을 기준으로 오름차순 정렬    
# x[1]이 같으면 x[0]순으로 정렬
meeting.sort(key=lambda x : (x[1], x[0]))


et=0
cnt=0
for x, y in meeting:
    # 검사하는 회의의 시작시간이 진행되고 있는 회의의 끝나는 시간보다 크면 그 회의는 해도됨
    if x>=et: 
        et=y # 끝나는 시간 update
        cnt+=1 
print(cnt)
