"""
Problem : 조이스틱
Site : https://school.programmers.co.kr/learn/courses/30/lessons/42860
Type : Greedy

Note :  가장 적게 움직이는 방법찾기였네..

1. sportswear 문제에서도 그랬듯이 문제를 나누는게 중요한듯
2. 그리디 == 국소 최적이 전역 최적이 될것이란 믿음

"""

def solution(name):
    answer = 0
    """
    왜 예시 JAZ 에서 A는 이동하는데 Z는 이동 안하냐 / 아 A 거꾸로구나
    
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 
    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
    JEROEN : 9 + 최초1번? + 4 + 9 + 12 + 4 + 11 = 50? / A 가 골때리네
    A 가 연속일때 반대로 가면서 스킵할수 있어야 하네
    
    26에서 본인 숫자 빼서 작은 놈 더하면 되네
    """
    # 우선 알파벳-숫자 사전 만들자
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha = {alpha:i for i, alpha in enumerate(alphabet, 0)}
    # A 만나면 패싱? / 연속이면 돌아가는게 저렴할지도 
    for w in name:
        temp1 = alpha[w]; temp2 = 26-temp1;
        score = min(temp1, temp2)
        answer += score
        
        
    # 가로 따로 다시 세자..
    n = len(name)
    move = n - 1
    for i in range(n):
        right = i + 1
        
        # A 라면 건너뛰기
        while right < n and name[right] == "A":
            right += 1
        # 1 : 정방향 가다가 빠꾸
        move = min(move, 2*i + n - right)
        # 2. 역방향 가다가 빠꾸
        move = min(move, i+2*(n-right))
    return answer + move

if __name__ == "__main__":
    """
    JAZ / 11
    JEROEN / 56
    JAN / 23
    """
    print(solution("JAZ"))
    print(solution("JEROEN"))
    print(solution("JAN"))
    