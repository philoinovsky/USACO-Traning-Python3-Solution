'''
ID: philoin1
LANG: PYTHON3
TASK: ttwo
'''
f = open('ttwo.in', 'r')
w = open('ttwo.out', 'w')
data = f.read().split('\n')
G = list(map(list,data[:10]))
D = [[-1,0],[0,1],[1,0],[0,-1]]
def getnext(E):
    E_next = [E[0]+D[E[2]][0], E[1]+D[E[2]][1],E[2]]
    if not 0 <= E_next[0] < 10 or not 0 <= E_next[1] < 10 \
        or G[E_next[0]][E_next[1]] == "*":
        E[2] += 1
        E[2] %= 4
        return E
    else:
        return E_next
for i in range(10):
    for j in range(10):
        if G[i][j] == 'F':
            F = [i,j]
        elif G[i][j] == 'C':
            C = [i,j]
F.append(0)
C.append(0)
cnt = 0
while (F[0] != C[0] or F[1] != C[1]) and cnt < 160000:
    F = getnext(F)
    C = getnext(C)
    cnt += 1
if cnt >= 160000:
    w.write("0\n")
else:
    w.write("%d\n"%cnt)