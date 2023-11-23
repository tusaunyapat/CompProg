a,b,c,d = input().split()

a = float(a)
b = float(b)
c = float(c)
d = float(d)

if a>b:
    a,b = b,a
    # print(a,b,c,d)
if a>c :
    a,c = c,a

if a>d:
    a,d = d,a

if b>c:
    b,c=c,b
    # print(a,b,c,d)
if b>d :
    b,d = d,b

if c>d:
    c,d = d,c
    # print(a,b,c,d)

# print(a,b,c,d)

print(round((b+c)/2,2))