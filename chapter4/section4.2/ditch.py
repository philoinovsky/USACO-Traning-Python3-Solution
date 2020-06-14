'''
ID: philoin1
LANG: PYTHON3
TASK: ditch
'''
f = open('ditch.in', 'r')
w = open('ditch.out', 'w')
def split(string):
    return list(map(int,string.split()))
data = f.read().split('\n')
[N,M] = list(map(int,data[0].split()))
maxflow = 0
G = [[0] * (M+1) for _ in range(M+1)]
flow = [0] * (M+1)
pre = [0] * (M+1)
for [S,E,C] in list(map(split,data[1:N+1])):
    G[S][E] += C #in case multiple edges between 2 nodes
def bfs(s,t):
    global pre,flow,G
    q = [s]
    pre = [-1] * (M+1)
    pre[s] = 0
    flow[s] = float('inf')
    while q:
        x = q.pop()
        if x == t:
            break
        for i in range(1,M+1):
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
EK(1,M)
w.write("%d\n"%maxflow)