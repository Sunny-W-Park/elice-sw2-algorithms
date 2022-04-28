def solution(array, commands):
    answer = []
    for c in range(len(commands)):
        narr = []
        i = commands[c][0]
        j = commands[c][1]
        k = commands[c][2]
        for p in range(i-1, j):
            narr.append(array[p])
        narr = sorted(narr)
        answer.append(narr[k-1])
    return answer
