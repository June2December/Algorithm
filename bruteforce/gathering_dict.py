"""
Problem : 모음사전
Site : https://school.programmers.co.kr/learn/courses/30/lessons/84512
Type : Brute-Force

Note :
"""


def solution(word):
    answer = 0
    """
    왼쪽정렬
    AA 가 2번째니까 E 가 2번째가 아닌걸 기억
    6진수 처럼 _ A E I O U 이렇게 생각하고 ㄱㄱ
    
    {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    123 이면 10**2  +  2*10**1  +  3*10**0
    AAAAE : x**4  +  x**3  +  x**2  +  x**1  +  x**0
            1        1        1        1        2?
    AAAE  : 1        1        1        y        0
    
    
    맨 뒤가 A 면 그 
    1   A____
    2   AA___
    3   AAA__
    ...
    16  AAO
    17  AAU
    """
    
    hexo = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    """
    5**4 + 5**3 + 5**2 + 5**1 + 5**0= 625 125 25 5 1 = 781
    5**3 + 5**2 + 5**1
    """
    weights = [781, 156, 31, 6, 1]
    
    for i, ch in enumerate(word):
        answer += hexo[ch] * weights[i] + 1
    return answer


if __name__ == "__main__":
    """
    word	result
    "AAAAE"	6
    "AAAE"	10
    "I"	    1563
    "EIO"	1189
    """
    
    print(solution("AAAAE"))
    print(solution("AAAE"))
    print(solution("I"))
    print(solution("EIO"))
    