q = list() # ลิสต์ q ใชเ้ก็บขอ้มูลบัตรควิทเี่ หมาะสม
n = int(input()) # อ่านจ านวนค าสั่ง
t_in = list()
time = 0
wait = 0
for k in range(n):
    c = input().split() # อ่านขอ้มูลค าสั่ง
    if c[0] == 'reset':
        first_queue = int(c[1])
        queue = first_queue

    elif c[0] == 'new':
        print('ticket', queue)
        t_in.append(int(c[1]))
        q.append(queue)
        queue += 1

    elif c[0] == 'next':
        call = q.pop(0)
        qtime_dt = t_in.pop(0)
        print('call', call)

    elif c[0] == 'order':
        wait_time = qtime_dt - float(c[1])
        wait += wait_time
        time +=1
        print('qtime',call,abs(int(wait_time)))
    
    elif c[0] == 'avg_qtime':

        avg = abs(wait)/(time)
        print('avg_qtime', round(avg,4) )