"""
Problem : 카드 정렬하기
Site : https://www.acmicpc.net/problem/1715
Type : Greedy

Note : ? 그냥 sort 하고 stack 처럼 쌓고 더했다 넣고 다시 빼서 더하고 넣고 이럼...?
"""
import sys
import heapq
def solution(num_list):
    answer = 0
    """
    더미 리스트가 오는데 뭔소린진 잘 모르겠지만 누적 합이 뒤에 더해진다는거 같은데
    아마 t 값이랑 t+1 값 더하기인가봄
    결국 최소 두개씩 계속 합하면 되니 stack 하면 되나
    a
    
    a b
    
    a b
    a b c
    
    a b
    a b c
    a b c d
    """
    length = len(num_list)
    if length == 1:
        return answer
    
    heapq.heapify(num_list)
    while len(num_list) > 1:
        a = heapq.heappop(num_list)
        b = heapq.heappop(num_list)
        s = a + b
        answer += s
        heapq.heappush(num_list, s)
    
    
    
    return answer


if __name__ == "__main__":
    """
    input           result
    3               100
    10
    20
    40
    """
    # input = sys.stdin.readline
    # N = int(input().strip()))
    # num_list = []
    # for _ in range(N):
    #     n = int(input().strip())
    #     num_list.append(n)
    # print(solution(num_list))
    
    num_list = [10, 20, 40]
    print(solution(num_list))
    