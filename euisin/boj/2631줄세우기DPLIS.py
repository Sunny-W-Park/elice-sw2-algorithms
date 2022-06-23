import sys
input = sys.stdin.readline

n = int(input())

arr = [0]*n
for i in range(n):
    arr[i] = int(input())

dp = [1 for i in range(n)]

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))