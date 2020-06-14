'''
ID: philoin1
LANG: PYTHON3
TASK: stall4
'''
f = open('stall4.in', 'r')
w = open('stall4.out', 'w')
def split(string):
    return list(map(int,string.split()))
data = f.read().split('\n')
[N,M] = list(map(int,data[0].split()))
G = [[0] * (N+M+2) for _ in range(N+M+2)] #0 souce,1 sink,2~2+N cows,2+N~2+N+M stalls
for i,L in enumerate(list(map(split,data[1:N+1]))):
    for j in L[1:]:
        G[i+2][j+N+1] = 1
        G[0][i+2] = 1
        G[j+N+1][1] = 1
M = M+N+1
maxflow = 0
flow = [0] * (M+1)
pre = [0] * (M+1)
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
EK(0,1)
w.write("%d\n"%maxflow)
