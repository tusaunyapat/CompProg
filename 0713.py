string = input()
s = []
word = ''

for i in range(len(string)):
    if (ord(string[i]) >=48 and ord(string[i]) <= 57) or (ord(string[i]) >=65 and ord(string[i]) <= 90) or (ord(string[i]) >=97 and ord(string[i]) <= 122) :
        word += string[i]
    else :
        s.append(word)
        word = ''
s.append(word)

a = []
for i in range(len(s)):
    if s[i] != '':
        a.append(s[i])

def convert(s):
    return s[0].upper() + s[1::].lower()


for i in a:
    if i == a[0]:
        print(convert(i).lower(), end='')
    else :
        print(convert(i), end='')
  
