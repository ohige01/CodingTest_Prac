import sys

N = int(input())
country_list = []
cnt_all = 0
for i in range(N):
    loc, cnt = map(int, sys.stdin.readline().split())
    cnt_all += cnt
    country_list.append([loc, cnt])

country_list.sort()

cnt_left = 0
cnt_right = cnt_all

for country in country_list:
    cnt_left += country[1]
    cnt_right -= country[1]
    if(cnt_left >= cnt_right):
        print(country[0])
        break