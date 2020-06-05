'''
ID: philoin1
LANG: PYTHON3
TASK: frac1
'''
from fractions import Fraction
from bisect import bisect_left
f = open('frac1.in', 'r')
w = open('frac1.out', 'w')
N = int(f.read().split('\n')[0])
def divide(n,m):
    ff = Fraction(n,m)
    return ff.numerator, ff.denominator
def generate(n):
    if n == 1:
        return ['0/1','1/1'], [0, 1]
    else:
        strings, values = generate(n-1)
        for i in range(1,n):
            idx = bisect_left(values,i/n)
            if values[idx] == i/n:
                continue
            values.insert(idx, i/n)
            nn, dd = divide(i,n)
            strings.insert(idx, "%s/%s"%(str(nn),str(dd)))
        return strings, values
strings, _ = generate(N)
for s in strings:
    w.write("%s\n"%s)