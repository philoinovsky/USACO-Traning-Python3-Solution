'''
ID: philoin1
LANG: PYTHON3
TASK: pprime
'''
from functools import lru_cache
f = open('pprime.in', 'r')
w = open('pprime.out', 'w')
[a, b] = list(map(int, f.read().split('\n')[0].split()))
d = list(range(1,10))

def wrap(num):
    return [str(i)+num+str(i) for i in range(10)]
@lru_cache(None)
def generate(digits):
    if digits == 1:
        return list(map(str,range(0,10)))
    elif digits == 2:
        return list(map(str,[00,11,22,33,44,55,66,77,88,99]))
    else:
        res = []
        for i in generate(digits-2):
            res.extend(wrap(i))
        return res
def isprime(num):
    if num % 2 == 0:
        return False
    i = 3
    while i*i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

total = set()
da = len(str(a))
db = len(str(b))
for i in range(da,db+1):
    for j in generate(i):
        j = int(j)
        if a <= j <= b:
            total.add(j)
total = list(total)
total.sort()
for i in total:
    if isprime(i):
        w.write("%d\n"%i)