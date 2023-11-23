def make_int_list(x):
    answer = []
    x = x.split()
    for i in x:
        answer.append(int(i))
    return answer

def is_odd(e):
    if e%2 == 0:
        return False
    else:
        return True
    
def odd_list(alist):
    answer = []
    for i in alist:
        if is_odd(i):
            answer.append(i)
    return answer

def sum_square(alist):
    summ = 0
    for i in alist:
        summ += int(i)*int(i)
    return summ

exec(input().strip())

        