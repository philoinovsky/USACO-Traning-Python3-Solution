'''
ID: philoin1
LANG: PYTHON3
TASK: inflate
'''
#time O(MN)
f = open('inflate.in', 'r')
w = open('inflate.out', 'w')
data = f.read().split('\n')
def split(string):
    return list(map(int,string.split()))
[M,N] = list(map(int,data[0].split()))
L = list(map(split,data[1:N+1]))
#unbound knapsack, TLE, O(N^2)
dp = [0] * (M+1)
for i in range(N):
    V = L[i][0]
    W = L[i][1]
    for j in range(W,M+1):
        if dp[j-W]+V > dp[j]:
            dp[j] = dp[j-W]+V
w.write("%d\n"%dp[-1])