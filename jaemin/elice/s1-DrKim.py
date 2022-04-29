# 김박사의 비밀 데이터
# PR 220429 JAEMIN
# AUTH 220429 JAEMIN

N = int(input())

input_list = []
for turn in range(N):
    input_list.append(int(input()))
print(str(sum(input_list))[:10])
