import math

a,b,c = input().split(',')
check_b = '...'
if b =='' :
    check_b = ''
    b = '0'
# print(int(b))

num_dec = int(a) + int(int(b)/(10**len(b)))
# print(num_dec)
# processing

# num9 start
num9 = 0
for i in range(len(c)):
    num9 += 9*(10**(i))

if check_b != '':
    num9 = num9 * (10 ** len(b))
# num9 end
# print(num9)
# เศษส่วนอย่างต่ำ
gcd = 1
if int(c)!=0:
    gcd = math.gcd(int(c), num9)
    # print('gcd = ',gcd)
    # newC = int(int(c)/gcd)
    newNum9 = num9/gcd
    print('num9 = ',num9)
    print('gcd = ',gcd)
    print('newNum9 = ',int(newNum9))
    # print("{:.15f}".format(newNum9))
    # print('newNum9 = ',newNum9)
    # answer = int(num_dec*newNum9 + newC)
    # print(int(answer), '/', int(newNum9))
# else :
#     newA = int(num_dec*(10**len(b)))
#     gcd = math.gcd(newA,10**len(b))
#     print('gcd = ',gcd)
#     answer = int(newA/gcd)
#     print(int(answer), '/', int((10**len(b))/gcd))




# print(int(num1/gcd))