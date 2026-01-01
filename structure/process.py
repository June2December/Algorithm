"""
Problem : 프로세스
Site : https://school.programmers.co.kr/learn/courses/30/lessons/42587
Type : stack queue

Note :
"""

from collections import deque
def solution(priorities, location):
    answer = 0
    """
    1. 전체 우선순위별로 나보다 큰 애들은 순서 생각 안하고 그냥 다 뽑아도 되네?
        아니구나 2, 3 이런식이면 다시 넣어둬야 되나..?
    2. 현재 위치는 포인터 처럼 처음 location 을 돌리거나 뺄때마다 기억해야 되네
        각 우선순위 별로 몇개인지 알아야 뺐다가 넣고 최고 우선순위가 더 있는지 확인 가능하네
    """
    # 1. 우선순위, 원래 인덱스 큐 
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    answer = 0
    
    # pointer = location
    
    while queue:
        cur = queue.popleft()
        
        # 2. 큐에 현재 꺼낸 것보다 우선순위가 높은 게 하나라도 있는지
        # 최대 길이 100 개라 O(n**2) 해도 만번
        if any(cur[0] < q[0] for q in queue):
            # 더 높은게 있다면 다시 뒤로
            queue.append(cur)
        else:
            # 3. 현재가 가장 우선순위가 높다면 실행
            answer += 1
            # 내가 찾던 위치의 프로세스라면 종료
            if cur[1] == location:
                return answer
    return answer


if __name__ == "__main__":
    """
    priorities	        location	return
    [2, 1, 3, 2]	    2	        1
    [1, 1, 9, 1, 1, 1]	0	        5
    """
    
    print(solution([2, 1, 3, 2], 2))
    print(solution([1, 1, 9, 1, 1, 1], 0))
    