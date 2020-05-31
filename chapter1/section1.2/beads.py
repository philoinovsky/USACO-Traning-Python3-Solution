'''
ID: philoin1
LANG: PYTHON3
TASK: beads
'''
f = open('beads.in', 'r')
w = open('beads.out', 'w')
l = list(f.read().split('\n')[1])
#cut before i
def expand(left, dir):
    lc = None
    n = -1 if dir == 'left' else 1
    cnt = 0
    while(True):
        left %= len(l)
        if cnt >= len(l):
            return len(l)
        if lc == None and l[left] != 'w':
            lc = l[left]
            left += n
            cnt += 1
        elif lc and l[left] not in [lc,'w']:
            return cnt
        else:
            left += n
            cnt += 1

maxx = 0
for i in range(len(l)):
    leftstart = (i-1) % len(l)
    rightstart = (i) % len(l)
    left = expand(leftstart,'left')
    right = expand(rightstart,'right')
    if left + right >= len(l):
        print(left,right,i)
        w.write("%d\n"%len(l))
        exit()
    else:
        maxx = max(maxx, left + right)

w.write("%d\n"%maxx)