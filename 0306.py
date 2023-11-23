id_1, gpax_1, com_1, cal1_1, cal2_1 = input().split()
id_2, gpax_2, com_2, cal1_2, cal2_2 = input().split()

com_1_check = False
com_2_check = False
cal1_1_check = False
cal1_2_check = False
cal2_1_check = False
cal2_2_check = False



if com_1 == "A":
    com_1_check = True

if com_2 == "A":
    com_2_check = True

if cal1_1 !='D' and cal1_1!='F':
    cal1_1_check = True

if cal2_1 !='D' and cal2_1!='F':
    cal2_1_check = True

if cal1_2 !='D' and cal1_2!='F':
    cal1_2_check = True

if cal2_2 !='D' and cal2_2!='F':
    cal2_2_check = True

#choose
# if not com_1_check and not com_2_check:
#     print('None')

if com_1_check and cal1_1_check and cal2_1_check:
    if com_2_check and cal1_2_check and cal2_2_check:
        if gpax_1 > gpax_2:
            print(id_1)
        elif gpax_2>gpax_1:
            print(id_2)
        else :
            if cal1_1 < cal1_2:
                print(id_1)
            elif cal1_2 < cal1_1:
                print(id_2)
            else :
                if cal2_1 < cal2_2:
                    print(id_1)
                elif cal2_2 < cal2_1:
                    print(id_2)
                else :
                    print('Both')
                    
    else :
        print(id_1)
else :
    if com_2_check and cal1_2_check and cal2_2_check:
        print(id_2)
    else :print('None')









