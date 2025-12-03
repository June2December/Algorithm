"""
Problem : 단속카메라
Site : https://school.programmers.co.kr/learn/courses/30/lessons/42884
Type : Greedy

Note : 그리디, 특정 선택을 할때의 최적의 선택을 하는것도 중요하지만 특정 상태를 맞추는것도 그리디가 되는구나
아래 식처럼 하면 처음 item 도 순회 가능하고 메모리도 아끼는 구나..

def solution(routes):
    routes.sort(key=lambda x: x[1])  # 진출 시점 기준 정렬
    answer = 0
    cam = -30001  # 최소 위치보다 왼쪽

    for s, e in routes:
        if cam < s:          # 현재 카메라 위치로는 이 차를 못 찍음
            answer += 1
            cam = e          # 이 차 진출 지점에 새 카메라 설치

    return answer
"""


def solution(routes):
    answer = 1
    
    """
    최대한 많은애를 같음 묶음으로 묶기,,,
    뒤에서부터 들어온 차 확인하면서 진출 위치의 최소값 진입 위치의 최댓값 비교하면 되네
    """
    # 일단 sort
    routes.sort(key=lambda x : x[0])
    # 최소 최대 첫 값 저장
    in_range, out_range = routes[0]
    for i, o in routes[1:]:
        # 이번꺼 같이 묶을 수 있 / answer += 0, in, out 최신화
        if out_range >= i:
            in_range = i
            out_range = out_range if out_range <= o else o
        # 이번꺼 같이 못 묶음
        else:
            answer += 1
            in_range, out_range = i, o
    return answer


if __name__ == "__main__":
    """
    routes                                      return
    [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]   2
    """
    print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))
    