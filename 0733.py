def read_next(f):
    while True:
        t = f.readline()
        if len(t) == 0: # ถ้าอ่านหมดแล้ว ออกจากวงวน
            break
        x = t.strip().split() # ลบ blank ซ้ายขวา
        if len(x) == 2: # แยกแล้วได้ 2 ส่วน --> ถูกต้อง ก็คืนผล
            return x[0], x[1]
    return "", ""
def less(sid1, sid2):
    if sid1[-2:] < sid2[-2:] :
        return True
    elif sid1[-2:] > sid2[-2:] :
        return False
    return sid1 < sid2
    
fn1, fn2 = input().split()
f1 = open(fn1, 'r')
f2 = open(fn2, 'r')
sid1, grade1 = read_next(f1)
sid2, grade2 = read_next(f2)

while sid1 != '' or sid2 != '':
    if sid1 != '' and sid2 != '':
        if less(sid1, sid2) :
            print(sid1, grade1)
            sid1, grade1 = read_next(f1)
        else :
            print(sid2, grade2)
            sid2, grade2 = read_next(f2)
    elif sid1 == '':
        print(sid2, grade2)
        sid2, grade2 = read_next(f2)
    elif sid2 == '':
        print(sid1, grade1)
        sid1, grade1 = read_next(f1)
