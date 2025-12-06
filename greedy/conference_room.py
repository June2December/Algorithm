"""
Problem : 동전 0
Site : https://www.acmicpc.net/problem/1931
Type : Greedy

Note : ...
"""
import sys
def solution(time_table):
    answer = 0
    """
    맨 먼저 시작한다고 해서 바로 껴주면 안되네..
    스타트를 누구로 끊어야 하지
    끝나는 애 기준으로 보면
        그 시각 뒤로는 젤 먼저 시작해서 젤 먼저 끝나는 애를 찾아야 하네
            이때 끝나는시간이 현재보다 늦지만 시작은 늦은 애는 건너 뛰고
    """
    time_table.sort(key = lambda x : (x[1], x[0]))
    
    _end = 0
    length = len(time_table)
    present = 0
    for start, end in time_table:
        if _end <= start:
            answer += 1
            _end = end
    return answer


if __name__ == "__main__":
    """
    input           result
    11              4
    1 4
    3 5
    0 6
    5 7
    3 8
    5 9
    6 10
    8 11
    8 12
    2 13
    12 14
    """
    # input = sys.stdin.readline
    # N = int(input().strip()))
    # time_table = []
    # for _ in range(N):
    #     s, e = map(int, input().split())
    #     time_table.append([s, e])
    # print(solution(time_table))
    time_table = [
        [1, 4],
        [3, 5],
        [0, 6],
        [5, 7],
        [3, 8],
        [5, 9],
        [6, 10],
        [8, 11],
        [8, 12],
        [2, 13],
        [12, 14]
    ]
    print(solution(time_table))
    