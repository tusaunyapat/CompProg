first = input()
second = input()
answer = True

for i in range(len(first)):
    if (first[i] == 'A' and second[i] == 'T') or (first[i] == 'T' and second[i] == 'A') or (first[i] == 'C' and second[i] == 'G') or (first[i] == 'G' and second[i] == 'C'):
        asnwer = True
    else :
        answer = False
        break

if answer:
    print('true')
else :
    print('false')