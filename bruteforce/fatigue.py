"""
Problem : 소수 찾기
Site : https://school.programmers.co.kr/learn/courses/30/lessons/42839
Type : Brute-Force

Note :
"""

from itertools import permutations
def solution(k, dungeons):
    answer = -1
    """
    DFS 이런식으로 하려고 했는데
    시작점 즉 던전을 처음꺼를 안가는것도 고려해야 하니
    FS 로 하면 던저 1곳 가고 거기서 다시 함수 재귀로 호출?
    그리고 순서 달려져도 결과 다르네...ㅠ
    
    그럼 어쩔수 없이 permutations 다 계산..?
    n n-1 n-2 ... / 8 이하라고 하니까
    괜찮을듯
    8 7 6 5 4 3 2 1 = 56 30 12 2 = 56 60 12 = 360 12 = 약 5000 도합 5만도 안되네
    """
    n = len(dungeons)
    # 던전 몇개갈 수 있을진 가봐야 알테니 최대한 긴거부터 확인하고 긴거 나오면 바로 반환
    # print(list(permutations(dungeons, n)))
    
    while n > 0:
        permute = list(permutations(dungeons, n))
        for seq in permute:
            hp = k
            flag = True
            for minimum, consume in seq:
                if minimum > hp:
                    flag = False
                    break
                hp -= consume
            if flag:
                return n
                
        n -= 1
        
    
    
    return answer

if __name__ == "__main__":
    """
    k	dungeons	                result
    80	[[80,20],[50,40],[30,10]]	3
    """
    
    print(solution(80, [[80,20],[50,40],[30,10]]))
    