color = {
    'black' :0,
    'brown' :1,
    'red'   :2,
    'orange':3,
    'yellow':4,
    'green' :5,
    'blue'  :6,
    'violet':7,
    'grey'  :8,
    'white' :9,
    'gold'  :-1,
    'silver':-2
}
error = {
    'brown' :'1%',
    'red'   :'2%',
    'green' :'0.5%',
    'blue'  :'0.25%',
    'violet':'0.10%',
    'grey'  :'0.05%',
    'gold'  :'5%',
    'silver':'10%'
}
do = True
ohm = ''

data = input().strip().split(',')
#error
if data[-1] not in error:
    do = False

if data[0] == 'black':
    do = False

if do :
    for i in range(len(data[:-2])):
        if data[i] in color and data[i] != 'gold' and data[i] != 'silver':
            ohm += str(color[data[i]])
        else :
            do = False
            break
if do :
    ohm = int(ohm)
    if data[-2] in color:
        ohm *= 10**(color[data[-2]])
        print('Resistor: %g Ohms' %ohm)
        print('Error: '+ error[data[-1]])
    else :
        do = False

if not do :
    print('Program Error')
    

        


