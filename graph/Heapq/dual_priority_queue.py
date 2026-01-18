"""
Problem : 이중우선순위큐
Site : https://school.programmers.co.kr/learn/courses/30/lessons/42628
Type : heapq

Note : heapq 의 쓸모가 최솟값 삭제 특화라고 국한한다면,
        이 밖에의 연산을 어떤식으로 구성해봐야 할까?
        Lazy deletion : "특정 값이 아직 유효한 값인지"만 기록
"""

import heapq
from collections import defaultdict
def solution(operations):
    answer = []
    """
    각 동작별로 spilt() 해서 1. 알파벳, 2. 숫자 보고 동작 결정
    1. I : append?
    2. D :
        1 : popleft?
        -1 : pop?
        
    pop 은 O(n) 이니까 아니고
    
    heap 으로 최솟값 무조건 뽑으면 되니까 heap 2개 만들어서 관리
    """
    # q.pop 해서 split 해서 의사 결정
    
    min_h = []
    max_h = []
    # heapq.heapify(operations)
    count = defaultdict(int)
    # INF = 10**10
    size = 0
    
    def confirm_min():
        # lazy 즉 다른 데이터 확인해가면서 유효한지 확인하자
        while min_h and count[min_h[0]] == 0:
            heapq.heappop(min_h)
    
    def confirm_max():
        while max_h and count[-max_h[0]] == 0:
            heapq.heappop(max_h)
    
    
    for op in operations:
        cmd, num = op.split()
        num = int(num)
        if cmd == "I":
            # min_q, max_q 둘다 append
            # min 은 그대로
            # max 는 - 곱해서 / 최솟값만 뽑을 수 있는데 사실 최대니까
            heapq.heappush(min_h, num)
            heapq.heappush(max_h, -num)
            count[num] += 1
            size += 1
        else:
            if size == 0:
                continue
            # 최대 빼기
            if num == 1:
                # 역배역에서 최소 빼두기
                confirm_max()
                temp = -1 * heapq.heappop(max_h)
                count[temp] -= 1
                size -= 1
            # 최소 빼기
            else:
                confirm_min()
                temp = heapq.heappop(min_h)
                count[temp] -= 1
                size -= 1
    
    return [0, 0] if size == 0 else [-max_h[0], min_h[0]]


if __name__ == "__main__":
    """
    operations                                                                  return
    ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]	                [0,0]
    ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	[333, -45]
    """
    
    print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
    print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
    
    