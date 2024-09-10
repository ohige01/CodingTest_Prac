import sys
sys.setrecursionlimit(10**6)    #jjjuni

N = int(sys.stdin.readline())
spot_list = [[] for i in range(N + 1)]
result = [0] * N
for i in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    spot_list[a].append(b)
    spot_list[b].append(a)

def findParentNode(node):
    for spot in spot_list[node]:
        if(result[spot - 1] == 0):
            result[spot - 1] = node
            findParentNode(spot)
        

findParentNode(1)

for i in range(1, N):
    print(result[i])