import sys

#sys.stdin = open("input.txt", "rt")
N = int(input())
words = []

for _ in range(N):
    words.append(input())   # 단어 words에 저장

for _ in range(N-1):    # words에서 시에 쓰인 단어 지움
    w = input()
    if w in words:
        words.remove(w)

print(words[0]) # 남은 단어 출력

