'''
ID: philoin1
LANG: PYTHON3
TASK: subset
'''
f = open('subset.in', 'r')
w = open('subset.out', 'w')
data = f.read().split('\n')
N = int(data[0])
if N % 4 in [1,2]:
    w.write("0\n")
    exit()
target = sum(range(1,N+1))//2
dp = [1] + [0] * target
for i in range(1,N+1):
    for j in range(target,i-1,-1):
        dp[j] += dp[j-i]
w.write("%d\n"%(dp[target]//2))