"""
Problem : 뒤집기
Site : https://www.acmicpc.net/problem/1439
Type : Greedy

Note :
"""
import sys
import re
def solution(bit):
    answer = 0
    """
    연속된걸 한번에 뒤짚는 경우로 최대한 적게
    연속된걸 하나로 합치면 되려나
    00011 을 01 로 하고 둘중 어느쪽이든 뒤짚으면 되니까?
    # 1. 연속된거는 그 숫자 하나로 
    # 2. 그리고 한번 더하면 끝?
    """
    # 연속된 숫자 고르기
    chunk0 = re.compile(r"[0]+")
    chunk1 = re.compile(r"[1]+")
    bit_list0 = chunk0.findall(bit)
    bit_list1 = chunk1.findall(bit)
    # print(bit_list0)
    # print(bit_list1)
    len0 = len(bit_list0)
    len1 = len(bit_list1)
    return len1 if len0 > len1 else len0


if __name__ == "__main__":
    """
    input                   result
    0001100                 1
    11111                   0
    00000001                1
    11001100110011000001    4
    11101101                2
    
    """
    # input = sys.stdin.readline
    # N = int(input().strip()))
    # num_list = []
    # for _ in range(N):
    #     n = int(input().strip())
    #     num_list.append(n)
    # print(solution(num_list))
    
    
    print(solution("0001100"))
    print(solution("11111"))
    print(solution("00000001"))
    print(solution("11001100110011000001"))
    print(solution("11101101"))
    