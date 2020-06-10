'''
ID: philoin1
LANG: PYTHON3
TASK: butter
'''
# Floyd-Warshall: O(P^3+PN), Bellman-Ford: O(NP^2)
from time import time
from collections import deque
start = time()
f = open('butter.in','r')
w = open('butter.out','w')
def split(string):
    return list(map(int,string.split()[:3]))
data = f.read().split('\n')
[N,P,C] = list(map(int,data[0].split()[:3]))
L = list(map(int,data[1:N+1])) #cow loc
TMP = list(map(split,data[N+1:N+1+C]))
E = [[] for _ in range(P+1)]
for [i,j,v] in TMP:
    E[i].append([j,v])
    E[j].append([i,v])
def bellman(p):
    D = [float('inf')]*(P+1)
    V = [False]*(P+1)
    D[p] = 0
    V[p] = True
    q = deque()
    q.append(p)
    while q:
        cur = q.popleft()
        V[cur] = False
        for [dest,dist] in E[cur]:
            if D[dest] > D[cur] + dist:
                D[dest] = D[cur] + dist
                if not V[dest]:
                    V[dest] = True
                    q.append(dest)
    res = 0
    for l in L:
        res += D[l]
    return res
MIN = float('inf')
for p in range(1,P+1):
    d = bellman(p)
    MIN = min(d,MIN)
w.write("%d\n"%MIN)
print(time()-start)