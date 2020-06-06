'''
ID: philoin1
LANG: PYTHON3
TASK: runround
'''
f = open('runround.in', 'r')
w = open('runround.out', 'w')
M = int(f.read().split('\n')[0])
def isrunaround(num):
    num = list(map(int,str(num)))
    if len(set(num)) != len(num):
        return False
    cnt = idx = 0
    visited = [False] * len(num)
    while cnt < len(num):
        idx = (idx + num[idx]) % len(num)
        if visited[idx]:
            break
        else:
            visited[idx] = True
            cnt += 1
    return cnt == len(num) and idx == 0
flag = False
while not flag:
    M += 1
    flag = isrunaround(M)
w.write("%d\n"%M)
