'''
ID: philoin1
LANG: PYTHON3
TASK: fact4
'''
f = open('fact4.in', 'r')
w = open('fact4.out', 'w')
N = int(f.read().split('\n')[0])
res = 1
for i in range(2,N+1):
    res *= i
w.write("%s\n"%str(res).rstrip('0')[-1])