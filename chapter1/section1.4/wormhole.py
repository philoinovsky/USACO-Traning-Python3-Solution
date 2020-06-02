'''
ID: philoin1
LANG: PYTHON3
TASK: wormhole
'''
f = open('wormhole.in', 'r')
w = open('wormhole.out', 'w')
data = f.read().split('\n')
m = int(data[0])
def split(string):
    return list(map(int,string.split()))
l = list(map(split,data[1:1+m]))
l.sort(key=lambda t:t[0]) #sort by x
d = dict()
for i in l:
    if d.get(i[1]):
        d[i[1]].append(i[0])
    else:
        d[i[1]] = [i[0]]
def all_pairs(lst):
    if len(lst) < 2:
        yield []
        return
    a = lst[0]
    for i in range(1,len(lst)):
        pair = [a,lst[i]]
        for rest in all_pairs(lst[1:i]+lst[i+1:]):
            yield [pair] + rest
def wormhole(start):
    idx = l.index(start)
    for i in pair:
        if idx in i:
            return l[i[0]] if idx == i[1] else l[i[1]]
def walk(start):
    [x, y] = start
    idx = d[y].index(x)
    return None if idx == len(d[y])-1 else [d[y][idx+1], y]
def isstuck(pair,start):
    visited = [start]
    while True:
        start = wormhole(start)
        start = walk(start)
        if start is not None and start not in visited:
            visited.append(start)
        else:
            return False if start is None else True
cnt = 0
for pair in all_pairs(list(range(m))):
    for start in l:
        if isstuck(pair,start):
            cnt += 1
            break
w.write("%d\n"%cnt)