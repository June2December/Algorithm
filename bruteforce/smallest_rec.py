"""
Problem : 최소직사각형
Site : https://school.programmers.co.kr/learn/courses/30/lessons/86491
Type : Brute-Force

Note :
"""

def solution(sizes):
    """
    가로 세로 무시하고
        큰 숫자들 중 젤 큰 수
        작은 숫자들 중 젤 큰 수
    곱하기
    """
    BIG = SMALL = 0
    for row, col in sizes:
        if row < col:
            if SMALL < row:
                SMALL = row
            if BIG < col:
                BIG = col
        else:
            if SMALL < col:
                SMALL = col
            if BIG < row:
                BIG = row
    
    return BIG * SMALL

if __name__ == "__main__":
    """
    sizes	                                        result
    [[60, 50], [30, 70], [60, 30], [80, 40]]	    4000
    [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]	120
    [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]	133
    """
    
    print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
    print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
    print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
    