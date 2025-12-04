"""
Problem : 설탕 배달
Site : https://www.acmicpc.net/problem/2839
Type : Greedy

Note : ...
"""


def solution(sugar):
    
    """
    총 중량을 최대한 적은 봉지 묶음으로..
    5, 3 으로 나누는데 최대한 5 가 많아야하는데
    1 x / 
    2 x / 
    3 1 / 5로 못 나눠서 3으로 나누면 1 나옴
    4 x / 
    5 1 / 5로 몫 1, 나머지 0 이여서 끝
    6 2 / 5로 몫 1, 이럼 못 만드네, 그럼 3으로 나누기
    7 x / 5로 몫 1, 이럼 못 만드네, 3으로 나누는건 불가
    8 2 / 5로 몫 1, 나머지 나눔 가능 / 불가하면 3으로 나눠보기..?
    9 3
    11 
    
    1 : 1, 6, 11, 16, 21, 26, ... , 81, 86
    2 : 2, 7, 12, 17
    3 : 
    4 : 
    
    1. 일단 5로 나눠 몫 일단 저장해놔
    2. 나머지 3으로 나눔
        - 가능, 몫 두개 더해
        - 불가능, 몫 에서 하나씩 빼가면서 3 배수 만들어지는지 확인 / 언제든 만들어지면 몫 갯수 2개 더해
    """
    
    # 1. 일단 5로 나눠서 첫번째 몫 구해
    num_5, rest = divmod(sugar, 5)
    # 2. while 문으로 div 다 탕진해도 좋으니 순회
    num_3, remain = divmod(rest, 3)
    if remain == 0:
        return num_5 + num_3
    else:
        while num_5 > 0:
            num_5 -= 1
            rest += 5
            num_3, remain = divmod(rest, 3)
            if remain == 0:
                return num_5 + num_3
    
    
    return -1


if __name__ == "__main__":
    """
    total   result
    18      4
    4       -1
    6       2
    9       3
    11      3
    """
    print(solution(18))
    print(solution(4))
    print(solution(6))
    print(solution(9))
    print(solution(11))
    