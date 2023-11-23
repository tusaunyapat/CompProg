a = 0
i=0
sum  = 0
while a!='q':
    a = input()
    if a!='q':
        i+=1
        sum+=float(a)
print('No Data') if i==0 else print(round((sum/i),2))
