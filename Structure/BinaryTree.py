inOrderTree = []
preOrderTree = []
postOrederTree = []

# 입력
while(1):
    print("insert: 0, delete: 1, exit: -1")
    menu = int(input("input: "))
    if menu == -1:
        exit()
    elif menu == 0:
        #insert 연산
        x = int(input("typing the value: "))
        
    elif menu == 1:
        if len(inOrderTree) > 0 :
            #delete 연산
            print()     
    else:
        print("invalid value")

    #리스트 출력
    print("InOrderTree(중위):", end=" ")
    print(inOrderTree)
    print("PreOrderTree(전위):", end=" ")
    print(preOrderTree)
    print("PostOrederTree(후위):", end=" ")
    print(postOrederTree)
    print()