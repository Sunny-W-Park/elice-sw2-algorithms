import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) #힙으로 만듬
    while scoville:
        a = heapq.heappop(scoville) #제일 작은수
        if a>=K: #제일 작은수가 K보다크면 정답 리턴
            return answer
        if scoville:
            b = heapq.heappop(scoville)
        else: #힙큐가 비었을 때 모든 스코빌 지수를 K 이상으로 만들 수 없으므로 -1 리턴
            return -1
        c = a+(b*2)
        heapq.heappush(scoville,c)
        answer += 1