h1, m1, h2, m2 = [int(e) for e in input().split()]

sec1 = h1*60 + m1
sec2 = h2*60+m2

d_sec = sec2 -sec1

dh = d_sec // 60
dm = d_sec - (dh*60)
if dh < 0:
    dh +=12

print(dh, dm)
