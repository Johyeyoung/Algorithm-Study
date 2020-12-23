import sys

# sys.stdin = open("input.txt", "rt")

N, K = map(int, input().split())
cards = list(map(int, input().split()))
answers = []

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            n = cards[i] + cards[j] + cards[k]
            answers.append(n)

answers = set(answers)
answers = list(answers)
answers.sort(reverse=True)
print(answers[K-1])







