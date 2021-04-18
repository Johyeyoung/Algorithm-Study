# 뱀과 사다리 게임 (00:18:34)

from collections import deque
n, m = map(int, input().split())
after = list(range(101))
dist = [-1]*101
for _ in range(n+m):
    x, y = map(int, input().split())
    after[x] = y
dist[1] = 0
q = deque()
q.append(1)
while q:
    x = q.popleft()
    for i in range(1, 6+1):
        y = x+i
        if y > 100:
            continue
        y = after[y]
        if dist[y] == -1:
            dist[y] = dist[x] + 1
            q.append(y)
print(dist[100])


# ---------------------------------------------------------------------------
# 데스 나이트 (00:09:55)

from collections import deque
dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]
dist = [[-1]*200 for _ in range(200)]
n = int(input())
sx,sy,ex,ey = map(int,input().split())
q = deque()
q.append((sx,sy))
dist[sx][sy] = 0
while q:
    x,y = q.popleft()
    for k in range(6):
        nx,ny = x+dx[k],y+dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if dist[nx][ny] == -1:
                q.append((nx,ny))
                dist[nx][ny] = dist[x][y] + 1
print(dist[ex][ey])


# ---------------------------------------------------------------------------
# 연구소 (00:09:55) BFS

from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(a):
    n = len(a)
    m = len(a[0])
    b = [[0]*m for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(m):
            b[i][j] = a[i][j]
            if b[i][j] == 2:
                q.append((i,j))
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m and b[nx][ny] == 0:
                b[nx][ny] = 2
                q.append((nx,ny))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if b[i][j] == 0:
                cnt += 1
    return cnt

n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for x1 in range(n):
    for y1 in range(m):
        if a[x1][y1] != 0:
            continue
        for x2 in range(n):
            for y2 in range(m):
                if a[x2][y2] != 0:
                    continue
                for x3 in range(n):
                    for y3 in range(m):
                        if a[x3][y3] != 0:
                            continue
                        if x1 == x2 and y1 == y2:
                            continue
                        if x1 == x3 and y1 == y3:
                            continue
                        if x2 == x3 and y2 == y3:
                            continue
                        a[x1][y1] = 1
                        a[x2][y2] = 1
                        a[x3][y3] = 1
                        cur = bfs(a)
                        if ans < cur:
                            ans = cur
                        a[x1][y1] = 0
                        a[x2][y2] = 0
                        a[x3][y3] = 0
print(ans)

# ---------------------------------------------------------------------------
# 연구소 (00:09:55) DFS

from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs(b, x, y):
    for k in range(4):
        nx,ny = x+dx[k],y+dy[k]
        if 0 <= nx < n and 0 <= ny < m and b[nx][ny] == 0:
            b[nx][ny] = 2
            dfs(b, nx,ny)

def go():
    b = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            b[i][j] = a[i][j]
    for i in range(n):
        for j in range(m):
            if b[i][j] == 2:
                dfs(b, i, j)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if b[i][j] == 0:
                cnt += 1
    return cnt
n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for x1 in range(n):
    for y1 in range(m):
        if a[x1][y1] != 0:
            continue
        for x2 in range(n):
            for y2 in range(m):
                if a[x2][y2] != 0:
                    continue
                for x3 in range(n):
                    for y3 in range(m):
                        if a[x3][y3] != 0:
                            continue
                        if x1 == x2 and y1 == y2:
                            continue
                        if x1 == x3 and y1 == y3:
                            continue
                        if x2 == x3 and y2 == y3:
                            continue
                        a[x1][y1] = 1
                        a[x2][y2] = 1
                        a[x3][y3] = 1
                        cur = go()
                        if ans < cur:
                            ans = cur
                        a[x1][y1] = 0
                        a[x2][y2] = 0
                        a[x3][y3] = 0
print(ans)

# ---------------------------------------------------------------------------
# 돌 그룹 (00:16:13)

import sys
sys.setrecursionlimit(1500*1500)
check = [[False]*1501 for _ in range(1501)]
x,y,z = map(int,input().split())
s = x+y+z
def go(x, y):
    if check[x][y]:
        return
    check[x][y] = True
    a = [x, y, s-x-y]
    for i in range(3):
        for j in range(3):
            if a[i] < a[j]:
                b = [x, y, s-x-y]
                b[i] += a[i]
                b[j] -= a[i]
                go(b[0], b[1])
if s % 3 != 0:
    print(0)
else:
    go(x,y)
    if check[s//3][s//3]:
        print(1)
    else:
        print(0)

# ---------------------------------------------------------------------------
# 벽 부수고 이동하기 (00:16:13)
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n,m = map(int,input().split())
a = [list(map(int,list(input()))) for _ in range(n)]
dist = [[[0]*2 for j in range(m)] for i in range(n)]
q = deque()
q.append((0,0,0))
dist[0][0][0] = 1
while q:
    x,y,z = q.popleft()
    for k in range(4):
        nx,ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == 0 and dist[nx][ny][z] == 0:
                dist[nx][ny][z] = dist[x][y][z] + 1
                q.append((nx,ny,z))
            if z == 0 and a[nx][ny] == 1 and dist[nx][ny][z+1] == 0:
                dist[nx][ny][z+1] = dist[x][y][z] + 1
                q.append((nx,ny,z+1))

if dist[n-1][m-1][0] != 0 and dist[n-1][m-1][1]  != 0:
    print(min(dist[n-1][m-1]))
elif dist[n-1][m-1][0] != 0:
    print(dist[n-1][m-1][0])
elif dist[n-1][m-1][1] != 0:
    print(dist[n-1][m-1][1])
else:
    print(-1)



# ---------------------------------------------------------------------------
# 벽 부수고 이동하기 4 (00:11:12)

from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n, m = map(int,input().split())
a = [list(map(int,list(input()))) for _ in range(n)]
group = [[-1]*m for _ in range(n)]
check = [[False]*m for _ in range(n)]
group_size = []
def bfs(sx, sy):
    g = len(group_size)
    q = deque()
    q.append((sx,sy))
    group[sx][sy] = g
    check[sx][sy] = True
    cnt = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if check[nx][ny] == False and a[nx][ny] == 0:
                    check[nx][ny] = True
                    group[nx][ny] = g
                    q.append((nx,ny))
                    cnt += 1
    
    group_size.append(cnt)

for i in range(n):
    for j in range(m):
        if a[i][j] == 0 and check[i][j] == False:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            print(0, end='')
        else:
            near = set()
            for k in range(4):
                nx,ny = i+dx[k],j+dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if a[nx][ny] == 0:
                        near.add(group[nx][ny])
            ans = 1
            for g in near:
                ans += group_size[g]
            print(ans%10, end='')
    print()



# ---------------------------------------------------------------------------
# 벽 부수고 이동하기 2 (00:13:42)
from collections import deque
a = [[0]*1000 for _ in range(1000)]
d = [[[0]*11 for i in range(1000)] for j in range(1000)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n,m,l = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,list(input()))))
q = deque()
d[0][0][0] = 1
q.append((0,0,0))
while q:
    x,y,z = q.popleft()
    for k in range(4):
        nx,ny = x+dx[k], y+dy[k]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if a[nx][ny] == 0 and d[nx][ny][z] == 0:
            d[nx][ny][z] = d[x][y][z] + 1
            q.append((nx,ny,z))
        if z+1 <= l and a[nx][ny] == 1 and d[nx][ny][z+1] == 0:
            d[nx][ny][z+1] = d[x][y][z] + 1
            q.append((nx,ny,z+1))
