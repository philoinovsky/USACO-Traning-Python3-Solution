'''
ID: philoin1
LANG: PYTHON3
TASK: fracdec
'''
from math import floor
f = open('fracdec.in', 'r') 
w = open('fracdec.out', 'w')
data = f.read().split('\n')
[D, N] = list(map(int,data[0].split()))
TMP = ("%.15f"%(D/N)).rstrip("0")
if TMP[-1] == '.':
    TMP += '0'
if len(TMP) < 15:
    w.write("%s\n"%TMP)
    exit()
DD = D
STR = ""
for i in range(50000): #500000 digits
    DD %= N
    STR += ("%.15f"%(DD/N))[2:12]
    DD *= 1e10
INT = D//N
w.write("%d."%INT)
cnt = len(str(INT)) + 1
def isvalid(start,length):
    flag = True
    for _ in range(4): #validate 5 times
        if STR[start:start+length] != STR[start+length:start+2*length]:
            flag = False
            break
        else:
            start += length
    return flag
def write(s,cnt):
    for i in s:
        w.write(i)
        cnt += 1
        if cnt % 76 == 0:
            w.write("\n")
    return cnt
for start in range(0,100):
    flag = False
    for length in range(1,50000):
        if isvalid(start,length):
            flag = True
            cnt = write("("+STR[start:start+length]+")",cnt)
            break
    if not flag:
        cnt = write(STR[start],cnt)
    else:
        break
w.write("\n")