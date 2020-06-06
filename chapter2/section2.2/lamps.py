'''
ID: philoin1
LANG: PYTHON3
TASK: lamps
'''
f = open('lamps.in', 'r')
w = open('lamps.out', 'w')
data = f.read().split('\n')
N = int(data[0])
C = int(data[1])
ON = list(map(int,data[2].split()))
OFF = list(map(int,data[3].split()))
def btn(nums,type):
    A = 2 if type < 4 else 3
    B = 1 if type % 2 == 0 else 0
    for i in range(len(nums)):
        if type == 1 or (i+1) % A == B:
            nums[i] ^= 1
    return nums
def verify(nums):
    for i in ON:
        if i != -1 and nums[i-1] != 1:
            return False
    for i in OFF:
        if i != -1 and nums[i-1] != 0:
            return False
    return True
def bruteforce(nums,n): # n is number of 1s
    res = []
    for i in R[n]:
        cnt = 1
        NUMS = nums.copy()
        while i and cnt < 5:
            if i & 1:
                NUMS = btn(NUMS,cnt)
            i = i >> 1
            cnt += 1
        if verify(NUMS):
            res.append(NUMS)
    return res
R = [
    [0],
    [1,2,4,8],
    [3,5,6,9,10,12],
    [7,11,13,14],
    [15]
]
lamps = [1] * N
if C < 2:
    res = bruteforce(lamps,C)
elif C == 2:
    res = bruteforce(lamps,0) + bruteforce(lamps,2)
elif C % 2 == 0:
    res = bruteforce(lamps,0) + bruteforce(lamps,2) + bruteforce(lamps,4)
else:
    res = bruteforce(lamps,1) + bruteforce(lamps,3)
res.sort()
if not res:
    w.write("IMPOSSIBLE\n")
else:
    for i in res:
        for j in i:
            w.write("%d"%j)
        w.write("\n")