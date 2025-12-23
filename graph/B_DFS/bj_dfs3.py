"""
Problem : 알고리즘 수업 - 깊이 우선 탐색 3
Site : https://www.acmicpc.net/problem/24481
Type : B_DFS

Note : 
"""
import sys
from collections import deque
def solution(N, R, edges):
    """
    인접 정점 오름차순 방문이라는데 깊이 구하는거라 정렬은 필요 없을듯 아니네 오름차순 정렬해야 방문을 바로 안하는구나
    """
    graph = [[] for _ in range(N+1)]
    for s, e in edges:
        graph[s].append(e)
        graph[e].append(s)
    
    for i in range(N+1):
        graph[i].sort(reverse=True)
    
    
    layer = 0
    stack = [(R, layer)]
    visited = [False] * (N+1)
    memory = [-1] * (N+1)
    memory[R] = 0
    while stack:
        cur, _layer = stack.pop()
        visited[cur] = True
        for nxt in graph[cur]:
            if not visited[nxt]:
                stack.append((nxt, _layer+1))
                memory[nxt] = _layer + 1
    for x in memory[1:]:
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
    0
    1
    2
    3
    -1
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
    solution(N, R, edges)
    