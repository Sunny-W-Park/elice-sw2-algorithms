#43105-정수삼각형

def solution(triangle):
    answer = 0
    
    dp = [[] for _ in range(len(triangle))]
    for i in range(len(triangle)):
        for j in range(i+1):
            dp[i].append(0)
            
    dp[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(len(dp[i])):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            if 0 < j and j < len(dp[i])-1:
                dp[i][j] = max(dp[i-1][j-1] + triangle[i][j], dp[i-1][j] + triangle[i][j])
            if j == len(dp[i])-1:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
    
    answer = max(dp[len(triangle)-1])
    
    return answer
