"""
Problem : 알고리즘 수업 - 너비 우선 탐색 1
Site : https://www.acmicpc.net/problem/24444
Type : B_DFS

Note : 돌아온 국룰!! / 그냥 BFS 순서 구하는거니 q 에 잘 쌓기만 하면 될듯
"""
import sys
from collections import deque
def solution(N, R, edges):
    answer = 0
    # 시작점은 1 아닐수도 있으니가 따로 노드별 간선 모아놔야 겠네
    graph = [[] for _ in range(N+1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    # 순서 굳이 구하는거니까 sort는 해줘야 하네 / 오름차순으로 방문할거래
    for i in range(1, N+1):
        graph[i].sort()
    
    # 이하 국룰 ㅋ
    start = R
    visited = [0] * (N+1)
    q = deque([R])
    visited[R] = 1
    order = 1
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if visited[nxt] == 0:
                order += 1
                visited[nxt] = order
                q.append(nxt)
    
    for i in range(1, N+1):
        print(visited[i])

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
    4
    3
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
    