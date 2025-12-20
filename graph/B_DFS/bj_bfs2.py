"""
Problem : 알고리즘 수업 - 너비 우선 탐색 2
Site : https://www.acmicpc.net/problem/24445
Type : B_DFS

Note : 
"""
import sys
from collections import deque
def solution(N, R, edges):
    """
    똑같이 무방향에 가중치 1로 동일이고 BFS
    """
    graph = [[] for _ in range(N+1)]
    for start, end in edges:
        graph[end].append(start)
        graph[start].append(end)
    for i in range(1, N+1):
        graph[i].sort(reverse=True)
    ####################
    order = 1
    q = deque([R])
    visited = [0] * (N+1)
    visited[R] = 1
    while q:
        cur = q.popleft()
        for neighbor in graph[cur]:
            if visited[neighbor] == 0:
                order += 1
                visited[neighbor] = order
                q.append(neighbor)
        # BFS 니까 넣는대로 나오겠네
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
    3
    4
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
    