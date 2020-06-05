'''
ID: philoin1
LANG: PYTHON3
TASK: holstein
'''
f = open('holstein.in', 'r')
w = open('holstein.out', 'w')
data = f.read().split('\n')
def split(string):
    return list(map(int,string.split()))
V = int(data[0])
needs = list(map(int,data[1].split()))
G = int(data[2])
scoops = list(map(split,data[3:3+G]))
#brute force
def bin(num):
    cnt = 0
    candidate = [0] * V
    selected = []
    while num:
        if num & 1:
            for i in range(V):
                candidate[i] += scoops[cnt][i]
            selected.append(cnt)
        num = num >> 1
        cnt += 1
    return candidate, selected
SELECTED = []
for i in range(2**G):
    candidate, selected = bin(i)
    if len(selected) < len(SELECTED) or not SELECTED:
        flag = True
        for j in range(V):
            if candidate[j] < needs[j]:
                flag = False
                break
        if flag:
            SELECTED = selected
string = str(len(SELECTED)) + ' '
for i in SELECTED:
    string += str(i+1) + ' '
w.write("%s\n"%string[:-1])