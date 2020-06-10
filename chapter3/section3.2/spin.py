'''
ID: philoin1
LANG: PYTHON3
TASK: spin
'''
f = open('spin.in', 'r')
w = open('spin.out', 'w')
data = f.read().split('\n')
R = [0] * 5
SRT = [[] for _ in range(5)]
RNG = [[] for _ in range(5)]
for i in range(5):
    ITER = iter(data[i].split())
    R[i] = int(next(ITER))
    num = int(next(ITER))
    for _ in range(num):
        SRT[i].append(int(next(ITER)))
        RNG[i].append(int(next(ITER)))
def UNION(ALL):
    ALL.sort(key=lambda t:t[0])
    last = -1
    res = [ALL[0]]
    for [start, end] in ALL[1:]:
        if start < res[-1][-1]:
            res[-1][-1] = min(end,res[-1][-1])
        else:
            res.append([start,end])
    return res
def INTERSECT(A,B):
    res = []
    i = j = 0
    while i < len(A) and j < len(B):
        small = [1,0] if A[i][1] < B[j][1] else [0,1]
        tmp = [max(A[i][0],B[j][0]),min(A[i][1],B[j][1])]
        if tmp[1] > tmp[0]:
            res.append(tmp)
        i += small[0]
        j += small[1]
    return res, bool(res)
def isvalid():
    RANGE = [[0,360+1]]
    for i in range(5):
        SELF = []
        for j in range(len(SRT[i])):
            START = SRT[i][j]
            END = SRT[i][j] + RNG[i][j]
            if END >= 360:
                END %= 360
                SELF.append([0,END+1])
                SELF.append([START,361])
            else:
                SELF.append([START,END+1])
        SELF = UNION(SELF)
        RANGE, res = INTERSECT(RANGE,SELF)
        if not res:
            return False
    return True
cnt = 0
while True:
    if isvalid():
        break
    else:
        cnt += 1
        if cnt == 360:
            break
        for i in range(5):
            for j in range(len(SRT[i])):
                SRT[i][j] += R[i]
                SRT[i][j] %= 360
if cnt != 360:
    w.write("%d\n"%cnt)
else:
    w.write("none\n")
    