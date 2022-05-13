# 1463
# PR 220513 JAEMIN
# AUTH 220505 JAEMIN

X = int(input())
dp = [0,0,1,1]


for idx in range(4,X+1):
    min_arr = [float('inf'),float('inf'),float('inf')]

    if idx%2 == 0:
        min_arr[0] = 1 + dp[int(idx/2)]
    
    if idx%3 == 0:
        min_arr[1] = 1 + dp[int(idx/3)]

    min_arr[2] = 1 + dp[idx - 1]
    dp.append(min(min_arr))
print(dp[X])