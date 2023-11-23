import math

a,b,c = input().split(',')
down = ((10**(len(b+c)))-(10**len(b)))
up = (int(a+b+c) - int(a+b))

gcd = math.gcd(up,down)
print(down)
print(up)
print(gcd)

print('answer =======>',int(up/3), '/', int(down/3))