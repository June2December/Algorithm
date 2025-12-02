"""
Problem : 섬 연결하기
Site : 
Type : Greedy / 크루스칼 알고리즘

Note : 노드간의 
"""

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
def solution(n, costs):
    answer = 0
    """
    누구와든 연결만 되 있으면 다 도달 가능하네
    
    적은 비용부터 연결지으면서 확인하면 될듯 / sort 를 비용 순으로 노드 2개 다 나온적 있으면 버려
    """
    # 1. 비용기준 오름차순
    costs.sort(key = lambda x : x[2])
    
    # 2. 순회, 무리를 지어서 연결만 되어 있음 되니까 하나씩 연결
    parent = list(range(n))  # 각 노드의 대표
    for a, b, cost in costs:
        # 두 노드의 대표가 다르면, 아직 다른 무리
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            answer += cost
        
    return answer




if __name__ == "__main__":
    """
    n   costs                                       return
    4   [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]   4
    """
    print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
    