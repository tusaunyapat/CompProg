def check_digit(n):
    sum = 0
    for i in range(12):
        sum += (13-i)*int(n[i])
    n12 = (11-(sum%11))%10
    return n12


exec(input())


