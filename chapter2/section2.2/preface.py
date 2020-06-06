'''
ID: philoin1
LANG: PYTHON3
TASK: preface
'''
f = open('preface.in', 'r')
w = open('preface.out', 'w')
N = int(f.read().split('\n')[0])
def add(q,Collection):
    cnt = 0
    while q:
        q, r = divmod(q,10)
        [f,s,t] = seq[cnt]
        Collection[f] += lookup[r][0]
        Collection[s] += lookup[r][1]
        Collection[t] += lookup[r][2]
        cnt += 1
    return
seq = [
    ['I','V','X'], ['X','L','C'],
    ['C','D','M'], ['M','M','M']
]
lookup = [
    [0,0,0], [1,0,0], [2,0,0],
    [3,0,0], [1,1,0], [0,1,0],
    [1,1,0], [2,1,0], [3,1,0],
    [1,0,1]
]
Collection = { 'I': 0, 'V': 0, 'X': 0, 'L': 0, 'C': 0, 'D': 0, 'M': 0 }
for i in range(1,N+1):
    add(i,Collection)
for i in Collection:
    if Collection[i] != 0:
        w.write('%s %d\n'%(i,Collection[i]))