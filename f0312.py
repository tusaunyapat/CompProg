def day_of_year(d,m,y):  

    y -=543

    day = [0,31,28,31,30,31,30,31,31,30,31,30,31]

    days = d
    

    # 28 or 29
    if m>=2:
        if y % 400 == 0:
            day[2]=29
            
        if y % 4 == 0 and y % 100 !=0:
            day[2]=29

    for i in range(m):
        days +=day[i]

    return days

exec(input())