
max_red = -999999
max_blue = -999999
min_red = 1000000000
min_blue = 1000000000
i=0
while True :
    data = input()
    if data == 'Zig-Zag' or data == 'Zag-Zig':
        problem = data
        break
    data = data.split()
    x = int(data[0])
    y = int(data[1])
    if i%2==0:
        if x<min_red:
            min_red = x
        if y>max_blue:
            max_blue = y
        if x>max_red:
            max_red = x
        if y<min_blue:
            min_blue = y
    else :
        if x>max_blue:
            max_blue = x
        if y<min_red:
            min_red = y
        if x<min_red:
            max_red=y
        if y>max_blue:
            max_blue = y
    i+=1

if problem == 'Zig-Zag':
    print(min_red, max_blue, end=' ')
else :
    print(min_blue,max_red, end=' ')
        
    