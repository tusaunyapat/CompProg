alp = {
        'a':2,
        'b':22,
        'c':222,
        'd':3,
        'e':33,
        'f':333,
        'g':4,
        'h':44,
        'i':444,
        'j':5,
        'k':55,
        'l':555,
        'm':6,
        'n':66,
        'o':666,
        'p':7,
        'q':77,
        'r':777,
        's':7777,
        't':8,
        'u':88,
        'v':888,
        'w':9,
        'x':99,
        'y':999,
        'z':9999,
        ' ':0
    }
num = {}
for key in alp:
    value = alp[key]
    num[value] = key


def text2keys(text):
    text = text.lower()
    s = ''
    for i in text:
        if i in alp:
            s+= str(alp[i]) +' '
    return s[:-1]

def keys2text(keys):
    s = ''
    keys = keys.split()
    for i in keys:
        if int(i) in num:
            s += num[int(i)]
    return s
exec(input().strip())
