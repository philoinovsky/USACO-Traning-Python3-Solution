'''
ID: philoin1
LANG: PYTHON3
TASK: shopping
'''
from functools import lru_cache
f = open('shopping.in', 'r')
w = open('shopping.out', 'w')
data = f.read().split('\n')
def split(string):
    return list(map(int,string.split()))
s = int(data[0])
O = list(map(split,data[1:s+1]))
b = int(data[s+1])
N = list(map(split,data[s+2:s+b+2]))
#multi knapsack
D = dict()
keys = [0 for _ in range(5)]
needs = [0 for _ in range(5)]
offers = []
for i in range(len(N)):
    keys[i] = N[i][0]
    offer = [0 for _ in range(5)] + [N[i][2]]
    offer[i] = 1
    offers.append(offer)
    needs[i] = N[i][1]
    D[N[i][0]] = i
for o in O:
    offer = [0 for _ in range(6)]
    for i in range(1,len(o)-1,2):
        if D.get(o[i]) != None:
            offer[D[o[i]]] = o[i+1]
    offer[-1] = o[-1]
    offers.append(offer)
@lru_cache(None)
def dp(a,b,c,d,e):
    L = [a,b,c,d,e]
    if a+b+c+d+e == 0:
        return 0
    MIN = float('inf')
    for o in offers:
        LL = [a,b,c,d,e]
        for i in range(5):
            LL[i] = LL[i]-o[i] if LL[i]-o[i] > 0 else 0
        if LL != L:
            NEXT = dp(LL[0],LL[1],LL[2],LL[3],LL[4])+o[-1]
            if NEXT < MIN:
                MIN = NEXT
    return MIN
w.write("%d\n"%dp(needs[0],needs[1],needs[2],needs[3],needs[4]))