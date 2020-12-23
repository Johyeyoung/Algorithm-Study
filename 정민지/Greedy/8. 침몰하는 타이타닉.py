import sys

# sys.stdin = open("input.txt", "rt")
N, M = map(int, input().split())
weights = list(map(int, input().split()))
sum = 0
cnt = 0

# 1. 리스트 오름차순 정렬
weights.sort()

# 2. 리스트 맨 앞과 맨 뒤 합한 값과 M 비교
# 2-1 M보다 작다면 둘 다 pop
# 2-2 M보다 크다면 맨 뒤의 값 pop
while 0 < len(weights):
    # 주의!! 마지막 한 명 남았을 때 weights[0], weights[-1] 모두 같은 숫자
    # -> 두 번 pop할 경우 에러발생 => 따로 처리!
    if len(weights) == 1:
        cnt += 1
        break

    if weights[0] + weights[-1] <= M:
        weights.pop(0)
        weights.pop(-1)
        cnt += 1
    else:
        weights.pop(-1)
        cnt += 1

print(cnt)

# ** deque(앞 뒤로 추가/삭제 가능한 자료구조) 사용하면 더 효율적인 코드
# - deque.pop() : 맨 뒤 pop
# - deque.popleft() : 맨 왼쪽 pop









