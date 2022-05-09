import sys
input = sys.stdin.readline

n, k = map(int,input().strip().split())

stuff = [(0,0)]
for i in range(n):
    a,b = map(int,input().strip().split())
    stuff.append((a,b))
knapsack = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    weight, value = stuff[i]
    for j in range(1,k+1):
        if j>=weight:
            knapsack[i][j] = max(knapsack[i-1][j], knapsack[i-1][j-weight]+ value)
        else:
            knapsack[i][j] = knapsack[i-1][j]
print(knapsack[n][k])