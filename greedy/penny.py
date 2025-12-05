"""
Problem : 동전 0
Site : https://www.acmicpc.net/problem/11047
Type : Greedy

Note : ...
"""
import sys
def solution(pence, price):
    answer = 0
    """
    동전은 N 종류 / K 만들기 최소로
    설탕배달 문제랑 거의 비슷하네
    
    pence = [1, 5, 10, ...] 일때 그거보다 작은것들중 젤 큰거 주고 시작?
    남은 금액에 대해서도 마찬가지? / 어차피 배수 관계라 못 줄일이 없는듯?
    
    어차피 동전 수는 최대 10개니까 매번 돌아도 될듯
    """
    # 더이상 분배할 동전 없을때까지니까 price 로 while 문?
    change = price
    # 가장 큰 동전부터 사용
    for coin in reversed(pence):
        if change == 0:
            break
        if coin <= change:
            cnt, change = divmod(change, coin)
            answer += cnt
    
    
    return answer


if __name__ == "__main__":
    """
    input           result
    10 4200         6
    1
    5
    10
    50
    100
    500
    1000
    5000
    10000
    50000
    ==================================================
    10 4790         12
    1
    5
    10
    50
    100
    500
    1000
    5000
    10000
    50000
    """
    # input = sys.stdin.readline
    # N, K = map(int, input().split())
    # pence = [int(input().strip()) for _ in range(N)]
    # print(solution(pence, K))
    
    pence = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
    K = 4790
    print(solution(pence, K))
    