ans = -1
for i in range(l+1):
    if d[n-1][m-1][i] == 0:
        continue
    if ans == -1:
        ans = d[n-1][m-1][i]
    elif ans > d[n-1][m-1][i]:
        ans = d[n-1][m-1][i]
print(ans)


# ---------------------------------------------------------------------------
# 벽 부수고 이동하기 3 (00:13:42)
from collections import deque
a = [[0]*1000 for _ in range(1000)]
d = [[[[0]*2 for k in range(11)] for i in range(1000)] for j in range(1000)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n,m,l = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,list(input()))))
q = deque()
d[0][0][0][0] = 1
q.append((0,0,0,0))
while q:
    x,y,z,night = q.popleft()
    for k in range(4):
        nx,ny = x+dx[k], y+dy[k]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if a[nx][ny] == 0 and d[nx][ny][z][1-night] == 0:
            d[nx][ny][z][1-night] = d[x][y][z][night] + 1
            q.append((nx,ny,z,1-night))
        if night == 0 and z+1 <= l and a[nx][ny] == 1 and d[nx][ny][z+1][1-night] == 0:
            d[nx][ny][z+1][1-night] = d[x][y][z][night] + 1
            q.append((nx,ny,z+1,1-night))
    if d[x][y][z][1-night] == 0:
        d[x][y][z][1-night] = d[x][y][z][night] + 1
        q.append((x,y,z,1-night))
