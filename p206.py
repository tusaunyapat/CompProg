def T2M(text):
    morse = ''
    for e in text :
        if e not in pattern:
            print('Invalid : '+text)
            return 0
        else :
            j = pattern.find('[' + e + ']')
            j += 3
            k = pattern.find('[',j)
            morse += pattern[j:k] + ' '
    print(morse.strip())

def M2T(morse):
    text = ''
    initial = morse
    morse = morse.split()
    for e in morse:
        # print(e)
        if (']' + e +'[') not in pattern:
            print('Invalid :', initial)
            return 0
        else :
            j = pattern.find(']' + e +'[')
            text += pattern[j-1]
    print(text.strip())

filename = input().strip()
fn = open(filename, 'r')

function = fn.readline().strip()
pattern = fn.readline().strip()

if function != 'T2M' and function != 'M2T':
    print('Invalid code')
else :
    
    text = fn.readline().strip()

    while text != '':
        if function == 'T2M':
            T2M(text)
        elif function == 'M2T':
            M2T(text)
        text = fn.readline().strip()

    
