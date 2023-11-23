def is_prime(n):
 # ทดสอบว่า n เป็นจ านวนเฉพาะหรือไม่
    if n <= 1:
        return False
    for k in range(2,int(n**0.5)+1):
        if n%k == 0:
            return False
    return True

def next_prime(N):
    while True:
        if is_prime(N+1):
            return N+1
        else:
            N+=1


def next_twin_prime(N):
 # คืนจ านวนเฉพาะสองค่าที่เป็น twin prime ที่มีค่าน้อยสุดที่มากกว่า N
 # twin prime คือจ านวนเฉพาะที่มีค่าต่างกัน 2 เชน่ 11 กับ 13 หรือ 41 กับ 43
    i=0
    
    while True:
        
        a = next_prime(N)
        b = next_prime(a)
        
        if b-a ==2:
            print('(',end='')
            print(a,end='')
            print(',',b,end='')
            print(')')
            break
        else :
            N+=1

exec(input().strip()) 