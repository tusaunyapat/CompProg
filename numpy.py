import numpy as np
def eq(A, B, p):
    check = A - B
    check = check[check == 0]
    return check

exec(input().strip()) 