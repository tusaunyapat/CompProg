


def RLE(text):
    if text=='':
        return []
    char = text[0]
    answer = []

    count = 0
    for i in range(len(text)):
        if char == text[i]:
            count+=1
        else :
            answer.append([char, count])
            char = text[i]
            count = 1
    answer.append([char, count])
    return answer

exec(input())