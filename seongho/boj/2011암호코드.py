# n자리수가 있으면,
# n 일 때, n-1일때의 경우의 수 x에 그냥 하나의 수를 더한다: x경우
# n 일 때, n-2일 때의 경우의 수 y에 두개의 수를 합쳐서 더한다. y경우

# 예:
# n=1 일 때는 1 #1
# n=2 일 때는 (1,1), (2) #2
# n=3 일 때 , (1,1,1),(2,1),(1,2) #3
# n=4 일 때는 (1,1,1,1), (2,1,1),(1,2,1),(1,1,2),(2,2) #5

# 특이 사항
# n-2일 때 y가지가 있으면, n-1번째 수*10+n번째 수가 함이 26이하여야함
# 그리고 0을 고려해야함

# dp[n]=dp[n-1]+dp[n-2] (if n-1,n 이 26이하)
code = input()  # 숫자를 쓰지만, 어차피 문자열을 쪼개는 것이 더 편해서 문자열로 입력
code_length = len(code)
if int(code[0]) == 0:  # 처음수로 0이 들어오는 것은 불가능
    print(0)
    exit()
elif code_length == 1:  # 한개의 수만 들어오고 0이 아니면 무조건 가능
    print(1)  # 이때의 경우의 수는 하나이므로 1을 출력
    exit()
dp = [0]*(code_length+1)
dp[0] = 1  # 103같은 케이스를 위해서 1로 설정
dp[1] = 1
# abc #...a +b+c , a+bc
for i in range(2, code_length+1):  # dp[2]부터 dp[N] 까지
    two_digit_num = int(code[i-2:i])  # 지금 수+ 바로 직전 수
    n_digit_num = int(code[i-1])  # 지금 수
    prev_digit_num = int(code[i-2])  # 바로 직전 수
    if (two_digit_num > 26 and n_digit_num == 0) or (n_digit_num == 0 and prev_digit_num == 0):
        print(0)  # 예로 30 같은 경우에는 30, 3/0 으로 둘다 해석 불가능
        exit()  # 00 같은 경우도 해석 불가능
    elif two_digit_num > 26 and n_digit_num != 0:
        dp[i] = dp[i-1]  # 예: 35같은 경우는 3/5로 만 해석이 가능 따라서 한자리수를 추가하는 것만 고려
    elif two_digit_num <= 26 and n_digit_num == 0:
        dp[i] = dp[i-2]  # 예: 20 같은 경우는 2/0이 불가능하므로 무조건 20으로 해석해야함, 따라서 두자리수 추가만 고려
    elif n_digit_num != 0 and prev_digit_num == 0:
        # 예: ..n101같은 상황이 온다면, 이때의 01 은 0/1, 01둘다 해석이 불가능하지만 10,1로 해석이 가능하기에 불가능한 케이스가 아니다. 그럼 이 3개의 수로 10/1 만이 유일하기에 이 3자리수를 1개의 경우로 추가하는 것.
        dp[i] = dp[i-3]
    else:
        dp[i] = (dp[i-1]+dp[i-2]) % 1000000  # 다른 평범한 케이스들
print(dp[-1])
