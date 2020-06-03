'''
ID: philoin1
LANG: PYTHON3
TASK: sprime
'''
from math import sqrt, floor
from functools import lru_cache
f = open('sprime.in', 'r')
w = open('sprime.out', 'w')
N = int(f.read().split('\n')[0])

def isprime(num):
    if num % 2 == 0:
        return False
    else:
        i = 3
        upb = floor(sqrt(num))
        while i <= upb:
            if num % i == 0:
                return False
            i += 2
        return True

@lru_cache(None)
def sprime(num):
    if num == 1:
        return [2,3,5,7]
    else:
        res = []
        for i in sprime(num-1):
            for j in [1,3,7,9]:
                n = i*10 + j
                if isprime(n):
                    res.append(n)
        return res

l = sprime(N)
l.sort()
for i in l:
    w.write("%d\n"%i)
