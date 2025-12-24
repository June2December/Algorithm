"""
Problem : 알고리즘 수업 - 너비 우선 탐색 4
Site : https://www.acmicpc.net/problem/24447
Type : B_DFS

Note : 
"""
import sys
from collections import deque
def solution(N, R, edges):
    """
    직관적으로 자료형을 튜플 모음 리스트로 가자
    [(1, 1), (2, 2), ...]
    """
    answer = 0
    graph = [[] for _ in range(N+1)]
    for s, e in edges:
        graph[s].append(e)
        graph[e].append(s)
    # 너비 탐색이여서 방문순서대로 넣어도 오름차순으로 잘 뽑히겠지
    for i in range(1, N+1):
        graph[i].sort()
    
    # 방문 확인 및 깊이(-1은 미방문)
    depths = [-1] * (N + 1)
    # 방문 순서
    orders = [0] * (N + 1)
    
    # 시작점 설정
    q = deque([R])
    depths[R] = 0
    order_cnt = 1
    
    while q:
        cur = q.popleft()
        orders[cur] = order_cnt # 꺼낼 때 순서 기록
        order_cnt += 1
        
        for nxt in graph[cur]:
            if depths[nxt] == -1: # 방문하지 않았다면
                depths[nxt] = depths[cur] + 1 # 큐에 넣기 전 방문처리 및 깊이 기록 / q 에 한번에 넣어서 관리하면 꼬이네..ㅜㅜ
                q.append(nxt)
    
    for i in range(1, N + 1):
        if depths[i] != -1: # 방문한 노드만
            answer += orders[i] * depths[i]
            
    print(answer)

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
    13
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
    