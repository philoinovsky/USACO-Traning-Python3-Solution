'''
ID: philoin1
LANG: PYTHON3
TASK: milk3
'''
from collections import deque
f = open('milk3.in', 'r')
w = open('milk3.out', 'w')
MAX = [A_MAX, B_MAX, C_MAX] = list(map(int, f.read().split('\n')[0].split()))
states = set([str([0,0,C_MAX])])
res = set([C_MAX])
q = deque([[0,0,C_MAX]])
def pourto(s, f, t):
    minn = min(s[f], MAX[t] - s[t])
    s[t] += minn
    s[f] -= minn
    return s
while q:
    s = q.popleft()
    for [f,t] in [[0,1],[0,2],[1,0],[1,2],[2,0],[2,1]]:
        after = pourto(s.copy(),f,t)
        if str(after) not in states:
            q.append(after)
            states.add(str(after))
            if after[0] == 0:
                res.add(after[2])

res = list(res)
res.sort()
string = ''
for i in res:
    string += str(i) + " "
w.write("%s\n"%string[:-1])