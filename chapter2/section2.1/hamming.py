'''
ID: philoin1
LANG: PYTHON3
TASK: hamming
'''
f = open('hamming.in', 'r')
w = open('hamming.out', 'w')
[N,B,D] = list(map(int,f.read().split('\n')[0].split()))
def hammingDistance(x, y):
    ans = 0
    for i in range(8,-1,-1):
        b1 = x>>i & 1
        b2 = y>>i & 1
        ans+= not(b1==b2)
    return ans
res = []
for i in range(2**B):
    if N <= 0:
        break
    flag = True
    for j in res:
        if hammingDistance(i, j) < D:
            flag = False
    if flag:
        N -= 1
        res.append(i)
cnt = 0
for i in res:
    if cnt % 10 == 9 or cnt == len(res)-1:
        w.write("%d\n"%i)
    else:
        w.write("%d "%i)
    cnt += 1