"""
Problem : 체육복 
Site : https://school.programmers.co.kr/learn/courses/30/lessons/42862
Type : Greedy

Note :  그리디는 어떻게 풀어야 잘 풀까
        순간마다 가장 좋아 보이는걸로 해도 잘 해결될 거 같을때

1. 그리디 전략은 ㄱㅊ은듯 / 앞 번호부터 빌려주는것도 ㄱㅊ

2. for 문 안 index 는 결국 ==>> 이중 for
    - new_reserve = reserve[:] / .copy() / set() 이 적절한 대안이라고 하네
    - 


"""


"""
def solution(n, lost, reserve):
    # 1. 집합으로 변환 (중복 제거 + O(1) 탐색)
    lost_set = set(lost)
    reserve_set = set(reserve)

    # 2. 여벌도 있었는데 잃어버린 학생 (교집합) 먼저 처리
    overlap = lost_set & reserve_set
    lost_set -= overlap        # lost에서 제거
    reserve_set -= overlap     # reserve에서도 제거

    # 3. 빌려줄 수 있는 학생들(번호 순) 기준으로 앞/뒤 학생에게 빌려주기
    for r in sorted(reserve_set):
        # 앞번호 학생에게 먼저
        if r - 1 in lost_set:
            lost_set.remove(r - 1)
        # 아니면 뒷번호 학생
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)

    # 4. 전체 인원 - 아직도 체육복이 없는 인원
    return n - len(lost_set)

"""

def solution(n, lost, reserve):
    answer = 0
    
    """
    - 주변인한테만 빌리기 가능
    - 여분 있는데 잃어버렸음 자기가 입어야지 여분
    - 인원 적어서 순회 쉽
    
    일단 돌면서 없는애 다 적어 / 이때 여분 있는애는 적지말고 reserve 에서 없애
    앞에놈부터 빌려주면 되네
    """
    # 일단 돌면서 없는애 다 적어 / 이때 여분 있는애는 적지말고 reserve 에서 없애
    students = [1] * (n+1)
    students[0] = 0
    for i in range(1, n+1):
        # 잃어버린애
        if i in lost:
            # 여분 없으면 일단 적어
            if i not in reserve:
                students[i] = 0
            # 여분 있으면 적지마 / 그대신 reserve 에선 없애
            else:
                idx = reserve.index(i)
                reserve.pop(idx)
    
    # 이제 다시 돌면서 없는애 기준 앞 뒷 놈 빌릴 수 있음 빌려
    for i in range(1, n+1):
        if students[i] == 0:
            if (i-1) in reserve:
                idx = reserve.index(i-1)
                reserve.pop(idx)
                students[i] = 1
            elif (i+1) in reserve:
                idx = reserve.index(i+1)
                reserve.pop(idx)
                students[i] = 1
    
    
    return sum(students)


if __name__ == "__main__":
    """
    n	lost	reserve	    return
    5	[2, 4]	[1, 3, 5]	5
    5	[2, 4]	[3]	        4
    3	[3]	    [1]	        2
    """
    print(solution(5, [2, 4], [1,3,5]))
    print(solution(5, [2, 4], [3]))
    print(solution(3, [3], [1]))
    