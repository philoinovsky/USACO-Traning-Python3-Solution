'''
ID: philoin1
LANG: PYTHON3
TASK: kimbits
'''
f = open('kimbits.in', 'r')
w = open('kimbits.out', 'w')
[N,L,I] = list(map(int,f.read().split('\n')[0].split()))
def dp(N,L,I):
    if N == L:
        rest = max(I-2**N,0)
        return rest, I-1
    rest, value = dp(N-1,L,I)
    if rest == 0:
        return 0, value
    if L > 0:
        rest, value = dp(N-1,L-1,rest)
        return rest, 2**(N-1) + value
    return rest, value
rest, value = dp(N,L,I)
string = '{0:0' + str(N) + 'b}'
w.write("%s\n"%string.format(value))
