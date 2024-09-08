def solution(s):
    stack = []
    state = True

    for letter in s:
        # 여는 괄호를 만나면 push
        if(letter=='('):
            stack.append('(')
        # 닫는 괄호를 만나면 pop
        elif(letter==")"):
            #stack이 비어있는가
            if(len(stack)!=0):
                stack.pop()
            else:
                state = False
                break

    # 입력된 문자열을 끝냈을 때 스택이 비어있는가        
    if(len(stack)!=0):
        state = False

    return state

s = input()
print(solution(s))