order = input().split()
summ = 0
count = 0
minn = 1000
maxx = -50
infile = open(order[0], 'r')

for line in infile:
    sid, point = line.strip().split()
    if sid[0:2] == order[1][-2::]:
        summ += float(point)
        if minn > float(point):
            minn = float(point)
        if maxx < float(point):
            maxx = float(point)
        count += 1

if count == 0:
    print('No data')
else:
    print(minn, maxx, summ/count)