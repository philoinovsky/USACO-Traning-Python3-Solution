'''
ID: philoin1
LANG: PYTHON3
TASK: stamps
'''
#TLE
f = open('stamps.in', 'r')
w = open('stamps.out', 'w')
ITER = iter(f.read().split('\n'))
[K, N] = list(map(int,next(ITER).split()))
L = []
while len(L) < N:
    L += list(map(int,next(ITER).split()))
ID = 0
dp = [float('inf')] * 2000000
for i in L:
    dp[i] = 1
while True:
    ID += 1
    for i in L:
        if ID - i > 0:
            if dp[ID-i]+1 < dp[ID]:
                dp[ID] = dp[ID-i]+1
    if dp[ID] > K:
        w.write("%d\n"%(ID-1))
        exit()