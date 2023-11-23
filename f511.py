def missing_digits(data):
    number = [False,False,False,False,False,False,False,False,False,False]
    numString = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    for ch in data:
        if ch in numString:
            index = numString.index(ch)
            number[index] = True

    answer = []

    for i in range(10):
        if not number[i]:
            answer.append(i)

    
    return answer


exec(input())

