import sys
def input():
    return sys.stdin.readline()

N = int(input())
A = list(map(int, input().split()))
S = int(input())

while(True):
    for i in range(1, N):
        if(A[i-1] < A[i]):
            tmp = A[i-1]
            A[i-1] = A[i]
            A[i] = tmp

            S -= 1
            if(S == 0):
                break
            else:
                continue
    break

print(*A)