'''
ID: philoin1
LANG: PYTHON3
TASK: sort3
'''
f = open('sort3.in', 'r')
w = open('sort3.out', 'w')
data = f.read().split('\n')
N = int(data[0])
nums = list(map(int,data[1:N+1]))
cnt = [0] * 3
all = [[0] * 3 for _ in range(3)]
for i in nums:
    cnt[i-1] += 1
start, stop = 0, cnt[0]
for idx in range(3):
    for i in nums[start:stop]:
        all[idx][i-1] += 1
    if idx != 2:
        start += cnt[idx]
        stop += cnt[idx+1]
ex = 2*(cnt[0] - all[0][0]) - min(all[0][1],all[1][0]) - min(all[0][2],all[2][0]) + min(all[1][2],all[2][1])
w.write("%d\n"%ex)