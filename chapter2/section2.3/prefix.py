'''
ID: philoin1
LANG: PYTHON3
TASK: prefix
'''
f = open('prefix.in', 'r')
w = open('prefix.out', 'w')
data = f.read().split('\n')
S = []
seq = ''
mode = 0
for i in data:
    if i == '.':
        mode = 1
        continue
    if mode == 0:
        S.extend(i.split())
    else:
        seq += i
dp = [True] + [False]*len(seq)
maxlen = max(S,key=lambda t:t.__len__()).__len__()
last = 0
for i in range(1,len(seq)+1):
    if last + maxlen < i:
        break
    for s in S:
        if i-len(s) >= 0 and dp[i-len(s)] and seq[i-len(s):i] == s:
            dp[i] = True
            last = i
            break
w.write("%d\n"%last)