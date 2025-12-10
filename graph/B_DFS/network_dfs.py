"""
Problem : 네트워크
Site : https://school.programmers.co.kr/learn/courses/30/lessons/43162
Type : B_DFS

Note : union 문제도 방문 하는걸 억제하는거라 비슷하긴 하네
"""

def solution(n, computers):
    answer = 0
    """
    computers 행렬은 대칭이네 대각은 항상 1로 자기 자신 가리키는거고
    # 1. 엣지를 먼저 찾아야 하나?
    # 2. 엣지끼리 그룹 만들기? / 전에 풀었던 문제랑 동일해 보이는데?
    DFS 문제로 풀자 카테고리가 DFS 이니
    ========================================================
    1. 그룹 돌면서 net 찾은 애들은 T/F 체크만 해두면 되네
        한번 search 할때 끝까지 찾으니 그때마다 카운팅하면 돼서
    2. com 방문 여부 저장용 메모리 필요
    3. 각 com range로 순회하면서 방문 안했다하면 answer += 1
    """
    visited = [False] * n
    for i in range(n):
        if visited[i] == False:
            answer += 1
            visited[i] = True
            # 여기서 DFS 등 BFS 해서 NET 구성하고 NET 이 필요하진 않네
            stack = [i]
            while stack:
                current = stack.pop()
                for com in range(n):
                    if computers[current][com] and not visited[com]:
                        visited[com] = True
                        stack.append(com)
    
    return answer


if __name__ == "__main__":
    """
    n       computers                           return
    3       [[1, 1, 0], [1, 1, 0], [0, 0, 1]]   2
    3       [[1, 1, 0], [1, 1, 1], [0, 1, 1]]   1
    """
    
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
    