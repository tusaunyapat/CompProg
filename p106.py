choice = input().strip()
num = int(input())
data = []

for i in range(num):
    raw = input().strip()
    data.append(raw)
    
length = len(data[0])

diff = False

for i in range(num):
    if len(data[i])!=length:
        diff = True
        print('Invalid size')
        break

if not diff:
    if choice == '90':
        for i in range(len(data[0])):
            for j in range(num):
                if j != num-1:
                    print(data[num-j-1][i],end='')
                else:
                    print(data[num-j-1][i],end='\n')

    elif choice == 'flip':
        for i in range(num):
            print(data[i][::-1])

    elif choice == '180':
        for i in range(num):
            print(data[num-i-1][::-1])
