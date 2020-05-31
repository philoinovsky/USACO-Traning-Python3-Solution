'''
ID: philoin1
LANG: PYTHON3
TASK: milk2
'''
f = open('milk2.in', 'r')
w = open('milk2.out', 'w')
data = f.read().split('\n')
num = data[0]
#pop the first line and last line(empty line)
data = data[1:-1]
def split(string):
    return list(map(int,string.split()))
time = list(map(split,data))
#sort based on the starting time
time.sort(key=lambda t:t[0]) 
res = [time[0]]
for i in range(1,len(time)):
    if time[i][0] > res[-1][1]:
        res.append(time[i])
    else:
        res[-1][1] = max(res[-1][1], time[i][1])
milked = max(res,key=lambda t:t[1]-t[0])
milked = milked[1] - milked[0]
notmilked = 0
for i in range(0,len(res)-1):
    notmilked = max(notmilked, res[i+1][0]-res[i][1])
w.write("%d %d\n"%(milked,notmilked))