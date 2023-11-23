number = float(input())
# print(round(number, 2))
string = str(round(number, 2))
# print(string)
string = string.split('.')
print(string)

number = string[0]


for i in range(len(number)):
    print(number[i],end='')
    if len(number) % 3 == 0:
        if i % 3 == 2 and i != len(number)-1:
            print(',',end='')
    if len(number) % 3 == 1:
        if i % 3 == 0 and i != len(number)-1:
            print(',',end='')
    if len(number) % 3 == 2:
        if i % 3 == 1 and i != len(number)-1:
            print(',',end='')
# print(string)

if len(string[1]) == 2:
    print('.'+string[1])
elif len(string[1]) == 1:
    print('.'+string[1]+'0')
else :
    print('.00')
    
    