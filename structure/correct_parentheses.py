"""
Problem : 올바른 괄호
Site : https://school.programmers.co.kr/learn/courses/30/lessons/12909
Type : stack queue

Note :
"""
import math
import sys
from collections import deque
def solution(s):
    answer = True
    """
    ( 나오면 스택에 넣고
    ) 나오면 직전거 봐서 짝꿍이면 빼고
    """
    stack = []
    for parantheses in s:
        if parantheses == "(":
            stack.append(parantheses)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
                continue
            return False
        
    return False if stack else True

if __name__ == "__main__":
    """
    s	        answer
    "()()"	    true
    "(())()"	true
    ")()("	    false
    "(()("	    false
    """
    
    print(solution("()()"))
    print(solution("(())()"))
    print(solution(")()("))
    print(solution("(()("))
    
    