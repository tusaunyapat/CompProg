def win(player1, player2,score1, score2):
    if player1==player2:
        return score1, score2
    
    if player1 == 'R':
        if player2 == 'S':
            score1 += 1
        else :
            score2 += 1

    if player1 == 'S':
        if player2 == 'R':
            score2 += 1
        else :
            score1 += 1

    if player1 == 'P':
        if player2 == 'S':
            score2 += 1
        else :
            score1 += 1
    return score1, score2

m = int(input())
score1 = 0
score2 = 0
times = 0
check = False
while   times < 3*m:
    times += 1
    player1, player2 = input().split()
    score1, score2 = win(player1, player2,score1, score2)
    if score2 == m or score1 == m:
        print(score1, score2)
        print('Player 2 wins') if score2 > score1 else print('Player 1 wins')
        check = True
        break
    
if not check :
    print(score1, score2)
    print('Tie')