import math

a = float(input())
L = 0
U = a
x = (L+U)/2

while abs(a-x**2)>=(10**(-10))*max(a,x**2):
    if x ** 2 > a:
        U = x
    else :
        L = x
    x = (L+U)/2

# print(x)
if math.log10(x**2)<0:
    print(round(math.log10(x**2),6)*-1)

else :
    print(round(math.log10(x**2),6))