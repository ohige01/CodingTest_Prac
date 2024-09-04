import sys
from collections import deque

# 큐 선언(일반 리스트로 처리하면 시간초과) 
list_q = deque([])
size = 2000000
index = 0

# 입력
for i in range(int(input())):
    #for문에서 input 쓰면 시간초과 뜸
    menu = list(map(str, sys.stdin.readline().split()))
    #push
    if(menu[0] == "push"):
        list_q.appendleft(menu[1])
    
    #pop
    elif(menu[0] == "pop"):
        if len(list_q) > 0 :
            print(list_q.pop())
        else:
            print(-1)
    
    #size
    elif(menu[0] == "size"):
        print(len(list_q))
    
    #empty
    elif(menu[0] == "empty"):
        if len(list_q) > 0 :
            print(0)
        else:
            print(1)
    
    #front
    elif(menu[0] == "front"):
        if len(list_q) > 0 :
            print(list_q[len(list_q) - 1])
        else:
            print(-1)
    
    #back
    elif(menu[0] == "back"):
        if len(list_q) > 0 :
            print(list_q[0])
        else:
            print(-1)