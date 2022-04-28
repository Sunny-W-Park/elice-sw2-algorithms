# 절대 반지

nickname = input()
N = int(input())
cnt = 0
for _ in range(N):
    t = str(input())
    t = t + t[0:len(nickname)-1]
    print()
    print(t)
    for i in range(0, len(t)-2):
        if t[i:i+len(nickname)] == nickname:
            cnt += 1
print(cnt)
