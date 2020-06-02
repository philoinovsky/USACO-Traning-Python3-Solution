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
    if len(lst) % 2 == 1:
        # Handle odd length list
        for i in range(len(lst)):
            for result in all_pairs(lst[:i] + lst[i+1:]):
                yield result
    else:
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
    if idx == len(d[y])-1:
        return None
    else:
        return [d[y][idx+1], y]
def isstuck(pair,start):
    visited = [start]
    while True:
        start = wormhole(start)
        start = walk(start)
        if start in visited:
            return True
        elif start is not None:
            visited.append(start)
        else:
            return False
lst = list(range(len(l)))
pairs = all_pairs(lst)
cnt = 0
for pair in pairs:
    for start in l:
        if isstuck(pair,start):
            cnt += 1
            break
w.write("%d\n"%cnt)