"""
Problem : 퍼즐 조각 채우기
Site : https://school.programmers.co.kr/learn/courses/30/lessons/84021
Type : B_DFS

Note : 너무 긴데 사실 간단한 FS 문제의 반복이고 도형비교에 대한 알고리즘 도 중요하네
"""

def affine(coor:list):
    x_min = 1e10
    y_min = 1e10
    for x, y in coor:
        if x < x_min:
            x_min = x
        if y < y_min:
            y_min = y
    return sorted([(x-x_min, y-y_min) for x, y in coor])

def dfs(board:list, target):
    """
    1 찾는거임
    """
    row, col = len(board), len(board[0])
    visited = [[False]*col for i in range(row)]
    start = (0,0)
    puzzles = []
    directions = ((1,0), (-1,0), (0,1), (0,-1))
    for x in range(row):
        for y in range(col):
            # 퍼즐이라면
            if board[x][y] == target and not visited[x][y]:
                stack = [(x, y)]
                visited[x][y] = True
                puzzle = []
                while stack:
                    cx, cy = stack.pop()
                    puzzle.append((cx, cy))
                    for dx, dy in directions:
                        nx, ny = dx+cx, dy+cy
                        if (0 <= nx < row and 0 <= ny < col) and board[nx][ny] == target and not visited[nx][ny]:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                # 퍼즐 맞으니까
                puzzle = affine(puzzle)
                puzzles.append(puzzle)
    return puzzles

def compare_puzzle(puzzles, holes):
    def affine_rot(shape):
        rotations = []
        cur = shape
        for _ in range(4):
            rotations.append(cur)
            # 90도 회전: (x, y) --> (-y, x)
            # rot 행렬 : [0, -1] [1, 0] 되니까
            cur = [(-y, x) for x, y in cur]
            cur = affine(cur)
        return rotations
    
    count = 0
    # 확인한 퍼즐은 다시 안해도 되지
    visited = [False] * len(puzzles)
    # sorted 했으니까 굳이 안해도 될듯???
    for hole in holes:
        for idx, puzzle in enumerate(puzzles):
            if visited[idx]:
                continue
            if len(puzzle) != len(hole):
                continue
            rot_puzzle = affine_rot(puzzle)
            if hole in rot_puzzle:
                visited[idx] = True
                count += len(hole)
                break
    return count

def solution(game_board, table):
    answer = -1
    """
    이건 너무 어려운데...
    큰 도형부터 넣을 수 있는지 확인 / 어차피 옆에 비어 있음 안돼서 딱 맞아야 할것 같은데?
    
    그럼 도형을 먼저 만들고 / 도형 만드는걸 DFS 로 찾나?
        - 도형을 찾는건 할 수 있음 --> 공백 따로 퍼즐 넣을 수 있는곳 들 만들기
    그 도형을 넣을 수 있음 넣고 / ㄱ 자 모양인걸 어떻게 기억하고 넣냐..
        - board 에서도 bfs 해서 영역 다 갖고 있어야 하네..
        - 어차피 큰 놈 부터 채운다고 뭐 바뀌는거 아니네 그 구멍에 똑같은 퍼즐 채워야 하니까
        - 영역 돌면서 체크
            - 1 영역 : 퍼즐 순회 같은 놈 있는지 확인
                이때 영역도 좌표를 좌상단으로 퍼즐도 좌상단으로 밀어서 비교하면 set? 로 비교하면 되려나
    
    그 다음 도형을 넣을 수 있음 넣고...
    """
    # 1. table 에서 퍼즐 조각 찾기
    puzzles = dfs(table, 1)
    # 1-1. 퍼즐 조각 좌상단으로 평행이동
    
    # 2. game_board 에서 퍼즐 구멍 찾기
    holes = dfs(game_board, 0)
    # 2-1. 퍼즐 구멍 좌상단으로 평행이동
    
    # 3. 각 퍼즐 조각을 순회하면서 구멍이랑 동일한지 비교
    return compare_puzzle(puzzles, holes)
    

if __name__ == "__main__":
    """
    game_board
    [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
    table
    [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
    result
    14
    
    game_board
    [[0,0,0],[1,1,0],[1,1,1]]
    table
    [[1,1,1],[1,0,0],[0,0,0]]
    result
    0
    """
    
    print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],\
        [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))
    print(solution([[0,0,0],[1,1,0],[1,1,1]],\
        [[1,1,1],[1,0,0],[0,0,0]]))
    