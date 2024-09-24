import sys
from functools import cmp_to_key

def compare_letter(a, b):
    a_str = str(a)
    b_str = str(b)

    if(int(a_str+b_str) > int(b_str+a_str)):
        return -1
    elif(int(a_str+b_str) < int(b_str+a_str)):
        return 1
    else:
        return 0
        
def solution(numbers):
    numbers.sort(key=cmp_to_key(compare_letter))
    answer = ''
    for i in numbers:
        answer += str(i)
    return str(int(answer))

numbers = list(map(int, sys.stdin.readline().split()))
print(solution(numbers))