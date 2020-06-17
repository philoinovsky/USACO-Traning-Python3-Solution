'''
ID: philoin1
LANG: PYTHON3
TASK: race3
'''
f = open('race3.in', 'r')
w = open('race3.out', 'w')
def split(string):
    return list(map(int,string.split()[:-1]))
data = f.read().split('\n')
L = list(map(split,data[:-2]))
"""
TODO
"""