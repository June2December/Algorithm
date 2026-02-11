"""
Problem : N으로 표현
Site : https://school.programmers.co.kr/learn/courses/30/lessons/42895?language=python3
Type : DP

Note :
        1. 상태를 정의하고 / 문제 해결을 위한 state 변수들을 잘 생각해보자
        2. 점화식을 세우고 / 해당 상태가 어떻게 수집되는지 확인하고
        3. 계산 순서를 정하는 능력 / 해당 상태 최신화 하는법 생각하자

        그냥 작성하지 말고 점화식을 꼭 세워보자
"""
def solution(N, number):
    answer = 0
    """
    중요한건 숫자 언급한 횟수 네
    
    32,000 은 99999 를 9 로 나누면 11111이고 3번 더하면 넘는 수이고
    
    덧셈뺄셈을 최대한 안 할 수록 숫자를 적게 쓰는거라고 보장은 안되네
    
    N :
    1
        N = N
    2
        N / N = 1
        NN = NN
        N + N = 2N
    3
        NN / N = 11
        NN + N = ?
    
    우선 집합을 만들어 보면 될거 같기도 하고 어디까지 만들지
    """
    # 우선 예외처리
    if N == number:
        return 1
    
    # 최대 정답이 8일테니
    set_list = []
    for i in range(1, 9):
        temp = set()
        temp.add(int(str(N)  * i))
        set_list.append(temp)
        
    print(set_list)
    return answer

if __name__ == "__main__":
    """
    """

    solution([])
    