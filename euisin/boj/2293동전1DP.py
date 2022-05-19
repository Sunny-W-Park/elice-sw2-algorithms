import sys
input = sys.stdin.readline

n,k = map(int,input().strip().split())
coins = [0]*n
for i in range(n):
    coins[i] = int(input().strip())
dp = [0]*(k+1)
dp[0] = 1
for coin in coins:
    for i in range(coin,k+1):
        if i-coin>=0:
            dp[i] += dp[i-coin]
print(dp[k])