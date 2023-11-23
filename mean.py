import numpy as np

def read_data():
 # อ่านข ้อมูลจากแป้นพิมพ์ จากนั้นสร้างและคืนอาเรย์สองตัว
 # weight เป็นอาเรย์สามชอ่ งเก็บน ้าหนักของคะแนนกลางภาค ปลายภาค และโครงงาน (float)
 # data เป็นอาเรย์ขนาด n4 เก็บข ้อมูลนักเรียน n คน แต่ละคนมีข ้อมูล
 # เลขประจ าตัว คะแนนกลางภาค ปลายภาค และโครงงาน (int)
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    # print(data)
    return weight, data

def report_lower_than_mean(weight, data):
 # แสดงเลขประจ าตัวที่ได้คะแนนรวมต ่ากว่าคะแนนเฉลี่ย
 # - คะแนนรวม ค านวณมาจากผลรวมของ คะแนนแต่ละสว่ นคูณด้วยน ้าหนักของแต่ละสว่ น
 # - คะแนนเฉลี่ย คือค่าเฉลี่ยของคะแนนรวมต่าง ๆ
 # ให้แสดงบนบรรทัดเดียวกันหมดคั่นดว้ยเครอื่ งหมายจลุ ภาคและชอ่ งว่างหนงึ่ ชอ่ ง
 # เรียงตามล าดับที่ปรากฎใน data ถ้าไม่มีใครได้ต ่ากว่าคะแนนเฉลี่ยเลย ให้แสดงค าว่า None
    total = np.sum(data[:,1:] * weight, axis = 1)
    # print(a)
    mean = np.mean(total)
    ans = data[:,0][total < mean]
    if len(ans) == 0:
        print('None')
    else:
        print(', '.join([str(e) for e in ans]))

exec(input().strip())