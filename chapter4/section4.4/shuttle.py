'''
ID: philoin1
LANG: PYTHON3
TASK: shuttle
'''
f = open('shuttle.in', 'r')
w = open('shuttle.out', 'w')
N = int(f.read().split('\n')[0])
b = [0] * (N+1)**2
l = 2
r = 1
while r < N:
    for i in range(1,r+1):
        b[0] += 1
        b[b[0]] = l
        b[N*(N+2)-b[0]-1] = b[b[0]]
    b[0] += 1
    b[b[0]] = l//2
    b[N*(N+2)-b[0]-1] = b[b[0]]
    l = -l
    r += 1
for i in range(1,r+1):
    b[0] += 1
    b[b[0]] = l
b[N*(N+2)-1] = -1
l = N
string = ''
for i in range(1,N*(N+2)+1):
    string += str(l) + ' '
    l += b[i]
    if i % 20 == 0:
        string = string[:-1] + '\n'
if string[-1] == ' ':
    string = string[:-1]
if string[-1] != '\n':
    string = string + '\n'
w.write("%s"%string)