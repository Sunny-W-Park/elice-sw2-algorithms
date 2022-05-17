import sys
sys.setrecursionlimit(10**6)  # dfs recursionlimit
M, N = map(int, sys.stdin.readline().split())  # M,N 입력
# 그래프 입력
graph = []
for i in range(M):
    graph.append(list(sys.stdin.readline().rstrip()))


# dfs 함수


def dfs(x, y):
    if x < 0 or y < 0 or x >= N or y >= M:  # 만약에 인자가 불가능하면 return하고 종료
        return
    if y == M-1:  # 만약에 y가 마지막 줄에 도달했다면 성공했다는 뜻
        global flag  # 성공여부 flag, global로 지정
        flag = "YES"  # flag를 yes로 바꾸고
        return  # 종료
    if graph[y][x] == "1":  # 1인경우 불가능 하므로 종료
        return
    if graph[y][x] == "0":  # 0인경우
        graph[y][x] = "1"  # visit했으니 1로 바꾸고
        dfs(x, y+1)  # 하
        dfs(x, y-1)  # 상
        dfs(x+1, y)  # 우
        dfs(x-1, y)  # 좌 탐색


# dfs 실행, 처음에는 flag를 NO로 지정
flag = "NO"
for i in range(N):  # 맨 윗줄에서 모든 x값 dfs 실행
    dfs(i, 0)
print(flag)