ans = -1
for j in range(2):
    for i in range(l+1):
        if d[n-1][m-1][i][j] == 0:
            continue
        if ans == -1:
            ans = d[n-1][m-1][i][j]
        elif ans > d[n-1][m-1][i][j]:
            ans = d[n-1][m-1][i][j]
print(ans)



# ---------------------------------------------------------------------------
# 움직이는 미로 탈출 (00:13:42)

from collections import deque
dx = [0,0,1,-1,1,-1,1,-1,0]
dy = [1,-1,0,0,1,1,-1,-1,0]
n = 8
a = [input() for _ in range(n)]
q = deque()
check = [[[False]*(n+1) for j in range(n)] for i in range(n)]
check[7][0][0] = True
q.append((7,0,0))
ans = False

while q:
    x,y,t = q.popleft()
    if x == 0 and y == 7:
        ans = True
    for k in range(9):
        nx,ny = x+dx[k],y+dy[k]
        nt = min(t+1, 8)
        if 0 <= nx < n and 0 <= ny < n:
            if nx-t >= 0 and a[nx-t][ny] == '#':
                continue
            if nx-t-1 >= 0 and a[nx-t-1][ny] == '#':
                continue
            if check[nx][ny][nt] == False:
                check[nx][ny][nt] = True
                q.append((nx,ny,nt))

print(1 if ans else 0)


# ---------------------------------------------------------------------------
# 아기 상어 (00:13:22)
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(a, x, y, size):
    n = len(a)
    ans = []
    d = [[-1]*n for _ in range(n)]
    q = deque()
    q.append((x,y))
    d[x][y] = 0
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if 0 <= nx < n and 0 <= ny < n and d[nx][ny] == -1:
                ok = False
                eat = False
                # 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다.
                if a[nx][ny] == 0: 
                    ok = True
                elif a[nx][ny] < size: # 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 
                    ok = True
                    eat = True
                elif a[nx][ny] == size: # 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
                    ok = True
                if ok:
                    q.append((nx,ny))
                    d[nx][ny] = d[x][y] + 1
                    if eat:
                        ans.append((d[nx][ny],nx,ny))
    if not ans:
        return None
    ans.sort()
    return ans[0]

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
x,y = 0,0
for i in range(n):
    for j in range(n):
        if a[i][j] == 9:
            x,y = i,j
            a[i][j] = 0
ans = 0
size = 2
exp = 0
while True:
    p = bfs(a, x, y, size)
    if p is None:
        break
    dist, nx, ny = p
    a[nx][ny] = 0
    ans += dist
    exp += 1
    if size == exp:
        size += 1
        exp = 0
    x,y = nx,ny
print(ans)

# ---------------------------------------------------------------------------
# 레이저 통신 (00:14:34)
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
m,n = map(int,input().split())
a = [input() for _ in range(n)]
sx=sy=ex=ey=-1
for i in range(n):
    for j in range(m):
        if a[i][j] == 'C':
            if sx == -1:
                sx,sy = i,j
            else:
                ex,ey = i,j
dist = [[-1]*m for _ in range(n)]
q = deque()
dist[sx][sy] = 0
q.append((sx,sy))
while q:
    x,y = q.popleft()
    for k in range(4):
        nx,ny = x+dx[k],y+dy[k]
        while 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == '*':
                break
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx,ny))
            nx += dx[k]
            ny += dy[k]
