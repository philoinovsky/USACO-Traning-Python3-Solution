'''
ID: philoin1
LANG: PYTHON3
TASK: milk6
'''
f = open('milk6.in', 'r')
w = open('milk6.out', 'w')
#WIP
data = f.read().split('\n')
[N,M] = list(map(int,data[0].split()))
V = [0] * (M+1)
skip = [False] * (N+1)
G = [[0] * (N+1) for _ in range(N+1)]
for i in range(1,1+M):
    [S,E,C] =  list(map(int,data[i].split()))
    G[S][E] += C*1001 + 1
    V[i] += C*1001 + 1
def init():
    global pre,flow,maxflow
    pre = [0] * (N+1)
    flow = [0] * (N+1)
    maxflow = 0
def bfs(s,t):
    global flow,pre,G
    q = [s]
    pre = [-1] * (N+1)
    flow[s] = float('inf')
    while q:
        x = q.pop()
        if x == t:
            break
        elif skip[x]:
            continue
        for i in range(1,N+1):
            if G[x][i] > 0 and pre[i] == -1:
                pre[i] = x
                flow[i] = min(flow[x],G[x][i])
                q.append(i)
    return -1 if pre[t] == -1 else flow[t]
def EK(s,t):
    global maxflow,G
    increase = bfs(s,t)
    while increase != -1:
        k = t
        while k != s:
            last = pre[k]
            G[last][k] -= increase
            G[k][last] += increase
            k = last
        maxflow += increase
        increase = bfs(s,t)
    return maxflow
init()
MAXFLOW = EK(1,N)
M0 = MAXFLOW//1001
M2 = MAXFLOW%1001
w.write("%d %d\n"%(M0,M2))
res = []
for i in range(2,M):
    if M2 <= 0:
        break
    init()
    if i == 3:
        fuck = 1
    skip[i] = True
    if EK(1,N) + V[i] == MAXFLOW:
        M2 -= 1
        res.append(i)
    skip[i] = False
string = ''
for i in res:
    string += str(i) + ' '
if string:
    string = string[:-1] + '\n'
w.write("%s"%string)