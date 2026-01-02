"""
Problem : 다리를 지나는 트럭
Site : https://school.programmers.co.kr/learn/courses/30/lessons/42583
Type : stack queue

Note :
"""

from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    """
    그냥 greedy 처럼 매 순간마다 weight 넘지 않겠다 싶음 실어 보내면 되네
    동시에 length 도 고민하고
    
    다리 위에 현황도 유지 해야하니가 그것도 q 로 해서 rotate 가 편할듯
        어차피 뽑아야 하는구나
    """
    
    total = 0 # 현재 올라 가 있는 다리 위 총 트럭 무게
    
    q_truck = deque(truck_weights)
    q_bridge = deque([0 for _ in range(bridge_length)])

    while q_truck or total > 0:
        # 1. 첫 진입 빼고 q_bridge 한 칸 이동
        acrossed = q_bridge.popleft()
        total -= acrossed
        
        # 2. 한 칸 이동 했으니 answer 최신화
        answer += 1
        
        # 3. 이번에 트럭 올라타기 가능이면 출발
        if q_truck and ((q_truck[0]+total) <= weight):
            nxt = q_truck.popleft()
            q_bridge.append(nxt)
            total += nxt
        else:
            q_bridge.append(0)
    
    return answer



if __name__ == "__main__":
    """
bridge_length	weight	truck_weights	                return
2	            10	    [7,4,5,6]               	    8
100	            100	    [10]	                        101
100	            100	    [10,10,10,10,10,10,10,10,10,10]	110
    """
    
    print(solution(2, 10, [7,4,5,6]))
    print(solution(100, 100, [10]))
    print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
    