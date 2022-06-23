arr = []
for _ in range(6):
    arr.append(input())

sol = []

for i in range(6):
    curr = ["" * 1 for x in range(3)]
    curr[0] = arr[i]
    for j in range(6):
        if i == j:
            continue
        left = j
        right = 0
        while right < 6:
            if right == i or right == j:
                right += 1
                continue
            else:
                curr[1] = arr[left]
                curr[2] = arr[right]
                findingwords = [curr[0], curr[1], curr[2], curr[0][0] + curr[1][0] + curr[2][0],
                                curr[0][1] + curr[1][1] + curr[2][1], curr[0][2] + curr[1][2] + curr[2][2]]
                for word in arr:
                    if word in findingwords:
                        findingwords.remove(word)
                if not findingwords:
                    print(curr[0])
                    print(curr[1])
                    print(curr[2])
                    exit()
            right += 1

print(0)
