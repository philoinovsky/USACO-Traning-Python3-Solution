'''
ID: philoin1
LANG: PYTHON3
TASK: namenum
'''
f = open('namenum.in', 'r')
d = open('dict.txt', 'r')
w = open('namenum.out', 'w')
data = list(map(int, f.read().split('\n')[0]))
dd = d.read().split('\n')
ddd = {
    2: ['A', 'B', 'C'],
    3: ['D', 'E', 'F'],
    4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'],
    6: ['M', 'N', 'O'],
    7: ['P', 'R', 'S'],
    8: ['T', 'U', 'V'],
    9: ['W', 'X', 'Y']
}
def search(string):
    for i in dd:
        if i.startswith(string):
            return True
    return False
s = []
for i in ddd[data[0]]:
    if search(i):
        s.append(i)
for i in range(1,len(data)):
    ss = s.copy()
    s = []
    for k in ss:
        for j in ddd[data[i]]:
            if search(k+j):
                s.append(k+j)
printed = False
for string in s:
    if string in dd:
        w.write("%s\n"%string)
        printed = True
if not printed:
    w.write("%s\n"%"NONE")