"""
ID: philoin1
LANG: PYTHON3
PROG: gift1
"""
f = open('gift1.in', 'r')
w = open('gift1.out', 'w')
data = iter(f.read().split('\n'))
d = dict()
tot = int(next(data))
for _ in range(tot):
    d[next(data)] = 0
for _ in range(tot):
    cur = next(data)
    [amount, num] = map(int,next(data).split())
    if num == 0:
        continue
    q, r = divmod(amount, num)
    d[cur] += r - amount
    for _ in range(num):
        d[next(data)] += q

for name in d.keys():
    w.write("%s %s\n"%(name,d[name]))