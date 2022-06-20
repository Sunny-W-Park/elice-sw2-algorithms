def solution(s):
    sol = len(s)
    for i in range(1, len(s)//2 + 2):
        word = ''
        currword = s[:i]
        count = 1

        for j in range(i, len(s)+i, i):
            if currword == s[j:j+i]:
                count += 1
            else:
                # 만약 다음 단어가 현재 단어가 아니라면
                if count == 1:
                    word += currword  # 글자가 1개면 숫자를 더하지 않고 그냥 추가
                else:
                    word += str(count) + currword
                    # 1개 이상이긴 한데 다음 단어가 아닐 때, 해당 글자의 카운트 + 글자
                currword = s[j: j+i]
                count = 1
                # 다음부터 이어질 새로운 단어를 만들고 count = 1로 초기화 후 건네줌

        sol = min(sol, len(word))
    return sol
