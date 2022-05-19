#11279

import heapq
N = int(input())
arr = []
heapq.heapify(arr)
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(arr) == 0:
            print(0)
        else:
            y = heapq.heappop(arr)
            print(y * -1)
    else:
        heapq.heappush(arr, (x*-1))


