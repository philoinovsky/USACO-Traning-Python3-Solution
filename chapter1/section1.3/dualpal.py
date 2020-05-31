'''
ID: philoin1
LANG: PYTHON3
TASK: dualpal
'''
f = open('dualpal.in', 'r')
w = open('dualpal.out', 'w')
[N,S] = list(map(int, f.read().split('\n')[0].split()))
def ispal(num:str):
    cp = list(num)
    cp.reverse()
    return list(num) == cp
def rebase(num:int, B:int):
    res = ''
    while num:
        num, r = divmod(num, B)
        res = str(r) + res
    return res
while(N):
    S += 1
    cnt = 0
    for B in range(2,11):
        sq = rebase(S,B)
        if ispal(sq):
            cnt += 1
    if cnt >= 2:
        N -= 1
        w.write("%d\n"%S)
            