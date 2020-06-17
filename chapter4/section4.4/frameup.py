'''
ID: philoin1
LANG: PYTHON3
TASK: frameup
'''
f = open('frameup.in', 'r')
w = open('frameup.out', 'w')
data = f.read().split('\n')
[H,W] = list(map(int,data[0].split()))
G = list(map(list,data[1:1+H]))
