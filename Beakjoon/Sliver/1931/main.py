import sys

N = int(input())
time = []
cnt = 1
for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    time.append([end, start])

time.sort()
for i in range(1, N):
    if(time[i][1] >= time[0][0]):
        cnt += 1
        time[0][0] = time[i][0]

print(cnt)