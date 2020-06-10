'''
ID: philoin1
LANG: PYTHON3
TASK: agrinet
'''
f = open('agrinet.in', 'r')
w = open('agrinet.out', 'w')
data = f.read().split('\n')
ITER = iter(data)
N = int(next(ITER))
G = []
for _ in range(N):
    res = []
    while len(res) < N:
        res += list(map(int,next(ITER).split()))
    G.append(res)
#O(N^2)
def prim():
    SUM = 0
    D = G[0] #Distance
    I = [True] + [False]*(N-1) #Intree
    for _ in range(N-1):
        MIN = float('inf')
        ID = -1
        for i in range(N):
            if I[i] == False and D[i] < MIN:
                MIN, ID = D[i], i
        I[ID] = True
        SUM += MIN
        for j in range(N):
            if I[j] == False and G[ID][j] < D[j]:
                D[j] = G[ID][j]
    return SUM
SUM = prim()
w.write("%d\n"%SUM)