"""
Problem : 기능개발
Site : https://school.programmers.co.kr/learn/courses/30/lessons/42586
Type : stack queue

Note :
"""
import math
import sys
from collections import deque
def solution(progresses, speeds):
    """
    먼저 배포되어야 하는게 정해져 있으니
    각 남은 % 를 speed로 나눈 값 
    Ex) 7, 3.xx, 9
    저장
    
    q 에서 첫번째 뺀것에서
    q이하 인것들을 다 빼 == 몇개인지만 세면 되네
    
    """
    answer = []
    # 세팅
    q = []
    for p, s in zip(progresses, speeds):
        # 결론은 올림해야 함
        # 1.75 같은 숫자는 결국 2일째 배포 가능
        # 어치피 배포는 하루 단위로 1일 2일 날 배포되니까
        # 1.75 과 1.74 누가 더 큰가는 사실 의미가 없네
        left = math.ceil((100-p)/s)
        q.append(left)
    q = deque(q)
    while q:
        cur = q.popleft()
        count = 1
        while q and cur >= q[0]:
            q.popleft()
            count += 1
        answer.append(count)
    return answer

if __name__ == "__main__":
    """
progresses	speeds	return
[93, 30, 55]	[1, 30, 5]	[2, 1]
[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]
    """
    
    print(solution([93, 30, 55], [1, 30, 5]))
    print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
    