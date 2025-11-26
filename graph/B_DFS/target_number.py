"""
Problem : 타겟 넘버
Site : https://school.programmers.co.kr/learn/courses/30/lessons/43165
Type : Recursive + DFS

Note :  재귀함수를 구현하는 방식 답안 참조
"""

def solution(numbers, target):
    answer = 0
    """
    리스트 길이랑 동일하게 -1, 1 조합을 만들어? / 메모리가 아깝다
    
    DFS 로 모든 경우의 수를 다 뒤져보자? / 모든 분기를 다 가보긴 해야하네
    1. {현재에서 (+/-) 탐색하고 다음} == 재귀구나
    2. 총합 = func(현재 위치, 총합)
    3. 다 돌았으면 정지조건
    """
    
    length = len(numbers)
    
    def dfs(cur_idx, cur_sum):
        nonlocal answer
        # 종료 조건
        if cur_idx == length:
            if cur_sum == target:
                answer += 1
            return
        # +
        dfs(cur_idx+1, cur_sum + numbers[cur_idx])
        # -
        dfs(cur_idx+1, cur_sum - numbers[cur_idx])
    
    
    # 첫 스타트
    dfs(0, 0)
    return answer

if __name__ == "__main__":
    print(solution([1, 1, 1, 1, 1], 3))  # 5
    print(solution([4, 1, 2, 1], 4))     # 2