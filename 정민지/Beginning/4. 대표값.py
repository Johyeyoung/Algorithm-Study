import sys

# sys.stdin = open("input.txt", "rt")

N = int(input())
scores = list(map(int, input().split()))
avg = int(sum(scores) / len(scores) + 0.5)
diff = float('inf')
result = -1

for i in range(N):
    if abs(avg - scores[i]) < diff:
        result = i+1
        diff = abs(avg - scores[i])

    elif abs(avg - scores[i]) == diff:
        if scores[result-1] < scores[i]:
            result = i + 1
            diff = abs(avg - scores[i])


print(f"{avg} {result}")







