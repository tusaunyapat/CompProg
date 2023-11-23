def knows(R,x,y):
    # return True if x knows y
    
    return True if y in R[x] else False
    
def is_celeb(R,x): # return True if a is celeb, otherwise return False
    # return False if x knows someone who is not him/herself
    # return False if there exists someone in R who don't know x
    # otherwise return True\
    if R[x] != set() and R[x] != {x}:
        
        return False
    for i in R:
        if i != x:
            if x not in R[i] :
                # print('here',x)
                return False
    return True


def find_celeb(R):
    # for each person x in the party
    # if x is celeb --> return x
    # if no celeb in the party --> return None
    for x in R:
        if is_celeb(R, x) :
            return x
    return None
def read_relations() :
    # build a dictionary R from inputs
    # whose structure is shown in the example
    
    R = dict()
    while True:
        d = input().split()
        if len(d) == 1 : break
        if d[0] not in R:
            R[d[0]] = set()
        if d[1] not in R:
            R[d[1]] = set()
        R[d[0]].add(d[1])
        
    return R
def main():
    R = read_relations()
    
    c = find_celeb(R)
    if c == None :
        print('Not Found')
    else:
        print(c)
exec(input().strip()) # do not remove this line