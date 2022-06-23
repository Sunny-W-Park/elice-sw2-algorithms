def solution(id_list, report, k):
    answer = []
    reporter = dict()
    reported = dict()
    s = set()
    for ids in id_list:
        reporter[ids] = 0
        reported[ids] = []

    for r in report:
        s.add(r)

    for i in s:
        a, b = i.split(" ")
        reported[b].append(a)

    for banned, prosecutor in reported.items():
        if (len(prosecutor) >= k):
            for pro in prosecutor:
                reporter[pro] += 1

    for val in reporter.values():
        answer.append(val)
    return answer
