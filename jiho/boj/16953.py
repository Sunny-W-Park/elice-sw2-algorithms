a, b = map(int, input().split())

count = 0
while a < b:
    if str(b)[-1] == "1":
        b = str(b)
        b = int(b[:len(b)-1])
        count += 1
    else:
        if b % 2 != 0:
            count = 0
            break
        else:
            b = b // 2
            count += 1
    if a == b:
        break
    elif a > b:
        count = 0
        break
if count == 0:
    print(-1)
else:
    print(count+1)
