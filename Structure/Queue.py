# 큐 선언
list_q = []

# 입력
while(1):
    print("enqueue: 0, dequeue: 1, exit: -1")
    menu = int(input("input: "))
    if menu == -1:
        exit()
    elif menu == 0:
        #push 연산
        x = int(input("typing the value: "))
        list_q.append(x)
    elif menu == 1:
        if len(list_q) > 0 :
            #pop 연산
            list_q.pop(0)
    else:
        print("invalid value")

    #리스트 출력
    print("Queue:", end=" ")
    print(list_q)
    print()