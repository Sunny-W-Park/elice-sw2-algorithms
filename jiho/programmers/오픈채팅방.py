def solution(record):
    answer = []
    idDic = dict()
    for rcd in record:
        temp = list(rcd.split(" "))
        if temp[0] == "Leave":
            continue
        else:
            idDic[temp[1]] = temp[2]
    for rcd in record:
        temp = list(rcd.split(" "))
        if temp[0] == "Change":
            continue
        else:
            if temp[0] == "Enter":
                answer.append(f'{idDic[temp[1]]}님이 들어왔습니다.')
            elif temp[0] == "Leave":
                answer.append(f'{idDic[temp[1]]}님이 나갔습니다.')
    return answer
