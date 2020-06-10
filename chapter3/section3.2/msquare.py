'''
ID: philoin1
LANG: PYTHON3
TASK: msquare
'''
from collections import deque
f = open('msquare.in', 'r')
w = open('msquare.out', 'w')
L = list(map(int,f.read().split('\n')[0].split()))
def A(L):
    L[-1] += "A"
    for i in range(4):
        L[i],L[7-i] = L[7-i],L[i]
    return L
def B(L):
    L[-1] += "B"
    L[0],L[1],L[2],L[3] = L[3],L[0],L[1],L[2]
    L[4],L[5],L[6],L[7] = L[5],L[6],L[7],L[4]
    return L
def C(L):
    L[-1] += "C"
    L[1],L[2],L[5],L[6] = L[6],L[1],L[2],L[5]
    return L
def valid(T):
    for i in range(8):
        if L[i] != T[i]:
            return False
    return True
q = deque()
q.append([1,2,3,4,5,6,7,8,''])
d = dict()
while True:
    l = q.popleft()
    if valid(l):
        w.write("%d\n%s\n"%(len(l[-1]),l[-1]))
        exit()
    for i in [A(l.copy()),B(l.copy()),C(l.copy())]:
        if str(i[:8]) not in d:
            d[str(i[:8])] = True
            q.append(i)
