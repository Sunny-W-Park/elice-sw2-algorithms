def solution(progresses, speeds):
    # calculate number of days left until release for each progress
    release_day = []
    for i in range(len(progresses)):
        left_over = 100-progresses[i]
        speed = speeds[i]
        if left_over % speed == 0:
            release_day.append(left_over//speed)
        else:
            release_day.append(1+left_over//speed)
    # empty array for answer and stack
    ans = []
    stack = []
    for j in range(len(release_day)):
        if stack == []:  # if stack is empty, we add release day
            stack.append(release_day[j])
        else:
            # else if first value in stack is smaller than current value
            if stack[0] < release_day[j]:
                # we add the number of values in the stack
                # we empty stack to reset
                # we add the current value to the stack
                ans.append(len(stack))
                stack = []
                stack.append(release_day[j])

            else:
                # we add current value to the stack
                stack.append(release_day[j])
    ans.append(len(stack))
    return ans
