"""
Problem : 소수 찾기
Site : https://school.programmers.co.kr/learn/courses/30/lessons/42839
Type : Brute-Force

Note :
"""

import math
from itertools import permutations
def find_prime(num):
    if num <= 1:
        return False
    arange = int(math.sqrt(num))
    return not any(num%i==0 for i in range(2, arange+1))

def solution(numbers):
    answer = 0
    """
    1. 소수 구하는거 생각해야 되고 / 함수로 만들자
        절반 이상까지의 숫자로 나눴을때 약수가 없음 되지
        1 ~ n**0.5 + 1 까지 
    2. 숫자 조합하는거 생각해야 되고
        숫자를 다 써도 되고 다 안 써도 되고 합쳐서 int()로 넣음 될듯
        011 11 같은 수인걸 비교하고 시작?
        수열 만들고 잘라서 쓰면 되려나
    """
    num_list = list(numbers)
    num_set = set()
    for n in range(1, len(num_list)+1):
        for p in permutations(num_list, n):
            num_set.add(int("".join(p)))
    # print(num_set)
    
    return sum(1 for num in num_set if find_prime(num))

if __name__ == "__main__":
    """
    numbers	return
    "17"	3
    "011"	2
    """
    
    print(solution("17"))
    print(solution("011"))
    