'''
ID: philoin1
LANG: PYTHON3
TASK: fence9
'''
f = open('fence9.in', 'r')
w = open('fence9.out', 'w')
[n,m,p] = list(map(int,f.read().split('\n')[0].split()))
def GCD(a,b):
    if b == 0:
        return a
    else:
        return GCD(b,a%b)
def PICK():
    S = p*m//2
    O = GCD(n,m) + GCD(abs(p-n),m) + p
    I = S - O//2 + 1
    return I
w.write("%d\n"%PICK())