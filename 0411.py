num = int(input())
red = []
blue = []

for i in range(num):
    x,y = input().split()
    x = int(x)
    y = int(y)
    if i%2==0:
        red.append(x)
        blue.append(y)
    else :
        blue.append(x)
        red.append(y)

red.sort()
blue.sort()

problem = input()

if problem == 'Zig-Zag':
    minn = red[0]
    maxx = blue[-1]
else :
    minn = blue[0]
    maxx = red[-1]

print(minn, maxx, end=' ')

