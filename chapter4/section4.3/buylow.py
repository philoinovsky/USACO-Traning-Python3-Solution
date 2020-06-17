'''
ID: philoin1
LANG: PYTHON3
TASK: buylow
'''
f = open('buylow.in', 'r')
w = open('buylow.out', 'w')
data = f.read().split('\n')
#O(N^2) TLE pass 9/10
N = int(data[0])
L = []
i = 1
while len(L) < N:
    L.extend(list(map(int,data[i].split())))
    i += 1
L.append(0)
N += 1
dp = [1] * N
num = [1] * N
for i in range(1,N):
    visited = set()
    candi = [0]
    count = 0
    for j in range(i):
        if L[j] > L[i]:
            candi.append(dp[j])
    dp[i] = max(candi) + 1
    for j in range(i-1,-1,-1):
        if L[j] > L[i] and dp[j] + 1 == dp[i] and L[j] not in visited:
            count += num[j]
            visited.add(L[j])
    num[i] = count if count else 1
w.write("%d %d\n"%(dp[-1]-1,num[-1]))