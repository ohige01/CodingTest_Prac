import sys
sys.setrecursionlimit(10**6)    #jjjuni

N = int(sys.stdin.readline())
spot_list = [[] for i in range(N + 1)]
result = [0] * N
for i in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    # 인접 리스트 형식
    spot_list[a].append(b)
    spot_list[b].append(a)

# dfs형식으로 그래프 순회
def findParentNode(node):
    for spot in spot_list[node]:
        # 저장되지 않은 지점을 만나면 저장
        if(result[spot - 1] == 0):
            result[spot - 1] = node
            findParentNode(spot)
        

findParentNode(1)

for i in range(1, N):
    print(result[i])