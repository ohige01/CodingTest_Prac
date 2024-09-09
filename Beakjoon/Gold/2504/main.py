stack = [] #괄호 스택
stack_op = [] #연산자 스택
stack_num = [1] #숫자 스택
state = True

letter = input()

for i in range(len(letter)):
    # 여는 괄호를 만나면 push
    if(letter[i]=='(' or letter[i]=='['):
        # 여는 괄호 뒤에 닫는 괄호가 있다면 + 추가
        if(i > 0):
            if(letter[i-1]==')' or letter[i-1]==']'):
                stack_op.append('+')
                stack_num.append(1)
        # 각 괄호에 맞춰서 연산 추가
        if(letter[i]=='('):
            stack_op.append("*2")
        elif(letter[i]=='['):
            stack_op.append("*3")
        stack.append(letter[i])
    # 닫는 괄호를 만나면 pop
    elif(letter[i]==')' or letter[i]==']'):
        # 스택이 비어있는가
        if(len(stack) != 0):
            # 괄호가 올바르게 짝지어져 있는가 검사 
            if(letter[i] == ')'):
                if(stack.pop() != '('):
                    state = False
                    break
            elif(letter[i] == ']'):
                if(stack.pop() != '['):
                    state = False
                    break 
            # 연산
            op = stack_op.pop()
            if(op == "*2"):
               stack_num.append(stack_num.pop() * 2) 
            elif(op == "*3"):
               stack_num.append(stack_num.pop() * 3) 
            elif(op == '+'):           
                stack_num.append(stack_num.pop() + stack_num.pop())
                # +연산할 시 뒤에 있는 연산도 함께 실행
                op = stack_op.pop()
                # 다수의 +가 있을시 모두 처리
                while(op == "+"):
                    stack_num.append(stack_num.pop() + stack_num.pop())
                    op = stack_op.pop()
                if(op == "*2"):
                    stack_num.append(stack_num.pop() * 2) 
                elif(op == "*3"):
                    stack_num.append(stack_num.pop() * 3)                    
        else:
            state = False
            break
    # 다른 괄호 및 문자가 들어올시
    else:
       state = False
       break 
# 입력된 문자열을 끝냈을 때 스택이 비어있는가        
if(len(stack)!=0):
    state = False

result = sum(stack_num)
if(state and result != 1):
    print(result)
else:
    print(0)