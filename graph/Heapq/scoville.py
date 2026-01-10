"""
Problem : 더 맵게
Site : https://school.programmers.co.kr/learn/courses/30/lessons/42626
Type : heapq

Note :
"""

import heapq
def solution(scoville, K):
    answer = 0
    """
    1. 직관적으로 든 생각인데, 어차피 지수가 k 만 넘으면 되니까 이미 k 가 넘는애들은 웬만하면 거의 신경 안써도 되겠네.
        다만 k 보다 훨씬 낮은애들로는 k를 못 넘길수도 있으니까 그건 해봐야 알거고
    2. 작은거 부터 처리하는게 맞겠지? / 가령 1 1 1 1 1 10 10 10 10 10 / 이면
        5번만에 11이상이 될수 있지만
        1 1 합치면 3 ,
        1 3 합치면 7,
        1 7 합치면 15,
        1 남은거 하나 하면 일단 1은 사라지니까
        4번만에 가능한건가?
    3. 그럼 push 시 정렬 알아서 되도록 heapq == 정렬은 아니긴 하지?
    4.
        1) heapq 에 최솟값이 k 보다 작고
        2) 더 이상 못 합치는 길이 1인 경우
        3) 
    """
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        # 되는데까지 합쳐보고 안되면 -1 반환
        if len(scoville) < 2:
            return -1
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, (min1 + min2 * 2))
        answer += 1
        
    
    return answer


if __name__ == "__main__":
    """
    scoville	            K	return
    [1, 2, 3, 9, 10, 12]	7	2
    """
    
    print(solution([1, 2, 3, 9, 10, 12], 7))
    