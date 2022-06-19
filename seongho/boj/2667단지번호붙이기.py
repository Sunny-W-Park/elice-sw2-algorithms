# 그래프 입력
import sys
N = int(sys.stdin.readline())
graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

# dfs


def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= N:  # 불가능한 좌표면 종료
        return
    if graph[x][y] == 0:  # 방문을 했거나 집이 없다면 종료
        return
    if graph[x][y] == 1:  # 집이라면
        graph[x][y] = 0  # 방문처리
        global house
        house += 1  # 이어진 집의 개수에 1더하기
        # 상하좌우 반복
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)


result = 0  # 총 단지 수
house_array = []  # 각 단지마다 집의 수를 저장할 배열

# 그래프 전체 탐색
for i in range(N):
    for j in range(N):
        house = 0  # 단지의 집의 수 초기화
        if graph[i][j] == 1:  # 집이면
            dfs(i, j)  # dfs 탐색 - 연결된 집은 다 0으로 변환됨
            result += 1  # 단지 수에 1 추가
            house_array.append(house)  # dfs로 증가한 집 수를 배열에 추가

# 각 단지의 집의 수 정렬 (오름차순)
house_array.sort()

# 출력
print(result)
print(*house_array)
