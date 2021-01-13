import sys
import heapq as hq

# ** 최대힙 : 부모 노드값이 자식 노드값보다 큰 완전 이진트리
# - 채우고 꺼낼 때 최소힙과 똑같다 단, 숫자에 - 부호 붙일 것!
# 3, 4에 - 붙이면 -3 > -4이므로 -4가 부모 노드가 된다


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
            print(-hq.heappop(a))    # 루트 노드 값 pop
    else:
        hq.heappush(a, -n)
