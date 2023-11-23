password = input().strip()
error = []


def length_morethan_8(s):
    return True if len(s) >=8 else False

def have_lowercase(s):
    for i in s:
        if ord(i) >=97 and ord(i) <= 122 :
            return True
    return False

def have_uppercase(s):
    for i in s:
        if ord(i) >=65 and ord(i) <= 90 :
            return True
    return False

def have_number(s):
    for i in s:
        if ord(i) >=48 and ord(i) <= 57 :
            return True
    return False

def have_symbol(s):
    for i in s:
        if i in '!@#$%^&*()_+/"' :
            return True
    return False

def is_repeat(s):
    for i in range(len(s)-3):
        if s[i] == s[i+1] and s[i+1] == s[i+2] and s[i+2] == s[i+3]:
            return True
    return False

def is_number_sequence(s):
    s = s.lower()
    key = ['01234567890', '0987654321']
    for i in range(len(s)-3):
        check = s[i:i+4]
        if sequence(check, key) :
            return True
    return False

def is_letter_sequence(s):
    s = s.lower()
    for i in range(len(s)-3):
        # print(ord(s[i]), ord(s[i+1]), ord(s[i+2]), ord(s[i+3]))
        if ord(s[i]) >=97 and ord(s[i]) <= 122 :
            
            if (ord(s[i]) - ord(s[i+1])) == 1 and (ord(s[i+1]) - ord(s[i+2])) == 1 and (ord(s[i+2]) - ord(s[i+3])) == 1:
                return True
            if (ord(s[i]) - ord(s[i+1])) == -1 and (ord(s[i+1]) - ord(s[i+2])) == -1 and (ord(s[i+2]) - ord(s[i+3])) == -1:
                return True
    return False

def sequence(s, key):
    s =s.lower()
    
    for i in key:
        if s in i :
            return True
    return False


def is_keyboard_sequence(s):
    s = s.lower()
    key = ['!@#$%^&*()_+', 'qwertyuiop', 'asdfghjkl', 'zxcvbnm','+_)(*&^%$#@!)', 'poiuytrewq', 'lkjhgfdsa','mnbvcxz']
    for i in range(len(s)-3):
        check = s[i:i+4]
        if sequence(check, key) :
            return True
    return False


if not length_morethan_8(password) : error.append('Less than 8 characters')
if not have_lowercase(password) : error.append('No lowercase letters')
if not have_uppercase(password) : error.append('No uppercase letters')
if not have_number(password) : error.append('No numbers')
if not have_symbol(password) : error.append('No symbols')
if is_repeat(password) : error.append('Character repetition')
if is_number_sequence(password) : error.append('Number sequence')
if is_letter_sequence(password) : error.append('Letter sequence')
if is_keyboard_sequence(password) : error.append('Keyboard pattern')

if len(error) > 0:
    for i in error:
        print(i)
else :
    print('OK')


# python 0732.py