'''
ID: philoin1
LANG: PYTHON3
TASK: maze1
'''
f = open('maze1.in', 'r')
w = open('maze1.out', 'w')
data = f.read().split('\n')
[W, H] = list(map(int,data[0].split()))
G = list(map(list,data[1:2*H+2]))
doors = []
def traverse(door):
    q = [door]
    cnt = 1
    while q:
        qq, q = q, []
        for [x,y] in qq:
            if dp[x][y] > cnt:
                dp[x][y] = cnt
                if x > 0 and G[2*x][2*y+1] == ' ':
                    q.append([x-1,y])
                if x < H-1 and G[2*x+2][2*y+1] == ' ':
                    q.append([x+1,y])
                if y > 0 and G[2*x+1][2*y] == ' ':
                    q.append([x,y-1])
                if y < W-1 and G[2*x+1][2*y+2] == ' ':
                    q.append([x,y+1])
        cnt += 1
for j in range(W):
    if G[0][2*j+1] == ' ':
        doors.append([0,j])
    if G[2*H][2*j+1] == ' ':
        doors.append([H-1,j])
for i in range(H):
    if G[2*i+1][0] == ' ':
        doors.append([i,0])
    if G[2*i+1][2*W] == ' ':
        doors.append([i,W-1])
dp = [[float('inf')] * W for _ in range(H)]
traverse(doors[0])
traverse(doors[1])
MAX = float('-inf')
for i in range(H):
    for j in range(W):
        MAX = max(MAX,dp[i][j])
w.write("%d\n"%MAX)