print(dist[ex][ey]-1)

# ---------------------------------------------------------------------------
# 소수 경로 (00:14:34)

#!/usr/bin/python3
from collections import deque
def change(num, index, digit):
    if index == 0 and digit == 0:
        return -1
    s = list(str(num))
    s[index] = chr(digit+ord('0'))
    return int(''.join(s))
prime = [False] * 10001

for i in range(2, 10001):
    if prime[i] == False:
        for j in range(i*i, 10001, i):
            prime[j] = True
for i in range(10001):
    prime[i] = not prime[i]

t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    c = [False] * 10001
    d = [0] * 10001
    d[n] = 0
    c[n] = True
    q = deque()
    q.append(n)
    while q:
        now = q.popleft()
        for i in range(4):
            for j in range(10):
                nxt = change(now, i, j)
                if nxt != -1:
                    if prime[nxt] and c[nxt] == False:
                        q.append(nxt)
                        d[nxt] = d[now] + 1
                        c[nxt] = True
    print(d[m])

# ---------------------------------------------------------------------------
# 적록색약 (00:14:34)

from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def can(blind, u, v):
    if u == v:
        return True
    if blind:
        if u == 'R' and v == 'G':
            return True
        if u == 'G' and v == 'R':
            return True
    return False

def go(a, blind):
    n = len(a)
    check = [[False]*n for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            if check[i][j]:
                continue
            ans += 1
            q = deque()
            q.append((i,j))
            check[i][j] = True
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx,ny = x+dx[k], y+dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if check[nx][ny]:
                            continue
                        if can(blind, a[x][y], a[nx][ny]):
                            check[nx][ny] = True
                            q.append((nx,ny))
    return ans

n = int(input())
a = [input() for _ in range(n)]
print(str(go(a, False)) + ' ' + str(go(a, True)))


# ---------------------------------------------------------------------------
# 4 연산 (00:15:55)
from collections import deque
limit = 1000000000
s,t = map(int,input().split())
check = set()
q = deque()
q.append((s,''))
check.add(s)
while q:
    x, s = q.popleft()
    if x == t:
        if len(s) == 0:
            s = '0'
        print(s)
        exit()
    if 0 <= x*x <= limit and x*x not in check:
        q.append((x*x,s+'*'))
        check.add(x*x)
    if 0 <= x+x <= limit and x+x not in check:
        q.append((x+x,s+'+'))
        check.add(x+x)
    if 0 <= x-x <= limit and x-x not in check:
        q.append((x-x,s+'-'))
        check.add(x-x)
    if x != 0 and 0 <= x//x <= limit and x//x not in check:
        q.append((x//x,s+'/'))
        check.add(x//x)
print(-1)

# ---------------------------------------------------------------------------
# 스타트링크 (00:15:55)
from collections import deque
f,s,g,u,d = map(int, input().split())
check = [False] * (f+1)
dist = [0] * (f+1)
q = deque()
q.append(s)
check[s] = True
while q:
    now = q.popleft()
    if now+u <= f and not check[now+u]:
        dist[now+u] = dist[now] + 1
        check[now+u] = True
        q.append(now+u)
    if now-d >= 1 and not check[now-d]:
        dist[now-d] = dist[now] + 1
        check[now-d] = True
        q.append(now-d)
if check[g]:
    print(dist[g])
else:
    print('use the stairs')

# ---------------------------------------------------------------------------
# 탈옥 (00:15:55)
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(a, x, y):
    n = len(a)
    m = len(a[0])
    dist = [[-1]*m for _ in range(n)]
    q = deque()
    q.append((x,y))
    dist[x][y] = 0
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1 and a[nx][ny] != '*':
                if a[nx][ny] == '#':
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))
                else:
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx,ny))
    return dist

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = ['.'+input()+'.' for _ in range(n)]
    n += 2
    m += 2
    a = ['.'*m] + a + ['.'*m]
    d0 = bfs(a, 0, 0)
    x1=y1=x2=y2=-1
    for i in range(n):
        for j in range(m):
            if a[i][j] == '$':
                if x1 == -1:
                    x1,y1 = i,j
                else:
                    x2,y2 = i,j
    d1 = bfs(a,x1,y1)
    d2 = bfs(a,x2,y2)
    ans = n*m

    for i in range(n):
        for j in range(m):
            if a[i][j] == '*':
                continue
            if d0[i][j] == -1 or d1[i][j] == -1 or d2[i][j] == -1:
                continue
            cur = d0[i][j] + d1[i][j] + d2[i][j]
            if a[i][j] == '#':
                cur -= 2
            ans = min(ans,cur)
    print(ans)


