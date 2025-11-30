"""
Problem : 큰 수 만들기
Site : https://school.programmers.co.kr/learn/courses/30/lessons/42883
Type : Greedy

Note :  그리디 == 국소최적이 전역최적이 될것이다
"그리디 알고리즘을 적용하면 가능할것 이다" 라는 생각 을 하려면 A 환경(국소)에서 B 만 해두면 되는구나 라는 개념까진 이제 알겠다
"""


def solution(number, k):
    answer = ''
    """
    숫자 최대 백만개.? / 그럼 숫자 뺄거 고르는건 nC* 여서 이런방식 풀이는 아니네
    그리디는 국소최소가 전역 최소일때 젤 효율적일것이다 라는거니까
    
    길이-k 개 숫자 뽑기
    0. temp = len(number) - k
    1. 0~k-1 까지에서의 최댓값 중 가장 왼쪽 하나 / i
    2. i~k 까지에서의 최댓값 중 가장 왼쪽 하나 / i
    n-k 번 돌고 n 번탐색이니까 너무 안좋은데...
    
    그러지 말고 매번 돌면 오래걸리니 임시 저장공간 만들어서 현재까지 최댓값 넣어구면 되네
    숫자 순회는 해야 되고
    지워야 하는 갯수 k
    임시저장소 temp 만들고
    
    temp[-1] < 이번숫자 / 아직 지워야 하는 갯수 남았다면 빼버려
    temp[-1] > 이번숫자 / 그럼 기존에 있던게 큰거 맞으니까 냅둬
    k 다 못지우면 슬라이싱 하면 될듯
    """
    # 전체 길이
    n = len(number) - k
    temp = []
    
    # 일다 순회
    for num in number:
        while temp and temp[-1] < num and k > 0:
            temp.pop()
            k -= 1
        temp.append(num)
    
    
    
    # 아직 다 못 지웠음 슬라이싱
    return "".join(temp[:n])



if __name__ == "__main__":
    """
    number          k       return
    "1924"          2       "94"
    "1231234"       3       "3234"
    "4177252841"    4       "775841"
    """
    print(solution("1924", 2))
    print(solution("1231234", 3))
    print(solution("4177252841", 4))
    