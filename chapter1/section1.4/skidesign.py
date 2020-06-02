'''
ID: philoin1
LANG: PYTHON3
TASK: skidesign
'''
#brute force
f = open('skidesign.in', 'r')
w = open('skidesign.out', 'w')
data = f.read().split('\n')
m = int(data[0])
l = list(map(int,data[1:m+1]))
l.sort(reverse=True)
res = float('inf')
for i in range(l[-1],l[0]-17):
    cur = 0
    for j in l:
        if j < i:
            cur += (i-j)*(i-j)
        elif j > i + 17:
            cur += (j-i-17)*(j-i-17)
    res = min(res,cur)
res = 0 if res == float('inf') else res
w.write("%d\n"%res)