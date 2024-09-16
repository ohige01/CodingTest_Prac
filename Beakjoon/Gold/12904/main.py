S = input()
T = input()

#T에서 S로 가도록 탐색
for i in range(len(T) - len(S)):
    if(T[-1] == 'A'):   #뒷 문자가 A면 뒤에 문자 삭제
        T = T[0:-1]
    elif(T[-1] == 'B'): #뒷 문자가 B면 삭제한 뒤 뒤집기
        T = T[0:-1]
        T = T[::-1]

#연산한 결과가 S와 같은지 검사
if(S == T):
    print(1)
else:
    print(0)