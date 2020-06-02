'''
ID: philoin1
LANG: PYTHON3
TASK: ariprog
'''
f = open('ariprog.in', 'r')
w = open('ariprog.out', 'w')
[N, M] = list(map(int, f.read().split('\n')[:2]))
if N > 22:
    w.write("NONE\n")
    exit()
elif N > 14:
    min_frac = 84
elif N > 7:
    min_frac = 12
else:
    min_frac = 1
arrlen = 2 * M * M + 1
t = [False] * arrlen
l = []
for i in range(M+1):
    for j in range(i,M+1):
        if not t[i*i+j*j]:
            l.append(i*i+j*j)
        t[i*i+j*j] = True
l.sort()
res = []
for c in range(len(l)-1):
    i = l[c]
    j = l[c+1] - i
    while i + (N - 1) * j < arrlen:
        if N > 7 and j % min_frac != 0:
            c += 1
            j = l[c+1] - i
            continue
        flag = True
        for k in range(N):
            if t[i+j*k] == False:
                flag = False
                break
        if flag:
            res.append([i,j])
        c += 1
        j = l[c+1] - i
res.sort(key=lambda t:t[1])
if res:
    for [i,j] in res:
        w.write("%d %d\n"%(i,j))
else:
    w.write("NONE\n")