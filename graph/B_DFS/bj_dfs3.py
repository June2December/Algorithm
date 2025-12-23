"""
Problem : 알고리즘 수업 -  우선 탐색 3
Site : 
Type : B_DFS

Note : 
"""
import sys
from collections import deque
def solution(N, R, edges):
    pass

if __name__ == "__main__":
    """
    input
    5 5 1
    1 4
    1 2
    2 3
    2 4
    3 4
    output
    
    """
    # input = sys.stdin.readline
    # N, M, R = map(int, input().split())
    # edges = []
    # for _ in range(M):
    #     edges.append(list(map(int, input().split())))
    
    N, M, R = 5, 5, 1
    edges = [[1, 4],
            [1, 2],
            [2, 3],
            [2, 4],
            [3, 4]]
    print(solution(N, R, edges))
    