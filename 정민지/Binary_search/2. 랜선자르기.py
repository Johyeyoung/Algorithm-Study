import sys

# ** 답이 어떤 범위 내에 존재할 때쟇 => 이분 검색

# sys.stdin = open("input.txt", "rt")
K, N = map(int, input().split())
lst = []
for i in range(K):
    lst.append(int(input()))

lower = 1
upper = max(lst)
cnt = 0  # 1 ~ 가장 긴 랜선의 길이 중 xcm 로 잘랐을 때 K개가 나와야 함
result = 0

while lower <= upper:   # 답이 될 수 있는 범위
    cnt = 0     # 주어진 랜선을 xcm로 잘랐을 때 나오는 개수
    mid = (lower + upper) // 2  # 답이 될 수 있는
    for i in range(K):
        cnt += lst[i] // mid

    if cnt < N:     # 총 개수가 N보다 작을 때 - 답의 최대 범위를 더 작게 함
        upper = mid - 1
    else:           # 총 개수가 N보다 같거나 클 때 - 답이 될 수 있고, 더 큰 수치로 자를 수 있는 지 검사
        lower = mid + 1        # 답의 최소 범위를 늘림
        result = mid

print(result)


























