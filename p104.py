result = list(input())
want = int(input())
newResult = []
score = [0,0,0,0,0,0,0,0,0,0]
i=0

while i!=len(result):
    newResult.append(result[i])
    if result[i] == 'X':
        newResult.append('0')
    i += 1

if len(newResult)%2==1:
    newResult.append('0')

result = newResult
# print(len(result))

frame = 0

# print(result)
for i in range (0,len(result), 2):
    
    # strike
    if result[i] == 'X':
        point = 10
        if frame!=10: # frame 10
            if result[i+2] == 'X':
                point += 10
                if result[i+4] == 'X':
                    point += 10
                else :
                    point += int(result[i+4])
            
            elif result[i+3] == '/':
                point += 10
            else :
                # print('this case', result[i+2], result[i+3])
                point += int(result[i+2]) + int(result[i+3])

    elif result[i+1] == '/':
        point = 10
        if frame!=10:
            if result[i+2] == 'X':
                point += 10
            else :
                point += int(result[i+2])
    else :
        point = int(result[i]) + int(result[i+1])
        

    score[frame] = point
    if frame == 9:
        break
    frame += 1

if want > 0 and want < 11 :
    print(score[want-1])
else :
    print(sum(score))


