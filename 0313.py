import math

day = [0,31,28,31,30,31,30,31,31,30,31,30,31]

bd, bm, by, d, m, y = [int(e) for e in input().split()]

# red
red = day[bm] - bd +1

by -= 543
y -= 543

if bm<=2:
    if by % 400 == 0:
        red+=1
    if by % 4 == 0 and by % 100 !=0:
        red+=1

for i in range(bm+1,13):
    red += day[i]

# print('red = ',red)

# black
black = 365 * (y - by -1)
# print('black = ',black)

# blue
blue = d

if m>=2:
    if y % 400 == 0:
        blue+=1
    if y % 4 == 0 and y % 100 !=0:
        blue+=1

for i in range(m):
    blue  += day[i]

blue-=1

# print('blue = ',blue)
t = red + black + blue
print(t,end=' ')

phys = math.sin(2*math.pi*t/23)
print('{:.2f}'.format(phys),end=' ')

emo = math.sin(2*math.pi*t/28)
print('{:.2f}'.format(emo),end=' ')

intel = math.sin(2*math.pi*t/33)
print('{:.2f}'.format(intel),end=' ')

