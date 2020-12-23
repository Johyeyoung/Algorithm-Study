import sys

# sys.stdin = open("input.txt", "rt")
L = int(input())
lst = list(map(int, input().split()))
M = int(input())

for i in range(M):
    max_height = max(lst)
    min_height = min(lst)
    lst[lst.index(max_height)] -= 1
    lst[lst.index(min_height)] += 1

print(max(lst) - min(lst))











