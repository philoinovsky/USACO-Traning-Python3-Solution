'''
ID: philoin1
LANG: PYTHON3
TASK: cowtour
'''
from functools import lru_cache
from math import sqrt
f = open('cowtour.in', 'r')
w = open('cowtour.out', 'w')
data = f.read().split('\n')
def split(string):
    return list(map(int,string.split()[:2]))
def warshall():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
    for i in range(N):
        D[i][i] = 0
    return
@lru_cache(None)
def diameter(num):
    PP = P[num]
    max_dia = float('-inf')
    for i in PP:
        max_dia = max(max_dia,findmax(i,num))
    return max_dia
@lru_cache(None)
def dis(i,j):
    [x0,y0] = pos[i]
    [x1,y1] = pos[j]
    return sqrt((x0-x1)**2+(y0-y1)**2)
@lru_cache(None)
def findmax(i,num):
    PP = P[num]
    MAX = 0
    for k in PP:
        if i != k:
            MAX = max(MAX,D[i][k])
    return MAX
N = int(data[0])
pos = list(map(split,data[1:1+N]))
G = list(map(list,data[1+N:1+2*N]))
D = [[float('inf')]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if G[i][j] == '1':
            D[i][j] = dis(i,j)
warshall()
selected = []
P = []
for i in range(N):
    if i not in selected:
        res = []
        for j in range(N):
            if D[i][j] != float('inf'):
                res.append(j)
                selected.append(j)
        P.append(res)
for i in range(N):
    for j in range(i+1,N):
        if D[i][j] == float('inf'):
            D[i][j] = D[j][i] = dis(i,j)
MIN = float('inf')
M = len(P)
for num1 in range(M):
    for num2 in range(num1+1,M):
        for i in P[num1]:
            for j in P[num2]:
                MIN = max(diameter(num1),diameter(num2),\
                    min(MIN,D[i][j]+findmax(i,num1)+findmax(j,num2)))
w.write("%.6f\n"%MIN)