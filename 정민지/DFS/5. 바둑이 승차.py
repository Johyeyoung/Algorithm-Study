import sys

#sys.stdin = open("input.txt", "rt")

# 나의 풀이 -> 시간 초과
# L : weight[L]이 원소로 들어간다 vs 들어가지 않는다
# sum : 트럭에 타는 강아지의 무게
def DFS(L, sum):
    if c < sum:
        return

    if L == n:
        result.append(sum) # 아마도 이 부분 때문에@

    else:
        DFS(L+1, sum + weight[L])   # 원소로 들어감
        DFS(L+1, sum)   # 원소로 들어가지 않음

# 강의 풀이 : result를 전역변수로!
# tsum : 현재 레벨까지 적용한 원소들의 합
def DFS2(L, sum, tsum):
    global result
    if sum + (total-tsum) < result: # sum + 앞으로 더해야 할 원소들의 합이 result보다 작다면 cut
        return                      # => result가 최대값이 되야하므로 남은 경우의 수가 모두 result보다 작다면 확인할 필요 x
    if c < sum:
        return

    if L == n:
        result = max(result, sum)   # 에러 안남!
        # result에 값을 재할당하기 때문에 여기서 result를 지역변수로 인식하여 에러 발생한 것!
        # => main문에서 선언했던 result를 불러와야하기 때문에 전역변수로 선언해야 함
    else:
        DFS2(L+1, sum + weight[L], tsum+weight[L])   # 원소로 들어감
        DFS2(L+1, sum, tsum+weight[L])   # 원소로 들어가지 않음


if __name__ == "__main__":
    c, n = map(int, input().split())
    weight = [int(input()) for _ in range(n)]
    result = -1
    total = sum(weight)
    DFS2(0, 0, 0)
    print(result)















