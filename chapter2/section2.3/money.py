'''
ID: philoin1
LANG: PYTHON3
TASK: money
'''
f = open('money.in', 'r')
w = open('money.out', 'w')
ITER = iter(f.read().split('\n'))
[V, N] = list(map(int,next(ITER).split()))
coins = []
while len(coins) < V:
    coins += list(map(int,next(ITER).split()))
dp = [1] + [0] * N
for i in coins:
    for j in range(i,N+1):
        dp[j] += dp[j-i]
w.write("%d\n"%dp[-1])