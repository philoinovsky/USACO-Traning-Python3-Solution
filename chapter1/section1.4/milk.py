'''
ID: philoin1
LANG: PYTHON3
TASK: milk
'''
#O(nlogn)
f = open('milk.in', 'r')
w = open('milk.out', 'w')
data = f.read().split('\n')
def split(string):
    return list(map(int,string.split()))
data = list(map(split,data[:-1]))
[N, M] = data[0]
data.pop(0)
data.sort(key=lambda t:t[0])
pay = 0
i = iter(data)
while N:
    [price, quantity] = next(i)
    pay += min(N, quantity) * price
    N -= min(N, quantity)
w.write("%d\n"%pay)