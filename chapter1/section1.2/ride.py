"""
ID: philoin1
LANG: PYTHON3
PROG: ride
"""
f = open('ride.in', 'r')
w = open('ride.out', 'w')
data = (f.read()).split('\n')
l1 = data[0]
l2 = data[1]
r1 = 1
r2 = 1
for i in l1:
    r1 *= (ord(i) - ord('A') + 1 )
for i in l2:
    r2 *= (ord(i) - ord('A') + 1)
res = "GO" if r1%47 == r2%47 else "STAY"
res += '\n'
w.write(res)