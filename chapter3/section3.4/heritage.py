'''
ID: philoin1
LANG: PYTHON3
TASK: heritage
'''
f = open('heritage.in', 'r')
w = open('heritage.out', 'w')
data = f.read().split('\n')
def split(string):
    return list(map(int,string.split()))
IN = data[0]
PRE = data[1]
def POST(IN,PRE):
    if len(IN) < 2:
        return IN
    first = PRE[0]
    idx = IN.index(first)
    return POST(IN[:idx],PRE[1:1+idx]) + POST(IN[1+idx:],PRE[1+idx:]) + first
w.write("%s\n"%(POST(IN,PRE)))