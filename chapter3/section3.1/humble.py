'''
ID: philoin1
LANG: PYTHON3
TASK: humble
'''
# time O(KNlog(N)), still TLE (faster than official sln) space O(N)
# (official solution O(KN) in cpp)
from heapq import *
f = open('humble.in', 'r')
w = open('humble.out', 'w')
data = f.read().split('\n')
[K,N] = list(map(int,data[0].split()))
L = list(map(int,data[1].split()[:K]))
H = [(v,k) for k,v in list(enumerate(L))]
heapify(H)
MAX = 0
ID = 0
while ID < N:
    MIN, k = heappop(H)
    for i in range(k,K):
        res = MIN*L[i]
        if len(H) < N - ID:
            if res > MAX:
                MAX = res
            heappush(H,(res,i))
        elif res < MAX:
            heappush(H,(res,i))
    ID += 1
w.write("%d\n"%MIN)

# official sln in py
# f = open('humble.in', 'r')
# w = open('humble.out', 'w')
# data = f.read().split('\n')
# [K,N] = list(map(int,data[0].split()))
# L = list(map(int,data[1].split()[:K]))
# hum = [1]+[0]*N
# IDX = [0] * K
# ID = 0
# while ID < N:
#     MIN = float('inf')
#     for i in range(K):
#         while L[i] * hum[IDX[i]] <= hum[ID]:
#             IDX[i] += 1
#         if L[i] * hum[IDX[i]] < MIN:
#             MIN = L[i] * hum[IDX[i]]
#     ID += 1
#     hum[ID] = MIN
# w.write("%d\n"%hum[ID])