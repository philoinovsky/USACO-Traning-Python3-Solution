'''
ID: philoin1
LANG: PYTHON3
TASK: friday
'''
f = open('friday.in', 'r')
w = open('friday.out', 'w')

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def isleap(date):
    if date % 400 == 0:
        return True
    elif date % 100 != 0 and (date % 100) % 4 == 0:
        return True
    else:
        return False

def year(occured, date, x):
    if isleap(date):
        months[1] = 29
    else:
        months[1] = 28
    week = x
    for time in range(12):
        week = (week + 13) % 7
        occured[week] += 1
        week = (week + (months[time]-13)) % 7
    return occured, week

years = int(f.read())
cnt = [0,0,0,0,0,0,0]
start = 1
for time in range(1900, years+ 1900, 1):
  cnt, start = year(cnt, time, start)
for steps in range(6):
  w.write(str(cnt[steps]) + " ")
w.write(str(cnt[6]) + "\n")