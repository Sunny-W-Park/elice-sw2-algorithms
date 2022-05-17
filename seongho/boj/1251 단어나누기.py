word = input()  # 문자열 입력
n = len(word)  # 문자열의 길이
ans_list = []
for i in range(1, n-1):  # i: 1부터 n-1 까지 (문자열을 i/n-i 두개로 나눔)
    for j in range(1, n-i):  # j: 1부터 n-i 까지 (나눠진 n-i길이의 문자열을 또 두개로 나눔)
        # 문자열을 (i,j,n-i-j) 길이로 삼등분
        a = word[0:i]  # 길이 i
        b = word[i:i+j]  # 길이 j
        c = word[i+j:n]  # 길이 n-i-j
        # 뒤집기
        a = a[::-1]
        b = b[::-1]
        c = c[::-1]
        # 단어 합치기
        new_word = a+b+c
        # 합친 결과를 정답리스트에 추가
        ans_list.append(new_word)
# 정답 리스트 알파벳순으로 정렬
ans_list.sort()
print(ans_list[0])  # 리스트의 첫 단어 출력
