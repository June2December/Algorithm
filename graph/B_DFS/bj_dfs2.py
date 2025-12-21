"""
Problem : 알고리즘 수업 - 깊이 우선 탐색 2
Site : https://www.acmicpc.net/problem/24480
Type : B_DFS

Note : 
"""
import sys
from collections import deque
def solution(N, R, edges):
    """
    똑같이 무방향에 가중치 1로 동일이고 DFS / 내림차순으로 방문하고 싶댄다
    """
    # 간선 기본 설정
    graph = [[] for _ in range(N+1)]
    for s, e in edges:
        graph[s].append(e)
        graph[e].append(s)
    for i in range(1, N+1):
        # 내림차순으로 가야하는데 stack 에 넣고 방문하는건 마지막에 넣은것이니 정배로 넣어야지
        graph[i].sort(reverse=False)
    # 국룰국룰
    stack = [R]
    visited = [0] * (N+1)
    order = 1
    while stack:
        cur = stack.pop()
        if visited[cur] == 0:
            visited[cur] = order
            order += 1
            for nxt in graph[cur]:
                stack.append(nxt)
    
    for x in visited[1:]:
        print(x)
    
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
    1
    4
    3
    2
    0
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
    