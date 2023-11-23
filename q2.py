filename = input()
keyword = input().lower()
new = input()
changing = True
text = ' '
fn = open(filename, 'r')



while text != '' :
    text = fn.readline().strip()
    text.lower()
    index_slash = [-1]
    check = []
    ans = ''
    for i in range(len(text)):
        if text[i] == '/':
            index_slash.append(i)
    
    # print(index_slash)

    for i in range(1,len(index_slash)):
        if index_slash[i] - index_slash[i-1] == len(keyword) + 1:
            if index_slash[i-1] == -1:
                check.append(0)
            else :
                check.append(index_slash[i-1])
    print(index_slash)
    print(check)




