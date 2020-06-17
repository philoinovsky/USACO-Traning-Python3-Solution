'''
ID: philoin1
LANG: PYTHON3
TASK: race3
'''
f = open('race3.in', 'r')
w = open('race3.out', 'w')
def split(string):
    return list(map(int,string.split()[:-1]))
data = f.read().split('\n')
L = list(map(split,data[:-2]))
def bfs(i,START,END,group,mode):
    q = [START]
    visited = [False] * len(L)
    visited[i] = visited[START] = True
    if mode == 2:
        group[START] = False
    while q:
        qq, q = q, []
        for j in qq:
            for k in L[j]:
                if mode == 0 and k == END:
                    return False
                elif mode == 2 and group[k]:
                    return False
                if not visited[k]:
                    q.append(k)
                    visited[k] = True
    return True if mode % 2 == 0 else visited
START = 0
unavoid = []
split = []
END = len(L)-1
for i in range(1,len(L)-1):
    if bfs(i,START,END,None,0):
        unavoid.append(i)
for i in unavoid:
    if bfs(i,i,END,bfs(i,START,i,None,1),2):
        split.append(i)
string = str(len(unavoid)) + ' '
for i in unavoid:
    string += str(i) + ' '
string = string[:-1] + '\n' + str(len(split)) + ' '
for i in split: 
    string += str(i) + ' '
string = string[:-1] + '\n'
w.write("%s"%string)