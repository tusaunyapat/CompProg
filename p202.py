card = input()
ans = ''
def get_num(char):
    if char == 'A':return 1
    elif char == 'T':return 10
    elif char == 'J':return 11
    elif char == 'Q':return 12
    elif char == 'K':return 13
    else : return int(char)
def get_value_alp(char):
    if char == 'C':return 1
    elif char == 'D':return 2
    elif char == 'H':return 3
    elif char == 'S':return 4
for i in range(0,len(card)-2,2):
    num_1 = get_num(card[i])
    num_2 = get_num(card[i+2])
    if num_1 > num_2:
        ans += '+' + str(num_1-num_2)
    elif num_1 < num_2:
        ans += str(num_1-num_2)
    else :
        alp_1 = get_value_alp(card[i+1])
        alp_2 = get_value_alp(card[i+3])
        if alp_1 > alp_2:
            ans += '+' + str(alp_1-alp_2)
        elif alp_1 < alp_2:
            ans += str(alp_1-alp_2)
        else :
            ans += '0'
print(ans)