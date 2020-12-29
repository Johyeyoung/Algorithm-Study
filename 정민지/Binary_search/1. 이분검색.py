import sys

# sys.stdin = open("input.txt", "rt")
N, M = map(int, input().split())
lst = list(map(int, input().split()))


# 이분검색
lower = 0
upper = N-1

while lower <= upper:
    mid = (lower + upper) // 2
    if lst[mid] == M:
        print(mid + 1)
        break
    elif lst[mid] < M:
        lower = mid + 1
    else:
        upper = mid - 1
        
# lst.sort()
# print(lst.index(M) + 1)
