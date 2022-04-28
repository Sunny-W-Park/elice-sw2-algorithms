import sys
input = sys.stdin.readline
n = int(input().strip())
result = 1
for i in range(n):
    x,y = map(int,input().strip().split())
    if x == y: #X와 Y가 같다면 continue
        continue
    elif x == result: #x가 1번떡이면 위치한 곳을 옮김
        result = y
        continue
    elif y == result: #y가 1번떡이면 위치한 곳을 옮김
        result = x
        continue
print(result) #최종 위치 프린트