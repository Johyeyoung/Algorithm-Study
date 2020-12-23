import sys
from collections import Counter

# sys.stdin = open("input.txt", "rt")
N = int(input())
score_lst = []

for i in range(N):
    lst = list(map(int, input().split()))
    c = Counter(lst)
    score = 0
    #1. 규칙(1)
    if len(c) == 1:
        score = 10000 + lst[0] * 1000
    #2. 규칙(2)
    elif len(c) == 2:
        score = 1000 + c.most_common(1)[0][0] * 100
    #3. 규칙(3)
    elif len(c) == 3:
        score = max(lst) * 100

    score_lst.append(score)

print(max(score_lst))



