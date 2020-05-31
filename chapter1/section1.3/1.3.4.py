'''
ID: philoin1
LANG: PYTHON3
TASK: palsquare
'''
f = open('palsquare.in', 'r')
w = open('palsquare.out', 'w')
B = int(f.read().split('\n')[0])
def d(num):
    return chr(num + ord('A') - 10)
def ispal(num):
    cp = list(num)
    cp.reverse()
    return list(num) == cp
def rebase(num):
    res = ''
    while num:
        num, r = divmod(num, B)
        if r >= 10:
            res = d(r) + res
        else:
            res = str(r) + res
    return res
for i in range(1,301):
    ii = rebase(i)
    sq = rebase(i*i)
    if ispal(sq):
        w.write("%s %s\n"%(ii,sq))