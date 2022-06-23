n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    a = a % 10
    if a == 0:
        print(10)
    elif a in [1, 5, 6]:
        print(a)
    elif a in [2, 3, 7, 8]:
        print(pow(a, b, 10))
    elif a in [4, 9]:
        print(pow(a, b, 10))
