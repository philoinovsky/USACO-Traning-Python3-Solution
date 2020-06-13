'''
ID: philoin1
LANG: PYTHON3
TASK: fence6
'''
from copy import deepcopy
f = open('fence6.in', 'r')
w = open('fence6.out', 'w')
data = f.read().split('\n')
N = int(data[0])
G = [[float('inf')] * (N+2) for _ in range(N+2)]
d = dict()
def do(record,cnt):
    LIST = record + [s]
    LIST.sort()
    if d.get(str(LIST)):
        V = d[str(LIST)]
    else:
        V = cnt
        d[str(LIST)] = V
        cnt += 1
    return cnt,V
cnt = 1
for i in range(N):
    [s, L, n0, n1] = list(map(int,data[1+3*i].split()))
    record0 = list(map(int,data[2+3*i].split()))
    record1 = list(map(int,data[3+3*i].split()))
    cnt,V0 = do(record0,cnt)
    cnt,V1 = do(record1,cnt)
    G[V0][V1] = G[V1][V0] = L
N = cnt-1
D = deepcopy(G)
MIN = float('inf')
#Floyd Minimum Loop
for k in range(1,N+1):
    for i in range(1,k):
        for j in range(1,i):
            MIN = min(MIN,D[i][j]+G[j][k]+G[k][i])
    for i in range(1,N+1):
        for j in range(1,i):
            if D[i][k] + D[k][j] < D[i][j]:
                D[i][j] = D[j][i] = D[i][k] + D[k][j]
w.write("%d\n"%MIN)