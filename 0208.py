import math

a,b,c = input().split(',')
up = (int(a+b+c) - int(a+b))
down = ((10**(len(b+c)))-(10**len(b)))

gcd = math.gcd(up,down)

print(up//gcd,'/',down//gcd)