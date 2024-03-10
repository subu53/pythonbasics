import random, sys
print("Rock, Paper,& Scissors Game")

#These variables keep track of the number of wins, lossess and ties
wins = 0
losses = 0
ties = 0

while True: #the main game loop
    print('%s Wins, %s Losses, %s Ties' %(wins, losses, ties))
    while True : #Player input loop
        print('Enter your move: (r)ock (p)aper s(cissors) or q(uit)')
        playerMove = input()
        if playerMove =='q':
            sys.exit #Quit the Program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break #Break out of the player input loop.
        print('Type one of r, p, s, or q')
        
    #Display what the player chose:
    if playerMove == 'r':
        print('Rock Versus ...')
    elif playerMove == 'p':
        print('Paper Versus ...')
    elif playerMove == 's':
        print('Scissors Versus ...')
    
    #Display what the Computer chose:
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = "r"
        print("Rock")
    elif randomNumber == 2:
        computerMove = "p"
        print("Paper")
    elif randomNumber == 3:
        computerMove = "s"
        print("Scissors")
    #Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties +1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins +1
    elif playerMove == 'p'and  computerMove == 'r':
        print('You win!')
        wins = wins +1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins +1
    elif playerMove == 'r' and computerMove == 'p':
        print('You Lose!')
        losses = losses +1
    elif playerMove == 'p' and computerMove == 's':
        print('You Lose!')
        losses = losses +1
    elif playerMove == 's' and computerMove == 'r':
        print('You Lose!')
        losses = losses +1
            