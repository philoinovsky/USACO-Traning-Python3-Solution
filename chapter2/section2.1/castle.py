'''
ID: philoin1
LANG: PYTHON3
TASK: castle
'''
from collections import namedtuple
f = open('castle.in', 'r')
w = open('castle.out', 'w')
data = f.read().split('\n')
def split(string):
    return list(map(int,string.split()))
[N, M] = list(map(int,data[0].split()))
nums = list(map(split,data[1:M+1]))
class room:
    def __init__(self):
        self.size = 0
        self.blocks = []
block = namedtuple("block",['x','y'])
rooms = []
visited = [[False] * N for _ in range(M)]
room_tb = [[None] * N for _ in range(M)]
t = [[8,1,0],[4,0,1],[2,-1,0],[1,0,-1]]
def visit(i,j,r):
    if not visited[i][j]:
        visited[i][j] = True
        if not r:
            r = room()
            rooms.append(r)
        r.size += 1
        r.blocks.append(block(i,j))
        room_tb[i][j] = rooms.index(r)
        rr = nums[i][j]
        for ii in range(4):
            q, rr = divmod(rr,t[ii][0])
            if q == 0:
                visit(i+t[ii][1],j+t[ii][2],r)
for i in range(M):
    for j in range(N):
        visit(i,j,None) #initialization
MAX = 0 #westest and southest
WALL = None
def compare(this,which,dir,MAX,WALL):
    if this != which:
        if rooms[this].size + rooms[which].size >= MAX:
            MAX = rooms[this].size + rooms[which].size
            WALL = [i,j,dir]
    return MAX, WALL
for j in range(N-1,-1,-1):
    for i in range(M): #compare to east and north only
        this = room_tb[i][j]
        if j != N-1:
            east = room_tb[i][j+1]
            MAX, WALL = compare(this,east,'E',MAX,WALL)
        if i != 0:
            north = room_tb[i-1][j]
            MAX, WALL = compare(this,north,'N',MAX,WALL)
w.write("%d\n"%len(rooms))
w.write("%d\n"%max(rooms,key=lambda t:t.size).size)
w.write("%d\n"%MAX)
w.write("%d %d %s\n"%(WALL[0]+1,WALL[1]+1,WALL[2]))