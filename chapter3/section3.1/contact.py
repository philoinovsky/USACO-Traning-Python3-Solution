'''
ID: philoin1
LANG: PYTHON3
TASK: contact
'''
f = open('contact.in', 'r')
w = open('contact.out', 'w')
data = f.read().split('\n')
[A,B,N] = list(map(int,data[0].split()))
STR = ''
for string in data[1:]:
    STR += string
#brute force
D = dict()
for length in range(A,B+1):
    for start in range(len(STR)-length+1):
        if D.get(STR[start:start+length]):
            D[STR[start:start+length]] += 1
        else:
            D[STR[start:start+length]] = 1
L = list(D.items())
L.sort(key=lambda t:(-t[1],len(t[0]),t[0]))
last = 0
cnt = 0
for i in range(len(L)):
    if L[i][1] != last:
        if last != 0:
            w.write("\n")
        if cnt >= N:
            exit()
        w.write("%d\n%s"%(L[i][1],L[i][0]))
        cnt += 1
        last = L[i][1]
        perline = 1
    else:
        if perline == 0:
            w.write("\n%s"%L[i][0])
        else:
            w.write(" %s"%L[i][0])
        perline += 1
        if perline == 6:
            perline = 0
w.write("\n")
