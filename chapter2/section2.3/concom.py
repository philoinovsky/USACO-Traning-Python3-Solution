'''
ID: philoin1
LANG: PYTHON3
TASK: concom
'''
f = open('concom.in', 'r')
w = open('concom.out', 'w')
data = f.read().split('\n')
def split(string):
    return list(map(int,string.split()))
N = int(data[0])
L = list(map(split,data[1:1+N]))
d = dict()
ds = dict()
#BFS with memory
table = [[False]*101 for _ in range(102)]
for [i,j,p] in L:
    if d.get(i):
        if d[i].get(j):
            d[i][j] += p
        else:
            d[i][j] = p
    else:
        d[i] = {j: p}
    if d[i][j] >= 50:
        if ds.get(i):
            ds[i].add(j)
        else:
            ds[i] = set([j])
for i in ds:
    q = list(ds[i])
    while q:
        qq, q = q, []
        for j in qq:
            if table[i][j]:
                continue
            table[i][j] = True
            if ds.get(j):
                q.extend(ds[j])
                ds[i] |= ds[j]
            if d.get(j):
                for l in d[j]:
                    if not d[i].get(l):
                        d[i][l] = 0
                    d[i][l] += d[j][l]
                    if d[i][l] >= 50 and l not in ds[i]:
                        ds[i].add(l)
                        q.append(l)
for i in sorted(ds.keys()):
    for j in sorted(list(ds[i])):
        if i == j:
            continue
        w.write("%d %d\n"%(i,j))