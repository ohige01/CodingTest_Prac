import sys
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while(scoville[0] < K):
        if(len(scoville) > 1):
            answer += 1
            x_1 = heapq.heappop(scoville)
            x_2 = heapq.heappop(scoville)
            heapq.heappush(scoville, (x_1 + x_2*2))
        else:
            return -1
    return answer

K = int(input())
scoville = list(map(int, sys.stdin.readline().split()))

print(solution(scoville, K))