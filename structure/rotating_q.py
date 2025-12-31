"""
Problem : 회전하는 큐
Site : https://www.acmicpc.net/problem/1021
Type : stack queue

Note :
"""
import math
import sys
from collections import deque
def solution(N, num_list):
    """
    10 받고 1 2 3 이면
    순회 : 시계, 반시계 방향 몇칸 이동인지 확인
        - 작은쪽으로 이동?
        - 좌우 이동량 똑같을때 그 다음 숫자에 따라서 다름?
            - 아니구나 상관없네
        = 결국 매번 그리디로 가까운 이동량 만큼 이동 될듯
    포인터로 찾으려고 하니까 순환큐에선 찾기 너무 빡세다
    O(n) 으로 매번 index 찾으면 최대 최악이 (50 숫자) * (50 회)
    """
    # answer = 0      # 총합
    # idx = 0         # 포인터 : 현재 위치 가리키기
    # subtract = {}   # 뺀 애들로 몇칸 이동하면 될지 계산
    q = deque([i for i in range(1, N+1)])
    answer = 0
    
    def _rotate(count, direction):
        for _ in range(count):
            q.rotate(direction)
    
    for num in num_list:
        idx = q.index(num)
        
        # 반시계로 돌리기
        if idx <= len(q)//2:
            _rotate(idx, -1)
            answer += idx
        # 시계로 돌리기
        else:
            _rotate((len(q) - idx), 1)
            answer += (len(q) - idx)
        q.popleft()
    
    return answer

if __name__ == "__main__":
    """
    input1
    10 3                0
    1 2 3
    
    input2
    10 3                8
    2 9 5
    
    input3
    32 6                59
    27 16 30 11 6 23
    
    input4
    10 10               14
    1 6 3 2 7 9 8 4 10 5
    """
    
    # input = sys.stdin.read().split()
    # if not input:
    #     exit()
        
    # N = int(input[0])
    # M = int(input[1])
    # # 나머지가 모두 뽑을 숫자 리스트
    # num_list = list(map(int, input[2:]))
    
    # print(solution(N, num_list))
    
    print(solution(10, [1,2,3]))
    print(solution(10, [2,9,5]))
    print(solution(32, [27,16,30,11,6,23]))
    print(solution(10, [1,6,3,2,7,9,8,4,10,5]))
    
    
    