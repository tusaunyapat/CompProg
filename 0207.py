code = input()
code = list(code)

dt_1 = (int(code[31])*1) + (int(code[24])*10) + (int(code[17])*100) + (int(code[10])*1000) + (int(code[3])*10000)

dt_2 = 0

for i in range(5):
    # print(int(code[7+(5*i)]))
    # print(10**(4-i))
    dt_2 += (int(code[7+(5*i)]))*(10 ** (4-i))
    
dt_3 = dt_1 + dt_2 + 10000

# dt_3 = list(dt_3)
# summ = int(dt_3[-1]) + int(dt_3[-2]) + int(dt_3[-3])

unit = (dt_3 % 100) // 10
ten = (dt_3 % 1000) // 100
hundred = (dt_3 % 10000) // 1000

dt_5 = ((unit + ten + hundred) % 10) + 1

alp = ['-','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
answer = (hundred*100) + (ten*10) + unit

print(hundred,end='')
print(ten,end='')
print(unit,end='')
print(alp[dt_5], end='')
