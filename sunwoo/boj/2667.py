#2667

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
g = []
for _ in range(N):
    s = input()
    line = []
    for i in range(N):
        line.append(int(s[i]))
    g.append(line)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    count = 1
    g[x][y] = 999
    q = deque()
    q.append((x, y))
    while q:
        qx, qy = q.popleft()
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]
            if 0 <= nx <= N-1 and 0 <= ny <= N-1:
                if g[nx][ny] == 1:
                    g[nx][ny] = 999
                    count += 1
                    q.append((nx, ny))
    return count

result = []
for i in range(N):
    for j in range(N):
        if g[i][j] == 1:
            result.append(bfs(i, j))

print(len(result))
for i in sorted(result):
    print(i)