# ---------------------------------------------------------------------------
# 말이 되고픈 원숭이 (00:18:54)

from collections import deque
dx = [0,0,1,-1,-2,-1,1,2,2,1,-1,-2]
dy = [1,-1,0,0,1,2,2,1,-1,-2,-2,-1]
cost = [0,0,0,0,1,1,1,1,1,1,1,1]
a = [[0]*200 for _ in range(200)]
d = [[[-1]*31 for i in range(200)] for j in range(200)]
l = int(input())
m,n = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
q = deque()
q.append((0,0,0))
d[0][0][0] = 0
while q:
    x,y,c = q.popleft()
    for k in range(12):
        nx = x+dx[k]
        ny = y+dy[k]
        nc = c+cost[k]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == 1:
                continue
            if nc <= l:
                if d[nx][ny][nc] == -1:
                    d[nx][ny][nc] = d[x][y][c] + 1
                    q.append((nx,ny,nc))
ans = -1
for i in range(l+1):
    if d[n-1][m-1][i] == -1:
        continue
    if ans == -1 or ans > d[n-1][m-1][i]:
        ans = d[n-1][m-1][i]
print(ans)


# ---------------------------------------------------------------------------
# 아기 상어 2 (00:18:54)

#!/usr/bin/python3
from collections import deque
dx = [0,0,1,-1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]
n, m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
def go(sx, sy):
    d = [[-1]*m for _ in range(n)]
    d[sx][sy] = 0
    q = deque()
    q.append((sx,sy))
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if d[nx][ny] == -1:
                    if a[nx][ny] == 1:
                        return d[x][y] + 1
                    else:
                        q.append((nx,ny))
                        d[nx][ny] = d[x][y] + 1

    return 0


ans = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            dist = go(i, j)
            if ans < dist:
                ans = dist
print(ans)



# ---------------------------------------------------------------------------
# 로봇 청소기 (00:18:54)
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1

    a[i-1],a[j] = a[j],a[i-1]

    j = len(a)-1
    while i < j:
        a[i],a[j] = a[j],a[i]
        i += 1
        j -= 1

    return True

def bfs(a, sx, sy):
    n = len(a)
    m = len(a[0])
    dist = [[-1]*m for _ in range(n)]
    q = deque()
    q.append((sx,sy))
    dist[sx][sy] = 0
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if dist[nx][ny] == -1 and a[nx][ny] != 'x':
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))
    return dist

while True:
    m,n = map(int,input().split())
    if n == 0 and m == 0:
        break
    a = [input() for _ in range(n)]
    b = [(0,0)]
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'o':
                b[0] = (i,j)
            elif a[i][j] == '*':
                b.append((i,j))
    l = len(b)
    d = [[0]*l for _ in range(l)]
    ok = True
    for i in range(l):
        dist = bfs(a,b[i][0], b[i][1])
        for j in range(l):
            d[i][j] = dist[b[j][0]][b[j][1]]
            if d[i][j] == -1:
                ok = False
    if not ok:
        print(-1)
        continue
    p = [i+1 for i in range(l-1)]
    ans = -1
    while True:
        now = d[0][p[0]]
        for i in range(l-2):
            now += d[p[i]][p[i+1]]
        if ans == -1 or ans > now:
            ans = now
        if not next_permutation(p):
            break
    print(ans)
    


# ---------------------------------------------------------------------------
# 성곽 (00:10:39)

