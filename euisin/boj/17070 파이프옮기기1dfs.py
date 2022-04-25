#17070 파이프 옮기기 1

#통과하는 코드입니다. dfs입니다.
import sys
input = sys.stdin.readline
n = int(input().strip())
board = []
for i in range(n):
    board.append(list(map(int, input().strip().split())))
#0가로 1세로 2대각
result = 0
def dfs(x2,y2,d):
    global result
    if x2 == n-1 and y2 == n-1:
            result += 1
    if d == 0 or d == 2:
        ny2 = y2 + 1
        if ny2 < n and board[x2][ny2] == 0:
            dfs(x2, ny2, 0)

    if d == 1 or d ==2:
        nx2 = x2 + 1
        if nx2 < n and board[nx2][y2] == 0:
            dfs(nx2, y2, 1)
    nx2 =x2 + 1
    ny2 = y2 +1
    if nx2 < n and ny2 < n and board[nx2][ny2] == 0 and board[nx2][ny2 - 1] == 0 and board[nx2 - 1][ny2] == 0:
        dfs(nx2, ny2, 2)

if board[n-1][n-1] == 1:
    print(0)
else:
    dfs(0,1,0)
    print(result)
    
    
#70%에서 시간초과판정나는 코드입니다. bfs
import sys
from collections import deque
input = sys.stdin.readline
n = int(input().strip())
board = []
for i in range(n):
    board.append(list(map(int, input().strip().split())))
#0가로 1세로 2대각
def bfs():
    result = 0
    q = deque()
    q.append((0, 1, 0))
    while q:
        x2, y2, d = q.popleft()
        if x2 == n-1 and y2 == n-1:
            result += 1
            continue
        if d == 0 or d == 2:
            ny2 = y2 + 1
            if ny2 < n and board[x2][ny2] == 0:
                q.append((x2, ny2, 0))

        if d == 1 or d ==2:
            nx2 = x2 + 1
            if nx2 < n and board[nx2][y2] == 0:
                q.append((nx2, y2, 1))
        nx2 =x2 + 1
        ny2 = y2 +1
        if nx2 < n and ny2 < n and board[nx2][ny2] == 0 and board[nx2][ny2 - 1] == 0 and board[nx2 - 1][ny2] == 0:
            q.append((nx2, ny2, 2))
    print(result)
if board[n-1][n-1] == 1:
    print(0)
else:
    bfs()
