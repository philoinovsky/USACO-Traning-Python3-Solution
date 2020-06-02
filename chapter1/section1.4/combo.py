'''
ID: philoin1
LANG: PYTHON3
TASK: combo
'''
#O(n)
f = open('combo.in', 'r')
w = open('combo.out', 'w')
data = f.read().split('\n')
m = int(data[0])
l1 = list(map(int,data[1].split()))
l2 = list(map(int,data[2].split()))
res = 1
def overlap(n1,n2):
    diff = max(n1-n2, n2-n1)
    dist = min(m-diff,diff)
    return max(min(m,5-dist),0)
for i in range(3):
    res *= overlap(l1[i],l2[i])
res = 2*min(m,5)**3 - res
w.write("%d\n"%res)