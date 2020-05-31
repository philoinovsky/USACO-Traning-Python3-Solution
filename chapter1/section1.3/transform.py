'''
ID: philoin1
LANG: PYTHON3
TASK: transform
'''
from copy import deepcopy
f = open('transform.in', 'r')
w = open('transform.out', 'w')
data = f.read().split('\n')
m = int(data[0])
a = list(map(list,data[1:1+m]))
b = list(map(list,data[1+m:1+2*m]))
def rot(A):
    B = [[None] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            B[j][m-i-1] = A[i][j]
    return B
def hrz(A):
    B = deepcopy(A)
    [i.reverse() for i in B]
    return B
if rot(a) == b:
    res = 1
elif rot(rot(a)) == b:
    res = 2
elif rot(rot(rot(a))) == b:
    res = 3
elif hrz(a) == b:
    res = 4
elif rot(hrz(a)) == b or rot(rot(hrz(a))) == b or rot(rot(rot(hrz(a)))) == b:
    res = 5
elif a == b:
    res = 6
else:
    res = 7
w.write("%d\n"%res)