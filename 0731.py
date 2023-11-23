dna = input().upper()
option = input()
new = ''
count = 0
DNA = True

if option == 'R':
    for i in dna:
        if i == 'A': new += 'T'
        elif i == 'T': new += 'A'
        elif i == 'C': new += 'G'
        elif i == 'G': new += 'C'
        else :
            DNA = False
            break
    if DNA : print(new[::-1])

if option == 'F':
    if dna.count('A') + dna.count('T') + dna.count('G') + dna.count('C') == len(dna):
        print('A='+str(dna.count("A"))+', '+'T='+str(dna.count("T"))+', '+'G='+str(dna.count("G"))+', '+'C='+str(dna.count("C")))
    else :
        print('Invalid DNA')

if option == 'D':
    condition = input().upper()
    if dna.count('A') + dna.count('T') + dna.count('G') + dna.count('C') == len(dna):
        for i in range(len(dna)-1):
            if dna[i] == condition[0] and dna[i+1] == condition[1]:
                count+=1
        print(count)
    else :
        print('Invalid DNA')
    




        