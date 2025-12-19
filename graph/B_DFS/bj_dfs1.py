"""
Problem : 알고리즘 수업 - 너비 우선 탐색 1
Site : https://www.acmicpc.net/problem/24479
Type : B_DFS

Note : dfs 로 풀라고 하니까 stack, 시작 노드 주어짐
"""
import sys
from collections import deque
def solution(N, R, edges):
    answer = 0
    # bj_bfs_1 처럼 순서 기억 해야 하니까 edges 오름차순 정렬 필요
    graph = [[] for _ in range(N+1)]
    for start, end in edges:
        graph[start].append(end)
        graph[end].append(start)
    for i in range(len(graph)):
        graph[i].sort(reverse=True)
    # FS
    visited = [0] * (N+1)
    stack = [R]
    order = 0
    while stack:
        cur = stack.pop()
        """
        순서 생각해보니 DFS 는 미리 스택에 들어가게 되니까
        방문 여부 확인을 마지막에 하거나 맨 처음에 해야되네
        """
        if visited[cur] != 0:
            continue
        order += 1
        
        visited[cur] = order
        for nxt in graph[cur]:
            if visited[nxt] == 0:
                stack.append(nxt)
    for num in visited[1:]:
        print(num)

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
    2
    3
    4
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
    