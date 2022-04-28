# 김박사

import sys
input = sys.stdin.readline
N = int(input())

result = 0

for i in range(N):
    num = int(input())
    result += num

_print = ''

for i in range(10):
    _print += str(result)[i]

print(_print)
