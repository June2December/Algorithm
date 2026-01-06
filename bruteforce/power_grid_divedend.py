"""
Problem : 전력망을 둘로 나누기
Site : https://school.programmers.co.kr/learn/courses/30/lessons/86971
Type : Brute-Force

Note :
"""

def find_tree(chunk, node):
    # 해당 간선으로 tree 만들기?
    # 시작점은 node?
    # 그냥 B_DFS 로 찾으면될듯?
    
    stack = [node]
    visited = {node}
    
    while stack:
        cur = stack.pop()
        for a, b in chunk:
            if a == cur and b not in visited:
                visited.add(b)
                stack.append(b)
            elif b == cur and a not in visited:
                visited.add(a)
                stack.append(a)
    return visited
    

def solution(n, wires):
    """
    다 연결하고 찾는거보다 임의로 안 edge 삭제 하고 둘의 차이를 보는게 빠를듯
    1. edge 빼는거 만들기
    아닌가 tree 구조라고 했으니까 
    해당 edge 지우고 
    그 상태에서 v1, v2 를 기준으로 각 tree 에 포함되는 node 갯수 구하면 되는건가
    
    2. 2개의 묶음이 나오는지 확인 / 어차피 완전연결 돼 있다 했으니 하나 끊으면 자동으로 그렇게 되긴 할듯
    2-1. 2개의 묶음이 몇개의 node들이 연결되어 있는지 확인하기
    """
    
    answer = set()
    
    for i in range(len(wires)):
        # 1. chunk 에 포함되는 node들을 set()로 만들고
        chunk = [wire for idx, wire in enumerate(wires) if idx != i]
        v1, v2 = wires[i]
        
        # 2. v1, v2로 시작하는 각 tree 갯수 구하기
        v1_nodes = find_tree(chunk, v1)
        v2_nodes = find_tree(chunk, v2)
        
        # 3. 둘의 차이의 절댓값 일단 저장?
        answer.add(abs(len(v1_nodes) - len(v2_nodes)))
    
    return min(answer)


if __name__ == "__main__":
    """
    n	wires	                                            result
    9	[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]	3
    4	[[1,2],[2,3],[3,4]]	                                0
    7	[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]	            1
    """
    
    print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
    print(solution(4, [[1,2],[2,3],[3,4]]))
    print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))
    