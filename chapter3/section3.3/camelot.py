'''
ID: philoin1
LANG: PYTHON3
TASK: camelot
'''
f = open('camelot.in', 'r')
w = open('camelot.out', 'w')
data = f.read().split('\n')
#TLE 4/20, use C++ instead, O(XYN) ~= 1e6
def split(string):
    return list(map(int,string.split()))
def cal(char):
    return ord(char) - ord('A') + 1
[x,y] = list(map(int,data[0].split()))
s = data[1].split()
K = [cal(s[0]),int(s[1])]
K[0] -= 1
K[1] -= 1
N = []
i = 2
while i < len(data):
    s = data[i].split()
    for j in range(0,len(s),2):
        N.append([cal(s[j]),int(s[j+1])])
    i += 1
if not N:
    w.write("0\n")
    exit()
king = [[float('inf')] * y for _ in range(x)]
KNIGHT = [[[None] * y for _ in range(x)] for _ in range(len(N))]
def knight(sx,sy):
    knight = [[None] * y for _ in range(x)]
    knight[sx][sy] = 0,king[abs(sx-K[0])][abs(sy-K[1])]
    q = [(sx,sy)]
    cnt = 0
    while q:
        qq, q = q, []
        cnt += 1
        for i,j in qq:
            for ii,jj in [(i-2,j-1),(i-2,j+1),(i-1,j-2),(i-1,j+2),(i+1,j-2),(i+1,j+2),(i+2,j-1),(i+2,j+1)]:
                if x > ii and ii >= 0 and y > jj and jj >= 0:
                    if not knight[ii][jj]:
                        distance = king[abs(ii-K[0])][abs(jj-K[1])]
                        if distance < knight[i][j][1]:
                            knight[ii][jj] = cnt, distance
                        else:
                            knight[ii][jj] = cnt, knight[i][j][1]
                        q.append((ii,jj))
                    elif knight[ii][jj][0] == cnt and knight[ii][jj][1] > knight[i][j][1]:
                        knight[ii][jj] = cnt, knight[i][j][1]
    return knight
for i in range(x):
    for j in range(y):
        if i == j or i*j == 0:
            king[i][j] = max(i,j)
        else:
            q = []
            for ii,jj in [(i-1,j),(i,j-1),(i-1,j-1)]:
                if ii >= 0 and jj >= 0:
                    q.append((ii,jj))
            for ii,jj in q:
                king[i][j] = min(king[i][j],king[ii][jj]+1)
for idx in range(len(N)):
    [ii,jj] = N[idx]
    KNIGHT[idx] = knight(ii-1,jj-1)
MIN_ALL = float('inf')
for i in range(x):
    for j in range(y):
        MIN = float('inf')
        SUM = 0
        for idx in range(len(N)):
            SUM += KNIGHT[idx][i][j][0]
            if KNIGHT[idx][i][j][1] < MIN:
                MIN = KNIGHT[idx][i][j][1]
        if SUM+MIN < MIN_ALL:
            MIN_ALL = SUM+MIN
w.write("%d\n"%(MIN_ALL))