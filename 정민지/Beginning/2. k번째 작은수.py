import sys

# sys.stdin = open("input.txt", "rt")

T = int(input())

for t in range(T):
    lst = []
    N, s, e, k = map(int, input().split())
    lst = list(map(int, input().split()))
    lst = lst[s-1:e]
    lst.sort()
    print(f"#{t+1} {lst[k-1]}")






