import sys
from collections import deque

#sys.stdin = open("input.txt", "rt")

# BFS : 출발점에서 목적지까지 최단 거리로 갈 때 사용
# => queue 사용!!
# 강의 풀이

s, e = map(int, input().split())
cnt = 0
res = 0
MAX = 10000
dis = [0] * (MAX+1)     # dis[idx] : 출발점(s)에서 idx까지 점프한 최소 횟수
ch = [0] * (MAX+1)      # 무조건 처음 방문한 점프만 들어가도록(최소 횟수이기 때문)
ch[s] = 1   # 출발점
dQ = deque()
dQ.append(s)

while dQ:
    now = dQ.popleft()
    if now == e:
        break
    for next in (now-1, now+1, now+5):
        if 0 < next <= MAX:
            if ch[next] == 0:
                dQ.append(next)
                ch[next] = 1
                dis[next] = dis[now] + 1
print(dis[e])



















