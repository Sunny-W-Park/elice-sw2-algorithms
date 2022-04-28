import math

def solution(progresses, speeds):
    answer = []
    stack = []
    stack.append(math.ceil((100 - progresses[0]) / speeds[0]))
    for i in range(1, len(progresses)):
        comp = stack[0]
        nq = math.ceil((100 - progresses[i]) / speeds[i])
        if comp >= nq:
            stack.append(nq)
        else:
            answer.append(len(stack))
            stack = []
            stack.append(nq)
    answer.append(len(stack))
    return answer
