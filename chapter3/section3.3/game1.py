'''
ID: philoin1
LANG: PYTHON3
TASK: game1
'''
f = open('game1.in', 'r')
w = open('game1.out', 'w')
ITER = iter(f.read().split('\n'))
N = int(next(ITER))
L = []
while len(L) < N:
    L += list(map(int,next(ITER).split()))
if N == 1:
    w.write("%d %d\n"%(L[0],0))
#O(N^2)
dp = [[0]*N for _ in range(N)]
for i in range(N):
    dp[i][i] = L[i]
for i in range(N-1):
    dp[i][i+1],dp[i+1][i] = (L[i],L[i+1]) if L[i] > L[i+1] else (L[i+1],L[i])
for k in range(2,N):
    for i in range(N-k):
        j = i + k
        dp[i][j] = max(L[i]+dp[j][i+1],L[j]+dp[j-1][i])
        dp[j][i] = min(dp[i][j-1],dp[i+1][j])
w.write("%d %d\n"%(dp[0][-1],dp[-1][0]))