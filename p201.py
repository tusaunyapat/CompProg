def is_odd(n):
    return True if n % 2 == 1 else False
def has_odds(x):
    for i in x:
        if is_odd(i):
            return True 
    return False
def all_odds(x):
    for i in x:
        if not is_odd(i):
            return False
    return True
def no_odds(x):
    for i in x:
        if is_odd(i):
            return False
    return True
def get_odds(x):
    ans = []
    for i in x:
        if is_odd(i):
            ans.append(i)
    return ans
def zip_odds(a, b):
    num = 0
    ans = []
    newA = get_odds(a)
    newB = get_odds(b)
    for i in range(max(len(newA), len(newB))):
        if len(newA)!=0:
            num = newA.pop(0)
            ans.append(num)
        if len(newB)!=0:
            num = newB.pop(0)
            ans.append(num)
    return ans
exec(input().strip())
