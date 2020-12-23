import sys
from collections import Counter

# sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
lst = []
for i in range(1, N+1):
    for j in range(1, M+1):
        num = i + j
        lst.append(num)

c = Counter(lst)
common = c.most_common(1)[0][1]
for key, val in c.items():
    if val == common:
        print(key, end=" ")









