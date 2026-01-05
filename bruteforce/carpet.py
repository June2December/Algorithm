"""
Problem : 카펫
Site : https://school.programmers.co.kr/learn/courses/30/lessons/42842
Type : Brute-Force

Note :
"""

import math
def solution(brown, yellow):
    answer = []
    """
    중앙에 노란 가로로 긴 직사각형 만드는데
        1. 이때 직사각형이 여러개 일테고
        / 노랑을 감싸는건데 전체 갯수만 맞으면 되니까 노랑이 가로인지 세로인지까지 알필요 없네
        
        2. 각 직사각형을 brown 으로 감쌀 수 있는 지 확인
    """
    # 1. 노랑 가로로 긴 직사각형 리스트 만들기
    # 소수 찾듯이 (세로 : 1~sqrt()) * (가로)
    yellow_list = list([yellow//i, i] for i in range(1, int(math.sqrt(yellow))+1) if yellow%i==0)
    # print(yellow_list)
    
    # 2. brown + yellow 해서 [가로, 세로] 중 노랑의 가로+2 세로+2 이상의 상자 있다면 바로 반환?
    whole = yellow + brown
    whole_list = list([whole//i, i] for i in range(1, int(math.sqrt(whole))+1) if whole%i==0)
    # print(whole_list)
    
    # 3. 노랑 상자 기준, 포함 가능한 전체 러그 만나면 바로 반환
    for col, row in yellow_list:
        for w_col, w_row in whole_list:
            if col+2 <= w_col and row+2 <= w_row:
                return [w_col, w_row]



if __name__ == "__main__":
    """
    brown	yellow	return
    10	    2	    [4, 3]
    8	    1	    [3, 3]
    24	    24	    [8, 6]
    """
    
    print(solution(10, 2))
    print(solution(8, 1))
    print(solution(24, 24))
    