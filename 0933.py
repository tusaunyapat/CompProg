def add_poly(p1, p2):
    poly = {}
    for c, d in p1:
        if d in poly:
            poly[d] += c
        else:
            poly[d] = c
    for c, d in p2:
        if d in poly:
            poly[d] += c
        else:
            poly[d] = c
    ans = []
    for d in sorted(poly)[::-1]:
        if poly[d]!=0:
            ans.append((poly[d], d))
    return ans

def mult_poly(p1, p2):
    ans = []
    for c1, d1 in p1:
        temp = []
        for c2, d2 in p2:
            temp.append((c1*c2, d1+d2))
        ans = add_poly(ans, temp)
    return ans


for i in range(3):
    exec(input().strip())
    