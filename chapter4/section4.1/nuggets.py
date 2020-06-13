'''
ID: philoin1
LANG: PYTHON3
TASK: nuggets
'''
f = open('nuggets.in', 'r')
w = open('nuggets.out', 'w')
data = f.read().split('\n')
N = int(data[0])
L = list(map(int,data[1:1+N]))
L.sort()
dp = [float('inf')] * L[0]
T = [float('inf')] * L[0]
for l in reversed(L):
    dp[l%L[0]] = l
    T[l%L[0]] = l
for i in range(1,L[0]):
    v = T[i]
    if v != float('inf'):
        for j in range(i,i+L[0]):
            j = j % L[0]
            dp[j] = min(dp[j-i]+v,dp[j])
MAX = float('-inf')
for i in dp:
    if i == float('inf'):
        w.write("0\n")
        exit()
    else:
        MAX = max(MAX,i-dp[0])
w.write("%d\n"%MAX)
