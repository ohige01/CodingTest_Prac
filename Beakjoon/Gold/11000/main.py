import sys

N = int(input())

subject = []
result = []     #각 강의의 종료시간 배열

for i in range(N):
    subject.append(list(map(int, sys.stdin.readline().split())))

subject.sort()  #입력값 정렬

result.append(subject[0][1])    #초기값 설정

for i in range(1, N):
    #강의의 최소 종료시간이 삽입될 강의 첫 시간보다 클 때 -> 새로 강의를 삽입해야 할때
    if(subject[i][0] < result[0]):      
        result.append(subject[i][1])    #완전 이진 트리의 마지막에 삽입

        index = len(result) - 1     #삽입한 인덱스 값
        parent_index = ((index + 1) // 2) - 1   #삽입한 인덱스의 부모 인덱스
        while(result[parent_index] > result[index] and parent_index >= 0):      #부모노드보다 자식노드가 작으면 실행
            tmp = result[parent_index]
            result[parent_index] = result[index]
            result[index] = tmp
            
            #바꾼뒤 인덱스값 재연산
            index = parent_index
            parent_index = ((index + 1) // 2) - 1

    else:   #강의를 뒷시간에 추가할 수 있을때
        result[0] = subject[i][1]   #제일 빨리 끝나는 강의 뒤에 붙여넣음

        index = 0
        #인덱스 값이 배열 크기를 넘길 때 처리
        child_left_index = index*2 + 1
        if(child_left_index >= len(result)):
            child_left_index = index
        child_right_index = index*2 + 2
        if(child_right_index >= len(result)):
            child_right_index = index

        #자식 노드를 비교했을 때 교환할 노드가 있다면
        while(result[child_left_index] < result[index] or result[child_right_index] < result[index]):
            change_index = -1
            #둘다 부모노드 보다 작다면
            if(result[child_left_index] < result[index] and result[child_right_index] < result[index]):
                #더 작은 노드를 선택
                if(result[child_left_index] <= result[child_right_index]):
                    change_index = child_left_index
                else:
                    change_index = child_right_index
            elif(result[child_left_index] < result[index]):
                change_index = child_left_index
            elif(result[child_right_index] < result[index]):
                change_index = child_right_index

            if(change_index > 0):
                tmp = result[change_index]
                result[change_index] = result[index]
                result[index] = tmp

                #바꾼뒤 인덱스 재연산
                index = change_index
                child_left_index = index*2 + 1
                if(child_left_index >= len(result)):
                    child_left_index = index
                child_right_index = index*2 + 2
                if(child_right_index >= len(result)):
                    child_right_index = index                         
print(len(result))