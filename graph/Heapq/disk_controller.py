"""
Problem : 디스크 컨트롤러
Site : https://school.programmers.co.kr/learn/courses/30/lessons/42627
Type : heapq

Note :
"""

import heapq
def solution(jobs):
    answer = 0
    """
    우선순위는 소요시간 / 요청시각 / 번호가 작은것
    jobs 가 이미 sort돼서 들어올듯 번호가 빠졌으니
    
    1. 요청시가 기준 sort? : 대기 q 에 들어가 있어야 할 수 있는데
    2. 그냥 순서대로 pop 하면서 소요시간 구해서 answer 에 더해두고 x
        q 를 거쳐서 가야만 하네 / 그렇지 않음 계속 전역 해를 구하게 되네
        중간에 텀 나는 시간이 생기면 실패하네
    3. return answer//n
    """
    n = len(jobs)
    # 1
    jobs.sort(key=lambda x: (x[0], x[1]))
    heap = []
    i = 0       # job 에서 아직 호출 안된 다음 작업 index
    current = 0
    
    # 2
    # i < n 으로 예외처리 해줘야 하고
    # 현재 기준 과거에 요청 들어왔던건 다 heap 에 넣어놔야지
    while i < n or heap:
        # 2-1 : 현재까지 요청 들어온 작업들
        while i < n and jobs[i][0] <= current:
            start, duration = jobs[i]
            heapq.heappush(heap, (duration, start, i))
            i += 1
        # 2-2 : 그중에서 지역 최적 으로다가
        if heap:
            duration, start, idx = heapq.heappop(heap)
            current += duration
            answer += (current - start)
        # 2-3 : 아직 모든 작업 수행은 안 했고,
            # 그다음 작업을 하기 위해 시점 이동
        else:
            current = jobs[i][0]
            
    return answer//n



if __name__ == "__main__":
    """
    jobs	                    return
    [[0, 3], [1, 9], [3, 5]]	8
    """
    
    print(solution([[0, 3], [1, 9], [3, 5]]))
    