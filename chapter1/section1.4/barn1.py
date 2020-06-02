'''
ID: philoin1
LANG: PYTHON3
TASK: barn1
'''
#O(nlogn)
f = open('barn1.in', 'r')
w = open('barn1.out', 'w')
data = f.read().split('\n')
[M, S, C] = list(map(int,data[0].split()))
l = list(map(int,data[1:C+1]))
l.sort()
if M >= C:
    w.write("%d\n"%C)
    exit()
diff = []
for i in range(C-1):
    diff.append(l[i+1]-l[i]-1)
diff.sort(reverse=True)
tot = l[-1] - l[0] + 1
for i in range(M-1):
    tot -= diff[i]
w.write("%d\n"%tot)