# 스택 선언
list_s = []

# 입력
while(1):
    print("push: 0, pop: 1, exit: -1")
    menu = int(input("input: "))
    if menu == -1:
        exit()
    elif menu == 0:
        #push 연산
        x = int(input("typing the value: "))
        list_s.append(x)
    elif menu == 1:
        if len(list_s) > 0 :
            #pop 연산
            list_s.pop()
    else:
        print("invalid value")

    #리스트 출력
    print("Stack:", end=" ")
    print(list_s)
    print()