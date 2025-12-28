"""
Problem : 주식가격
Site : https://school.programmers.co.kr/learn/courses/30/lessons/42584
Type : stack queue

Note :
"""
import sys
from collections import deque
def solution(prices):
    """
    해당 시점 이후로 미만인 숫자 나오면 안되는거네
    십만이 길이니까 뭔가 매번 계산은 당연 아닐거고
    O(n) 이 직감적으로 맞을거 같은데
    한 시점 마다 이게 앞의 어느 놈까지 제한할 수 있는지
    t1  t2  t3
        30
    20
            1
    이런건 불가능하네 아니구나 가능하구나
    그럼 이번 t3, 1 이 t2, t3 보다도 작으니까 다 없애야 하네
    크면 이번것도 넣고 작으면  앞에 놈들 차례로 빼고?
    그럼 q 만들어서 매 순간 마다 비교해가며 이번걸 뒤에 넣거나 맨앞에꺼를 추출?
    이때 빼는순간의 인덱스를 기억하고 있어야 하네
    
    1) 핵심은 i 시점 의 가격이 떨어지지 않은 기간 구하기
        1. i 보다 작아지는 j --> j-i
        2. i 보다 작아짐 없음 --> n-1-i
    
    2) 핵심은 아직 뒤까지 확인해야 하는 경우 특정 구조에 저장
        1. 해당 자료구조는 주식가격이 우상향 하는 과정만 담김
        2. 가장 마지막 주식가격이랑 비교
            1) stack으로 주식 가격 저장
                가격으로 i, j 인덱스 접근 못하니까 인덱스 저장
    
    """
    n = len(prices)
    answer = [0] * n
    
    
    stack = [0]
    for j in range(1, n):
        # q 로 하면 되나? / stack 이였던것
        # 현재 가격이 누구보다 더 작아지면? 그걸 어떻게 다 기억하지
        # 인덱스를 기억해서 매 회마다
            # stack 마지막보다 크면 stack 삽입
            # stack 마지막보다 작으면 stack.pop 해서 그놈 계산해서 answer 에 넣
        while prices[stack[-1]] > prices[j]:
            highest_idx = stack.pop()
            answer[highest_idx] = j - highest_idx
        
        
        stack.append(j)

    
    
    # 이검 마지막 예외?처리
    while stack:
        idx = stack.pop()
        answer[idx] = n-1-idx
    
    
    return answer

if __name__ == "__main__":
    """
    prices              return
    [1, 2, 3, 2, 3]     [4, 3, 1, 1, 0]
    """
    prices = [1, 2, 3, 2, 3]
    
    print(solution(prices))
    