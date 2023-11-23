def get_product_from_file(textfile):
    product = {}
    fn = open(textfile, 'r')
    text = fn.readline().strip()
    while text !='':
        
        a = text.split('=')
        a[0], a[1] = a[0].strip(),a[1].strip()

        if a[0] == 'created_date':
            a[1] = str(a[1][:2]) + '/' + a[1][2:4] + '/' + a[1][4:]

        #create dict    
        product[a[0]] = a[1]

        text = fn.readline().strip()
    fn.close()

    return product

def cal_defect_ratio(textfile):

    defect_ratio = 0
    b = get_product_from_file(textfile)
    a = b['scan_data']
    # print(type(a))
    plus = a.count('+')
    minus = a.count('-')
    # print(type(plus))
    defect_ratio = (plus)/(plus + minus)

    return round(defect_ratio,2)

def cal_defect_box_ratio(textfile):
    product = get_product_from_file(textfile)
    # print(type(product))
    data = product['scan_data']
    # print(type(data))
    data = data.split(',')
    n = int(round(len(data) ** (1/3),1))
    # run = 0
    # floor = []
    # row = []
    # column = []
    # for i in range(n):
    #     for j in range(n):
    #         for k in range(n):
    #             if data[run] == '+':
    #                 floor.append(i)
    #                 row.append(j)
    #                 column.append(k)
    #             run += 1
    # if floor == []:
    #     height, length, width = 0,0,0
    # else :
    #     height = max(floor) - min(floor) + 1
    #     length = max(row) - min(row) + 1
    #     width = max(column) - min(column) + 1
    n = int(round(len(data)**(1/3),1))
    X = []
    Y = []
    Z = []
    for i in range(len(data)):
        if data[i] == '+':
            x = int(i/n) - n*(int(i/(n*n)))
            y = i%n
            if y == 0:
                y = n
            z = i //(n*n)
            X.append(x)
            Y.append(y)
            Z.append(z)
            # print(x,y,z)
    if X == [] or Y == [] or Z == []:
        height = 0
        length = 0
        width = 0
    else :
        height = max(X) - min(X) + 1
        length = max(Y) - min(Y) + 1
        width = max(Z) - min(Z) + 1
    return round(height *length* width / len(data), 2)

def create_prod_summary_file(pids):
    a = pids[:]
    a.sort()
    # print(type(a))
    if a != []:
        fn = open("product_summary.csv", 'w')
        fn.write('pid,created_date,factory_id,defect_ratio,defect_box_ratio\n')
        forAppend = []
        for i in a :
            dct = get_product_from_file(i+str('.txt'))
            ID = dct['pid']
            date = dct['created_date']
            factory = dct['factory_id']
            ratio = cal_defect_ratio(i+str('.txt'))
            box = cal_defect_box_ratio(i+str('.txt'))
            forAppend.append([str(ID),str(date),str(factory),str(ratio),str(box)])
        forAppend.sort()
        [fn.write(','.join(forAppend[i])+'\n') for i in range(len(forAppend))]
        fn.close()
    
def create_size_summary_file(pids):
    s = 0
    m = 0
    l = 0
    for i in pids:
        if cal_defect_box_ratio(i+str('.txt')) < 0.33:
            s += 1
        elif 0.33 <= cal_defect_box_ratio(i+str('.txt')) < 0.67:
            m += 1
        elif cal_defect_box_ratio(i+str('.txt')) >= 0.67:
            l += 1
    if pids != []:
        fn = open("size_summary.csv", 'w')
        fn.write('size,#\n')
        fn.write('S'+','+str(s)+'\n')
        fn.write('M'+','+str(m)+'\n')
        fn.write('L'+','+str(l)+'\n')
        fn.close()



# create_size_summary_file(["001","009","008"])
# create_prod_summary_file(["001","199","003","004","ABCD","002","010","009","008","007","005"])

print(cal_defect_box_ratio('001.txt'))
print(cal_defect_box_ratio('002.txt'))
print(cal_defect_box_ratio('003.txt'))
print(cal_defect_box_ratio('004.txt'))
print(cal_defect_box_ratio('005.txt'))
print(cal_defect_box_ratio('007.txt'))
print(cal_defect_box_ratio('008.txt'))
print(cal_defect_box_ratio('009.txt'))
print(cal_defect_box_ratio('010.txt'))
print(cal_defect_box_ratio('199.txt'))
print(cal_defect_box_ratio('ABCD.txt'))




