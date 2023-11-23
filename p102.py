choice = input()

if choice == 'str2RLE':
    text = input()
    char = text[0]
    
    count = 0
    for i in range(len(text)):
        if char == text[i]:
            count+=1
        else :
            print(char, count, end = ' ')
            char = text[i]
            count = 1
    print(char, count)

elif choice == 'RLE2str':
    text = input().split()
    alp = text[0::2]
    num = text[1::2]
    for i in range(len(num)):
        print(alp[i]*int(num[i]),end='')
        
else :
    print('Error')