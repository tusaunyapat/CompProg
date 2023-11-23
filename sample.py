def match(s, pattern):
    if len(s) != len(pattern):
        return False
    for i in range(len(pattern)):
        if s[i].lower() != pattern[i] and pattern[i] != '?':
            return False
    return True

def rename(s, pattern, word):
    k1 = 0
    out  = ''
    while True:
        k2 = s.find('/', k1)
        if k2 == -1:break
        folder = s[k1:k2]
        if match(folder, pattern):
            out += word + '/'
        else :
            out += folder + '/'
        k1 = k2 + 1
    return out + s[k1:]

filename = input().strip()
pattern = input().strip().lower()
replace = input().strip()
fn = open(filename, 'r')
for text in fn:
    print(rename(text.strip(), pattern, replace))
fn.close()

        