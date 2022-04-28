#절대 반지

import sys
input = sys.stdin.readline

N = int(input())
B = list(map(int, input().split()))
A = [0] * N

A[0] = B[0]
for i in range(1, N):
    cum = sum(A[0 : i])
    A[i] = (i+1)*B[i] - cum

for i in A:
    print(i, end = ' ')
