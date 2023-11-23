data = input()
order = data.split()

orderID = order[0]
option = order[1]
date = int(order[2])
month = int(order[3])
year = int(order[4])
error = []
deliver = []

while data != 'END':
    #error
    d_in_m = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    newYear = year - 543
    if (newYear%400==0) or (newYear%4==0 and newYear%100!=0):
        d_in_m[2] = 29
    if year < 2558 :
        error.append('Error: ' + data + ' --> ' + 'Invalid year')
    elif not (1<=month<=12) :
        error.append('Error: ' + data + ' --> ' + 'Invalid month')
    
    
    elif date > d_in_m[month] or date <1 :
        error.append('Error: ' + data + ' --> ' + 'Invalid date')
    elif option not in 'EQNF':
        error.append('Error: ' + data + ' --> ' + 'Invalid delivery type')
     #deliver
    else :
        
        delivery = ['E','Q','N','F']
        delivery_day = [1,3,7,14]
        index = delivery.index(option)

        date += delivery_day[index]
        if date > d_in_m[month]:
            date -= d_in_m[month]
            month += 1
        if month > 12:
            month -= 12
            year +=1
        deliver.append([year,month,date,orderID])
    
    data = input()
    if data != 'END':
        order = data.split()
        orderID = order[0]
        option = order[1]
        date = int(order[2])
        month = int(order[3])
        year = int(order[4])
    
#error
[print(i) for i in error]
#deliver
deliver.sort()
for i in deliver:
    print(i[3]+': delivered on ' + str(i[2]) +'/'+str(i[1])+'/'+str(i[0]))