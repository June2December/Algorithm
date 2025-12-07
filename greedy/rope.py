"""
Problem : 로프
Site : https://www.acmicpc.net/problem/2217
Type : Greedy

Note : 그리디 문제를 풀때 무시해도 될것을 판단 잘해서 단순 조건문이 최적의 선택을 할 수 있도록 하는걸 유도해야 하네
역으로
단순 조건문으로 최적의 선택 하면 그리디 가능한가 고민해봐야 할듯
"""
import sys
def solution(ropes):
    answer = 0
    """
    길이가 주어지진 않네
    최대한 본인 중량을 다 쓰는 방향
    최대한 많은 밧줄 연결하면 좋지
    
    Ex) 3 3 3 6 9
    3씩 가해지게 3 x 5 가 최대
    6 x 2 보다 크네
    
    아 오름차순으로 정렬하고 그 잘리는 구간으로 갯수 곱하기 가장 작은값 해서 비교
    모든 방식을 다 시도 해야 될수도 있네 호나 100 드는애 나올 수 있으니
    """
    length = len(ropes)
    ropes.sort()
    # 각 시도마다 들 수 있는 중량 저장용 list
    scores = list()
    # 각 시도마다 로프에 가해지는 부하를 저장해놔야 같은거 안하지
    tries = set()
    for idx, rope in enumerate(ropes):
        if rope not in tries:
            tries.add(rope)
            score = (length-idx) * rope
            scores.append(score)
    return max(scores)


if __name__ == "__main__":
    """
    input           result
    2               20
    10
    15
    """
    # input = sys.stdin.readline
    # N = int(input().strip())
    # ropes = []
    # for _ in range(N):
    #     rope = int(input().strip()))
    #     ropes.append(rope)
    # print(solution(ropes))
    ropes = [10, 15]
    print(solution(ropes))
    