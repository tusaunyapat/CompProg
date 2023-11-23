def match(text, check):
    if text == check:
        return True
    return False
    if '?' in check:
        ques = []
        if len(text) != len(check):
            return False
        for i in range(len(text)):
            if check[i] == '?':
                continue
            else :
                if check[i] != text[i]:
                    return False
        return True
    if '(' in  check:
        if not have_check2(text, check):
            return True
        else :
            return False
        
        
    
def have_check2 (text, check):
    k2 = 0
    k1 = check.find('(',k2)
    while True:
        k2 = check.find(')',k1)
        if k2 == -1 or k1 == -1:
            break
        c = check[k1+1:k2]
            
        index = text.find(check[k2+1])
            
        if text[index-1] in c:
            return True
        k1 = k2 + 1
    return False
                
exec(input().strip())