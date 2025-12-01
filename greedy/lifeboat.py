"""
Problem : 구명보트
Site : https://school.programmers.co.kr/learn/courses/30/lessons/42885
Type : Greedy

Note :  주석에 달아둔 내 첫 직관도 greedy 입장에서 가능한 풀이지
다만 O(n^2) 는 피해야지
"""

def solution(people, limit):
    answer = 0
    
    """
    len(people) <= 50,000
    40 ~ 240
    
    보트에 무거운 애부터 태워, 그 다음으로 무거운애 태워 / n x n 차원이네..
    보트에 무거운 애부터 태워, 남은 무게 에 대해 가벼운 애들 태워 / 항상 가득 태워 보내기
    뒤에서 뽑고 앞에서 뽑고 또 뽑을 수 있으면 
    
    241 길이 배열 만들어서 명수 세두고 해볼까?
    """
    # 일단 준비
    right = len(people) - 1
    left = 0
    people.sort()
    
    # 순회, 무거운애 1 + 가벼운애 가능하면 +1
    # pop 하면 안되는구나 list 당겨 적어야 되서..ㅠㅠ
    # 마지막 한명 남으면 right == left 될 수 도 있네
    while left <= right:
        # 무거운애, 가벼운애
        heavy, light = people[right], people[left]
        add = heavy + light
        if add > limit:
            right -= 1
        else:
            right -= 1
            left += 1
        # 보트 태워 보내고 갯수 세기
        answer += 1
    
    return answer



if __name__ == "__main__":
    """
    people              limit   return
    [70, 50, 80, 50]    100     3
    [70, 80, 50]        100     3
    """
    print(solution([70, 50, 80, 50], 100))
    print(solution([70, 80, 50], 100))
    