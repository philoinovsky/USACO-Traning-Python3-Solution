'''
ID: philoin1
LANG: PYTHON3
TASK: zerosum
'''
f = open('zerosum.in', 'r')
w = open('zerosum.out', 'w')
N = int(f.read().split('\n')[0])
d = ['+','-',' ']
res = []
for i in range(3**(N-1)):
    q = i
    l = [1]
    string = '1'
    for j in range(2,N+1):
        q, r = divmod(q, 3)
        if r == 0:
            l.append(j)
        elif r == 1:
            l.append(-j)
        else:
            l[-1] = 10*l[-1]+j if l[-1] > 0 else 10*l[-1]-j
        string += d[r] + str(j)
    if sum(l) == 0:
        res.append(string)
res.sort()
for i in res:
    w.write("%s\n"%i)