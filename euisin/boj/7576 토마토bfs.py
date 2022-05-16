import sys
from collections import deque
input = sys.stdin.readline

m,n = map(int,input().strip().split())

board = []
q = deque()
for i in range(n):
    items = list(map(int,input().strip().split()))
    board.append(items)
    for j in range(m):
        if items[j] == 1:
            q.append((i,j))
#0 = 익지 않은 토마토 -1토마토 X 1 익은 토마토
#0이 모두 1이 되지 못하는 상황이면 -1
#0이 모두 1이 되는 날짜수

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    global board
    global q
    while q:
        x,y = q.popleft()
        val = board[x][y]
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny] == 0:
                board[nx][ny] = val+1
                q.append((nx,ny))
bfs()
result = 0
for i in board:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result, max(i))
print(result-1)