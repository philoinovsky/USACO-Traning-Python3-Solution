'''
ID: philoin1
LANG: PYTHON3
TASK: nocows
'''
f = open('nocows.in', 'r')
w = open('nocows.out', 'w')
[N, K] = list(map(int,f.read().split('\n')[0].split()))
dp = [[0]*(K+1) for _ in range(N+1)] #deoth <= k
for i in range(1,K+1):
    for j in range(1,N+1,2):
        if j == 1:
            dp[j][i] = 1
        for k in range(1,j-1,2):
            dp[j][i] = (dp[j][i]+dp[k][i-1]*dp[j-1-k][i-1])%9901
w.write("%d\n"%((dp[N][K]-dp[N][K-1])%9901))