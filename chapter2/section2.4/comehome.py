'''
ID: philoin1
LANG: PYTHON3
TASK: comehome
'''
from functools import lru_cache
f = open('comehome.in', 'r')
w = open('comehome.out', 'w')
data = f.read().split('\n')
def split(string):
    return string.split()[:3]
def warshall():
    for i in range(N):
        D[i][i] = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
    return
@lru_cache(None)
def I(char):
    if char.isupper():
        return ord(char) - ord('A') + 26
    elif char.islower():
        return ord(char) - ord('a')
M = int(data[0])
N = 52
pos = list(map(split,data[1:1+M]))
D = [[float('inf')]*N for _ in range(N)]
for [i,j,v] in pos:
    if D[I(i)][I(j)] > int(v):
        D[I(i)][I(j)] = D[I(j)][I(i)] = int(v)
warshall()
MIN = float('inf')
res = None
for i in range(26,51):
    if D[i][-1] < MIN:
        MIN = D[i][-1]
        res = chr(i-26+ord('A'))
w.write("%s %d\n"%(res,MIN))