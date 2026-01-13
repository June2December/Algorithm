"""
Problem : 이중우선순위큐
Site : https://school.programmers.co.kr/learn/courses/30/lessons/42628
Type : heapq

Note :
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
    heapq.heapify(operations)
    
    for op in operations:
        cmd, num = op.split()
        if cmd == "I":
            # min_q, max_q 둘다 append
            # min 은 그대로
            # max 는 - 곱해서 / 최솟값만 뽑을 수 있는데 사실 최대니까
            heapq.heappush(min_h, num)
            heapq.heappush(max_h, -num)
        else:
            # 최대 빼기
            if num == 1:
                pass
            else:
                pass
                
    
    return answer


if __name__ == "__main__":
    """
    
    """
    
    print(solution())
    