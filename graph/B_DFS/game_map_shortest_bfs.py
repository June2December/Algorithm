"""
Problem : 게임 맵 최단거리
Site : https://school.programmers.co.kr/learn/courses/30/lessons/1844
Type : B_DFS

Note : BFS, DFS 문제는 stack, queue 뽑는 순서가 알아서 해주니, 국룰! 국룰! 외우자
"""


def solution(maps):
    answer = 0
    """
    최단거리를 찾아야 하니 bfs 가 적합해 보임
    *FS 할때 visited, 메모리, 방향키
    """
    # 국룰 국룰 국룰국
    move = ((-1,0), (1,0), (0,-1), (0,1))
    start = (0,0)
    N, M = len(maps), len(maps[0])
    
    visited = set()
    visited.add(start)
    q = [[0, 0, 1]]
    while q:
        x, y, cost = q.pop(0)
        for dx, dy in move:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M and (nx,ny) not in visited and maps[nx][ny] == 1:
                visited.add((nx,ny))
                if (nx == N-1) and (ny == M-1):
                    return cost+1
                q.append([nx, ny, cost+1])
    return -1


if __name__ == "__main__":
    """
    n                                                               answer
    [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]   11
    [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]   -1
    """
    
    print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
    print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
    