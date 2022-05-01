import sys
nickname = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())
rings = []
for i in range(n):
    rings.append(sys.stdin.readline().rstrip()*2)
cnt = 0
for i in rings:
    if i.find(nickname) != -1:
        cnt += 1
print(cnt)
