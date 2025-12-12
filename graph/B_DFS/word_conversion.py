"""
Problem : 단어 변환
Site : https://school.programmers.co.kr/learn/courses/30/lessons/43163
Type : B_DFS

Note : 역시나!! 국룰 국룰 국룰!!
"""


from collections import deque
def solution(begin, target, words):
    answer = 0
    """
    사전에 있는것 중 하나만 바뀌였다면 바꿀 수 있고
    
    최소비용으로 바꾸니까 BFS 지?
    국룰 visited 를 words 랑 똑같아지면 멈추게 되는게 맞지?
    words 를 visited 처럼 쓰면서 뽑으면 되나 / 최대 길이 50이라 n 번 도는건 문제 없지 않을가 싶은데
    1. [] 만들고 현재꺼 넣어
            2. 현재꺼가 target이면 반환
            3. 현재단어랑 한단어 다르면 words 에서 빼기
            4. 그 단어를 [] 에 삽입
        5. 2,3,4 반복
    """
    if target not in words:
        return answer
    seq = deque([(begin, 0)])
    word_length = len(begin)
    visited = [False] * len(words)
    while seq:
        cur, cost = seq.popleft()
        
        # 달성!
        if cur == target:
            return cost
        for idx, word in enumerate(words):
            if visited[idx] == False:
                # 한 단어만 다른지 체크
                count = 0
                for j in range(word_length):
                    if word[j] == cur[j]:
                        count += 1
                # 같으니까 한 글자만 다른거
                if count == (word_length-1):
                    seq.append((word, cost+1))
                    visited[idx] = True
    return answer

if __name__ == "__main__":
    """
    begin       target          words                                       return 
    'hit'       'cog'           ["hot", "dot", "dog", "lot", "log", "cog"]  4
    'hit'       'cog'           ["hot", "dot", "dog", "lot", "log"]         0
    """
    
    print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
    print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]))
    