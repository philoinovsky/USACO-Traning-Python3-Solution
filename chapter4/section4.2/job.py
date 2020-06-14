'''
ID: philoin1
LANG: PYTHON3
TASK: job
'''
f = open('job.in', 'r')
w = open('job.out', 'w')
data = f.read().split('\n')
[N,M0,M1] = list(map(int,data[0].split()))
i = 1
L = []
while len(L)<M0+M1:
    L.extend(list(map(int,data[i].split())))
    i += 1
A = L[:M0]
B = L[M0:]
time1 = [0]*N
time2 = [0]*N
timea = [0]*M0
timeb = [0]*M1
for i in range(N):
    MIN = float('inf')
    for j in range(M0):
        if timea[j] + A[j] < MIN:
            MIN = timea[j] + A[j]
            k = j
    timea[k] = time1[i] = MIN
w.write("%d "%MIN)
for i in range(N):
    MIN = float('inf')
    for j in range(M1):
        if timeb[j] + B[j] < MIN:
            MIN = timeb[j] + B[j]
            k = j
    timeb[k] = time2[i] = MIN
ans = 0
for i in range(N):
    if time1[i] + time2[N-i-1] > ans:
        ans = time1[i] + time2[N-i-1]
w.write("%d\n"%ans)