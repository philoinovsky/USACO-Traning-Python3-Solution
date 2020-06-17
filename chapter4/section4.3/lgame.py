'''
ID: philoin1
LANG: PYTHON3
TASK: lgame
'''
from collections import namedtuple
f = open('lgame.in', 'r')
d = open('lgame.dict', 'r').read().split('\n')[:-2]
w = open('lgame.out', 'w')
W = f.read().split('\n')[0]
D = dict()
item = namedtuple("item",['score','counter'])
scores = {
    'q':7,'w':6,'e':1,'r':2,'t':2,'y':5,'u':4,'i':1,'o':3,'p':5,
    'a':2,'s':1,'d':4,'f':6,'g':5,'h':5,'j':7,'k':6,'l':3,
    'z':7,'x':7,'c':4,'v':6,'b':5,'n':2,'m':5
}
for i in d:
    score = 0
    counter = dict()
    for j in i:
        score += scores[j]
        if counter.get(j):
            counter[j] += 1
        else:
            counter[j] = 1
    D[i] = item(score,counter)
def verify(i,CC):
    flag = True
    for char in D[d[i]].counter:
        if CC.get(char) and CC[char] >= D[d[i]].counter[char]:
            CC[char] -= D[d[i]].counter[char]
        else:
            flag = False
            break
    if flag:
        return D[d[i]].score, CC
    else:
        return 0, None
LIM = 0
counter = dict()
for j in W:
    if counter.get(j):
        counter[j] += 1
    else:
        counter[j] = 1
    LIM += scores[j]
MAX = 0
LIST = []
for i in range(len(d)):
    value, newcounter = verify(i,counter.copy())
    if value > 0:
        if value > MAX:
            MAX = value
            LIST = [[d[i]]]
        elif value == MAX:
            LIST.append([d[i]])
        if value < LIM:
            for j in range(i+1,len(d)):
                value1, _ = verify(j,newcounter.copy())
                if value1 > 0:
                    if value + value1> MAX:
                        MAX = value + value1
                        LIST = [[d[i],d[j]]]
                    elif value + value1 == MAX:
                        LIST.append([d[i],d[j]])
w.write("%d\n"%MAX)
for j in LIST:
    if len(j) == 1:
        w.write("%s\n"%j[0])
    if len(j) == 2:
        w.write("%s %s\n"%(j[0],j[1]))