from collections import deque
dx = [0,-1,0,1]
dy = [-1,0,1,0]
m,n = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
d = [[0]*m for _ in range(n)]
def bfs(x, y, rooms):
    q = deque()
    q.append((x,y))
    d[x][y] = rooms
    cnt = 0
    while q:
        x,y = q.popleft()
        cnt += 1
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if d[nx][ny] != 0:
                continue
            if (a[x][y] & (1<<k)) > 0:
                continue
            q.append((nx,ny))
            d[nx][ny] = rooms
    return cnt
rooms = 0
room = [0]
for i in range(n):
    for j in range(m):
        if d[i][j] == 0:
            rooms += 1
            room.append((bfs(i,j,rooms)))
print(rooms)
ans = 0
for i in range(1,rooms+1):
    if ans < room[i]:
        ans = room[i]
print(ans)
ans = 0
for i in range(n):
    for j in range(m):
        x,y = i,j
        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if d[nx][ny] == d[x][y]:
                continue
            if (a[x][y] & (1<<k)) > 0:
                if ans < room[d[x][y]]+room[d[nx][ny]]:
                    ans = room[d[x][y]]+room[d[nx][ny]]
print(ans)

# ---------------------------------------------------------------------------
# 새로운 하노이 탑 (00:10:39)

from collections import deque
s = []
for i in range(3):
    temp = input().split()
    cnt = int(temp[0])
    if cnt > 0:
        s.append(temp[1])
    else:
        s.append('')
cnt = [0,0,0]
for i in range(3):
    for ch in s[i]:
        cnt[ord(ch)-ord('A')] += 1
d = dict()
q = deque()
q.append(tuple(s))
d[tuple(s)] = 0
while q:
    x = q.popleft()
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            if len(x[i]) == 0:
                continue
            y = list(x[:])
            y[j] = y[j] + x[i][-1]
            y[i] = y[i][:-1]
            y = tuple(y)
            if y not in d:
                d[y] = d[x] + 1
                q.append(y)

ans = ['', '', '']
for i in range(3):
    for j in range(cnt[i]):
        ans[i] += chr(ord('A')+i)
print(d[tuple(ans)])


# ---------------------------------------------------------------------------
# 연구소 2 (00:09:01)

from collections import deque
n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
candi = []
ans = -1
for i in range(n):
    for j in range(n):
        if a[i][j] == 2:
            a[i][j] = 0
            candi.append((i,j))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    d = [[-1]*n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if a[i][j] == 3:
                q.append((i,j))
                d[i][j] = 0
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] != 1 and d[nx][ny] == -1:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx,ny))
    cur = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] != 1:
                if d[i][j] == -1:
                    return
                if cur < d[i][j]:
                    cur = d[i][j]
    global ans
    if ans == -1 or ans > cur:
        ans = cur


def go(index, cnt):
    if index == len(candi):
        if cnt == m:
            bfs()
    else:
        x,y = candi[index]
        a[x][y] = 3
        go(index+1, cnt+1)
        a[x][y] = 0
        go(index+1, cnt)

go(0,0)
print(ans)


# ---------------------------------------------------------------------------
# 연구소 3 (00:09:01)

from collections import deque
n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
candi = []
ans = -1
for i in range(n):
    for j in range(n):
        if a[i][j] == 2:
            # 차이 1 (연구소 2는 a[i][j] = 0; 이 적혀있음)
            candi.append((i,j))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    d = [[-1]*n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if a[i][j] == 3:
                q.append((i,j))
                d[i][j] = 0
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] != 1 and d[nx][ny] == -1:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx,ny))
    cur = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] == 0: # 차이 3
                if d[i][j] == -1:
                    return
                if cur < d[i][j]:
                    cur = d[i][j]
    global ans
    if ans == -1 or ans > cur:
        ans = cur


def go(index, cnt):
    if index == len(candi):
        if cnt == m:
            bfs()
    else:
        x,y = candi[index]
        a[x][y] = 3
        go(index+1, cnt+1)
        a[x][y] = 2 # 차이 2
        go(index+1, cnt)

go(0,0)
print(ans)
