'''
ID: philoin1
LANG: PYTHON3
TASK: numtri
'''
f = open('numtri.in', 'r')
w = open('numtri.out', 'w')
data = f.read().split('\n')
def split(string):
    return list(map(int,string.split()))
R = int(data[0])
nums = list(map(split,data[1:R+1]))
for i in range(1,R):
    for j in range(len(nums[i])):
        left = nums[i-1][j-1] if j > 0 else 0
        right = nums[i-1][j] if j < len(nums[i-1]) else 0
        nums[i][j] += max(left,right)
res = max(nums[-1])
w.write("%d\n"%res)