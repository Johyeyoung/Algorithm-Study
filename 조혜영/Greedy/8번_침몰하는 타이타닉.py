import sys
from collections import deque
sys.stdin=open("input.txt", "r")
n, limit=map(int, input().split())

# 사람의 몸무게 정보를 담는 배열선언 & 오름차순정렬
p=list(map(int, input().split()))
p.sort()

# list로 만들면 자료를 빼거나 넣으면 전체가 이동을 해야하므로 불필요한 연산 生 
# deque는 list대용으로 자료를 추가하거나 삭제하여도 자료 자체가 
# 이동하는 것이 아닌 포인터로 가리키는것이라 이걸 사용!
p=deque(p)



cnt=0 # 구명보트의 개수

# 모든 인원이 다 탈출할때까지 ~
while p:
    
    # ------- 예외처리 :인원이 1명 남은 경우 
    if len(p)==1:
        cnt+=1
        break
    
    # -------------------------------------------------
    # 최대 몸무게 기준으로 탈출 시킬때 혹시 최소 몸무게를 합해서 탈출할 수 있나 확인 
    # 탈출할 때마다 구명보트cnt의 수 += 1
    if p[0]+p[-1]>limit:
        p.pop() # 최대 몸무게 한명만 탈출
        cnt+=1
    
    else:
        # deque에서 맨 앞자리를 꺼내는 방법 (list는 pop())
        p.popleft() # 최소 몸무게의 사람 탈출
        p.pop() # 최대 몸무게의 사람도 탈출 
        cnt+=1
print(cnt)

