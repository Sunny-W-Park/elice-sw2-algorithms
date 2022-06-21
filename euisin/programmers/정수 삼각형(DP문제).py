def solution(triangle):
    answer = 0
    leng = len(triangle)
    for i in range(1,leng):
        triangle[i][0] += triangle[i-1][0]
        triangle[i][i] += triangle[i-1][i-1]
        for j in range(1,i):
            triangle[i][j] = triangle[i][j]+triangle[i-1][j-1] if triangle[i-1][j-1] >= triangle[i-1][j] else triangle[i][j]+triangle[i-1][j]
    answer = max(triangle[leng-1])
    return answer