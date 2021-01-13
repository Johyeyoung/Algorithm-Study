import sys
import heapq as hq

# ** 최소힙 : 부모 노드값이 자식 노드값보다 작은 완전 이진트리
# - 채우기
# 레벨별로 채워나감(위에서 밑으로) 만일 부모 노드값이 더 크다면 자리 바꿈
# - 꺼내기
# 루트 노드부터 pop -> 가장 하위 레벨의 오른쪽의 노드값을 루트 노드로 옮김 -> 다시 최소 힙 만듦

# 강의 풀이
#sys.stdin = open("input.txt", "rt")
a = []

while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))    # 루트 노드 값 pop
    else:
        hq.heappush(a, n)