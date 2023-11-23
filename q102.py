def f1(a, b, c):
    if a < 0:
        if b > c:
            return int(c)
        else :
            return int(b)
    if b < 0:
        if a > c:
            return int(c)
        else :
            return int(a)
    if c < 0:
        if b > a:
            return int(a)
        else :
            return int(b)


def f2(a, b, c):
    if a > 0:
        if b > c:
            return int(b)
        else :
            return int(c)
    if b > 0:
        if a > c:
            return int(a)
        else :
            return int(c)
    if c > 0:
        if b > a:
            return int(b)
        else :
            return int(a)

def f3(a, b, c):
    s = a + b + c
    s = abs(s)
    s = str(s)
    return s[0]

def f4(a, b, c):
    s = a + b + c
    s = abs(s)
    s = str(s)
    return s[-1]

def main():
    s1, s2, a, b, c = [int(e) for e in input().split()]
    if s1 == 0 and s2 == 0:
        print(f1(a, b, c))
    if s1 == 0 and s2 == 1:
        print(f2(a, b, c))
    if s1 == 1 and s2 == 0:
        print(f3(a, b, c))
    if s1 == 1 and s2 == 1:
        print(f4(a, b, c))
    else :
        print('Error')

exec(input().strip())