"""
Problem : 최소 힙
Site : https://www.acmicpc.net/problem/1927
Type : heapq

Note :
"""

import heapq
import sys
def solution(seq):
    answer = 0
    
    """
    배열 받으니까 한 숫자씩 돌면서 반복문 안에서 print 해버리자
    """
    # 최소를 빼긴 해야 하니까
    min_heap = []
    heapq.heapify(min_heap)

    for x in seq:
        if x == 0:
            if min_heap:
                min_v = heapq.heappop(min_heap)
                print(min_v)
            else:
                print(0)
        else:
            heapq.heappush(min_heap, x)


if __name__ == "__main__":
    """
    input
    9
    0
    12345678
    1
    2
    0
    0
    0
    0
    32

    output
    0
    1
    2
    12345678
    0
    """
    # input = sys.stdin.readline
    # N = int(input().strip())
    # temp = []
    # for i in range(N):
    #     K = int(input().strip())
    #     temp.append(K)
    # solution(temp)
    

    solution([0, 12345678, 1, 2, 0, 0, 0, 0, 32])
    