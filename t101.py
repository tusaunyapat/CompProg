a, b, c = [float(e) for e in input().split()]

check = b**2 - 4*a*c

if check > 0:
    print('2')
elif check < 0:
    print('3')
else :
    print('1')