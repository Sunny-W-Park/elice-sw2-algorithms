# 11279
# PR 220519 JAEMIN
# AUTH 220519 JAEMIN

import heapq
import sys

input_list = list()
hq = list()
heapq.heapify(hq)
N = int(sys.stdin.readline())

for _ in range(N):
	input_list.append(int(sys.stdin.readline()))

for input_line in input_list:
	if input_line == 0:
		if len(hq) > 0:
			print(heapq.heappop(hq)[1])
		else:
			print(0)
	else:
		heapq.heappush(hq,(-input_line,input_line))
		
