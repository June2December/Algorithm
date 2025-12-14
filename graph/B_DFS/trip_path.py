"""
Problem : 여행 경로
Site : https://school.programmers.co.kr/learn/courses/30/lessons/43164
Type : B_DFS

Note : 기존 국룰이 빠지네 visited 없이 구현
사실상 visited 구현된건 맞은데, 방문순서를 기록해서 문제를 푸네
"""

from collections import defaultdict
def solution(tickets):
    answer = []
    """
    공항별 갈 수 있는 공항들을 따로 관리는 해야겠네 / dict?
    """
    # 공항 별 비행편 만들기
    airport = defaultdict(list)
    for a, b in tickets:
        airport[a].append(b)
    for a in airport.keys():
        airport[a].sort(reverse=True)
    # BFS, DFS 중 경로 확인만 하면돼서 DFS 로 ?
    path = ["ICN"]
    while path:
        # 현재 공항 방문
        cur = path[-1]
        # 항공권 중에 먼저가야 하는거 뽑아서 다음방문으로
        # reverse 로 해놨으니 꺼내는 족족 그냥 넣으면 될듯
        if airport[cur]:
            path.append(airport[cur].pop())
        # 항공권 더 이상 없으면 path에 저장해 놔서 그 순서로 가도록
        else:
            answer.append(path.pop())
            
    return answer[::-1]


if __name__ == "__main__":
    """
    tickets : [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    return : ["ICN", "JFK", "HND", "IAD"]
    
    
    tickets : [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
    return : ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
    """
    
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
    
