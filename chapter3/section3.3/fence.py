'''
ID: philoin1
LANG: PYTHON3
TASK: fence
'''
import sys
sys.setrecursionlimit(1500)
f = open('fence.in', 'r')
w = open('fence.out', 'w')
data = f.read().split('\n')
def split(string):
    return list(map(int,string.split()))
N = 500
F = int(data[0])
L = list(map(split,data[1:F+1]))
G = [[] for _ in range(N+1)]
T = [[0] * (N+1) for _ in range(N+1)]
D = dict()
#O(E + V)
def find_circuit(idx):
    if G[idx][-1] == len(G[idx])-1:
        circuit.append(idx)
    else:
        while G[idx][-1] != len(G[idx])-1:
            for dst in G[idx][:-1]:
                if T[idx][dst]:
                    T[idx][dst] -= 1
                    T[dst][idx] -= 1
                    G[idx][-1] += 1
                    G[dst][-1] += 1
                    find_circuit(dst)
        circuit.append(idx)
for [i,j] in L:
    G[i].append(j)
    G[j].append(i)
    T[i][j] += 1
    T[j][i] += 1
for l in G:
    l.sort()
selected = -1
for i in range(1,len(G)):
    G[i].append(0) #index
    if len(G[i]) % 2 == 0 and selected == -1:
        selected = i
selected = 1 if selected == -1 else selected
circuit = []
find_circuit(selected)
for i in circuit[::-1]:
    w.write("%d\n"%i)