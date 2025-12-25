"""
Problem : 알고리즘 수업 - 깊이 우선 탐색 4
Site : https://www.acmicpc.net/problem/24482
Type : B_DFS

Note : 
"""
import sys
from collections import deque
def solution(N, R, edges):
    """
    얘야 말로 깊숙히 갈 수 있을때까지 가야하는거니까 tuple로 depth 기록 필요하네
    """
    answer = 0
    graph = [[] for _ in range(N+1)]
    for s, e in edges:
        graph[s].append(e)
        graph[e].append(s)
    # 깊이여서 거꾸로 담아놔야 / 내림차순 방문 원하니 오름차순으로 정렬
    for i in range(1, N+1):
        graph[i].sort()
    
    stack = [(R, 0)]
    # visit을 -1 여부로 확인 동시에 깊이 기록
    visited = [-1] * (N+1)
    visited[R] = 0
    while stack:
        cur, depth = stack.pop()
        if depth < visited[cur]: # 불필요 방문은 예외처리 필요
            continue
        visited[cur] = depth
        for nxt in graph[cur]:
            if visited[nxt] == -1:
                stack.append((nxt, depth+1))
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
    0
    3
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
    