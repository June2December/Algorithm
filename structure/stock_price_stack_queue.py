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
    """
    answer = []
    return answer

if __name__ == "__main__":
    """
    prices              return
    [1, 2, 3, 2, 3]     [4, 3, 1, 1, 0]
    """
    print(solution(prices))
    