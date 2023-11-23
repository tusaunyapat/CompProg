data = input().split()
answer = True

for i in range(10):
    
    if i == 0:
        if data[i] > data[i+1]:
            answer = False
            break
    
    elif float(data[i-1]) > float(data[i]):
        answer = False
        break

if answer:
    print('true')
else :
    print('false')

