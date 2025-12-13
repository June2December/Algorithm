"""
Problem : 아이템 줍기
Site : https://school.programmers.co.kr/learn/courses/30/lessons/87694
Type : B_DFS

Note : 두 방법이 유일하다고 하는데, 결국 grid 에서 상하좌우로 움직일때랑 다르게 엣지를 생각 필요한거네
"""

from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    """
    움직일 수 있는 후보가 어떻게 되는거지?
    x, y 에서 출발 가정 했을때
    상자1 에서 상자 2로 넘어가는 순간 상자1로 안 가고 상자2 로 갈 수 있는 방법은?
    상자별 범위 만들어서 움직였을때 상자2 안에 있으면 거기로 가도록 설계?
    어차피 한 점에서 여러 개 만나는일 없다는거 같으니?
    이게 최선인가
    전체 만들고 하나로 이어 붙이는게 나을거 같은데
    # 1. 이동 가능한 경로 만들기 / 그냥 사각형 포함하는 모든 점 만들고 안쪽 빼기?
    # 전체 엣지 끼리 다 더하기 - 전체 내부 공간 빼기
    아 1,1 / 1,2 랑 연결이 안 되 있을수도 있구나
    
    결론:
    그래서 최초 생각했던대로 상자별 좌표를 따로 갖고 있거나
    한번에 합쳐서 갖고 있으면 2배로 확장해야 하는거네..
    """
    
    # 좌표 최대가 50, 2배 스케일 + extra
    SIZE = 102
    board = [[0] * SIZE for _ in range(SIZE)]

    # 1. 사각형 전체 영역 채우기
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                board[x][y] = 1

    # 2. 내부 제거, 엣지만
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                board[x][y] = 0

    # 3. BFS
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque()
    sx, sy = characterX * 2, characterY * 2
    tx, ty = itemX * 2, itemY * 2

    q.append((sx, sy, 0))
    visited = [[False] * SIZE for _ in range(SIZE)]
    visited[sx][sy] = True

    while q:
        x, y, dist = q.popleft()
        if x == tx and y == ty:
            return dist // 2

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < SIZE and 0 <= ny < SIZE:
                if board[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))

    return 0



if __name__ == "__main__":
    """
    rectangle	characterX	characterY	itemX	itemY	result
[[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]	1	3	7	8	17
[[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]	9	7	6	1	11
[[1,1,5,7]]	1	1	4	7	9
[[2,1,7,5],[6,4,10,10]]	3	1	7	10	15
[[2,2,5,5],[1,3,6,4],[3,1,4,6]]	1	4	6	3	10
    """
    
    print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))
    print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1))
    print(solution([[1,1,5,7]], 1, 1, 4, 7))
    

