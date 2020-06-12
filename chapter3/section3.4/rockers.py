'''
ID: philoin1
LANG: PYTHON3
TASK: rockers
'''
f = open('rockers.in', 'r')
w = open('rockers.out', 'w')
data = f.read().split('\n')
#O(MNT)
[N,T,M] = list(map(int,data[0].split()))
L = list(map(int,data[1].split()[:N]))
dp = [[0]*(T+1) for _ in range(M+1)]
for t in L:
    for i in range(M,0,-1):
        for j in range(T,t-1,-1):
            dp[i][j] = max(dp[i][j],dp[i-1][-1]+1,dp[i][j-t]+1)
w.write("%d\n"%dp[-1][-1])