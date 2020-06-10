'''
ID: philoin1
LANG: PYTHON3
TASK: ratios
'''
from copy import deepcopy
f = open('ratios.in', 'r')
w = open('ratios.out', 'w')
def split(string):
    return list(map(int,string.split()))
data = f.read().split('\n')
goal = list(map(int,data[0].split()))
matrix = list(map(split,data[1:4]))
for i in range(3):
    for j in range(i+1,3):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
def solve(M,P):
    def swap(a,b):
        M[a],M[b] = M[b],M[a]
        O[a],O[b] = O[b],O[a]
        P[a],P[b] = P[b],P[a]
        return
    def compute(a,b):
        t = M[b][a]/M[a][a]
        for i in range(a,3):
            M[b][i] -= t*M[a][i]
        P[b] -= t*P[a] 
        return
    O = [0,1,2]
    if M[0][0] == 0:
        if M[1][0] != 0:
            swap(0,1)
        else:
            swap(0,2)
    if M[1][0] != 0:
        compute(0,1)
    if M[2][0] != 0:
        compute(0,2)
    if M[1][1] == 0:
        swap(1,2)
    if M[2][1] != 0:
        compute(1,2)
    S = [0,0,0]
    S[2] = P[2]/M[2][2]
    S[1] = (P[1]-S[2]*M[1][2])/M[1][1]
    S[0] = (P[0]-S[2]*M[0][2]-S[1]*M[0][1])/M[0][0]
    S[0],S[1],S[2] = S[O[0]],S[O[1]],S[O[2]]
    if abs(round(S[0]) - S[0]) < 1e-5 and abs(round(S[1]) - S[1]) < 1e-5 and \
        abs(round(S[2]) - S[2]) < 1e-5 and S[0] >= 0 and S[1] >= 0 and S[2] >= 0:
        return list(map(round,S))
    else:
        return None
for i in range(1,200):
    GOAL = [i*j for j in goal]
    M = deepcopy(matrix)
    S = solve(M,GOAL)
    if S is not None:
        w.write("%d %d %d %d\n"%(S[0],S[1],S[2],i))
        exit()
w.write("NONE\n")