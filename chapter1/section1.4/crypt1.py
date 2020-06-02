'''
ID: philoin1
LANG: PYTHON3
TASK: crypt1
'''
from itertools import product
f = open('crypt1.in', 'r')
w = open('crypt1.out', 'w')
data = f.read().split('\n')
nums_str = data[1].split()
nums = list(map(int,data[1].split()))
def isvalid(num, type):
    n = 999 if type == "partial" else 9999
    d = 3 if type == "partial" else 4
    digit = 0
    if num > n:
        return False
    while num:
        num, r = divmod(num, 10)
        digit += 1
        if r not in nums:
            return False
    if digit < d:
        return 0 in nums
    else:
        return True
cnt = 0
for i in product(nums_str,repeat=5):
    s = ''.join(i)
    first = int(s[:3])
    s1 = int(s[3:4]) #second 1st digit
    s2 = int(s[4:5]) #second 2nd digit
    p1 = s1*first   #partial 1
    p2 = s2*first   #partial 2
    summ = p1 + 10*p2 #sum
    if isvalid(p1,"partial") and isvalid(p2,"partial") and isvalid(summ,"total"):
        cnt += 1
w.write("%d\n"%cnt)