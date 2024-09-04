import sys

# 스택 선언
list_s = []

# 입력
for i in range(int(input())):
    #for문에서 input 쓰면 시간초과 뜸
    menu = list(map(str, sys.stdin.readline().split()))
    #push
    if(menu[0] == "push"):
        list_s.append(int(menu[1]))
    
    #pop
    elif(menu[0] == "pop"):
        if len(list_s) > 0 :
            print(list_s.pop())
        else:
            print(-1)
    
    #size
    elif(menu[0] == "size"):
        print(len(list_s))
    
    #empty
    elif(menu[0] == "empty"):
        if len(list_s) > 0 :
            print(0)
        else:
            print(1)
    
    #top
    elif(menu[0] == "top"):
        if len(list_s) > 0 :
            print(list_s[len(list_s) - 1])
        else:
            print(-1)