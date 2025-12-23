"""
Problem : 알고리즘 수업 - 넓이 우선 탐색 3
Site : https://www.acmicpc.net/problem/24446
Type : B_DFS

Note : 
"""
import sys
from collections import deque
def solution(N, R, edges):
    """
    깊이를 측정해야하니 깊은곳으로 무조건 가는 DFS 가 아닌 BFS 지
    깊이를 각 노드마다 추적해야 해서 같이 tuple 로 추적하자
    """
    graph = [[] for _ in range(N+1)]
    for s, e in edges:
        graph[s].append(e)
        graph[e].append(s)
    layer = 0
    q = deque([(R, layer)])
    visited = [False] * (N+1)
    memory = [-1] * (N+1)
    memory[R] = 0
    while q:
        cur, _layer = q.popleft()
        visited[cur] = True
        
        for nxt in graph[cur]:
            if not visited[nxt]:
                q.append((nxt, _layer+1))
                memory[nxt] = _layer + 1
                visited[nxt] = True
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
    1
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
    