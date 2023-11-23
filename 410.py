import math

a = float(input())
num = a
L = 0
count = 0
while num!=0:
    num = num //10
    count+=1


U = count
x = (L+U)/2
while not math.isclose(a, 10**x):
    if 10**x > a:
        U = x
    else :
        L = x
    x = (L+U)/2
print(round(x,6))