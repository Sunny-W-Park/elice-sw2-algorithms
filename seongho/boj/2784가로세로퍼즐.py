from itertools import permutations as perm
# permutation module import
words = []  # 첫 6개의 3자리 단어를 입력받을 빈 배열

# 배열에 단어들 입력
for i in range(6):
    words.append(input())
# 배열의 단어들로 조합 계산
p = list(perm(words, 3))

# 전체 조합중에
#예: ABC/DEF/GHI
for word_comb in p:
    test_crossword = ""  # test해볼 조합의 빈 문자열 정의
    test_list = []  # test 해볼 조합으로 만들어지는 6개의 문자를 담을 배열
    for word in word_comb:
        test_crossword += word  # test 조합의 단어들을 추가
        #예: test_crossword="ABCDEFGHI"
        test_list.append(word)  # test할 조합의 가로 단어들 3개를 추가
        # 예:test_list=['ABC','DEF','GHI']

    # 세로 단어들
    for i in range(3):  # 0,1,2
        new_word = test_crossword[i]+test_crossword[i+3]+test_crossword[i+6]
        test_list.append(new_word)  # 세로단어를 test_list에 추가
        #예: test_list =['ABC','DEF','GHI','ADG','BEH','CFI']
    test_list.sort()  # 처음 주어지는 words 배열이 알파벳 순서이기에, test_list도 알파벳 순서로 정렬
    ans = ""  # 정답이 없을 경우 바뀌지 않을 빈 ans 문자열
    # 일치하는 조합이 있다면
    if test_list == words:
        # ans를 정답 형식에 맞게 설정
        ans = [test_crossword[0:3], test_crossword[3:6], test_crossword[6:9]]
        break  # 첫번째 조합만 필요하므로 break

# 정답이 없다면 0을 출력
if ans == "":
    print(0)
else:  # 정답이 있다면 정답 출력
    print(*ans)
