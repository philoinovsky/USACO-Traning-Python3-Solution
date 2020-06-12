'''
ID: philoin1
LANG: PYTHON3
TASK: range
'''
f = open('range.in', 'r')
w = open('range.out', 'w')
#O(N^2)
data = f.read().split('\n')
N = int(data[0])
G = [list(s) for s in data[1:N+1]]
dp = [[0]*(N+1) for _ in range(N+1)]
res = [0] * (N+1)
for i in range(1,N+1):
    for j in range(1,N+1):
        if G[i-1][j-1] != '0':
            dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1
            if dp[i][j] > 1:
                res[dp[i][j]] += 1
SUM = sum(res)
for i,v in enumerate(res):
    if v != 0:
        w.write("%d %d\n"%(i,SUM))
        SUM -= v