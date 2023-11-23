word = input()
ans = []
answer = ''
while word != 'end':
    
    for i in range(len(word)):
        if (ord(word[i]) >=65 and ord(word[i]) <= 90) or (ord(word[i]) >=97 and ord(word[i]) <= 122) :
            Ascii = ord(word[i])
            Ascii += 13
            if Ascii > 90 and Ascii < 104:
                Ascii -= 26
            elif Ascii > 122 and Ascii < 136:
                Ascii -= 26
            answer += chr(Ascii)
            
        else :
            answer += word[i]
    ans.append(answer)
    answer = ''
    word = input()

[print(i) for i in ans]