import random
secretNumber = random.randint(1,20)

#Ask the player to guess 6 times.
for guessesTaken in range (1,7):
    print("Take a Guess")
    guess = int(input())
    
    if guess < secretNumber:
        print("Your guess is too low")
    elif guess > secretNumber:
        print("Your guess is too high")
    else:
        break #This condition is correct guess
    
if guess == secretNumber:
    print("Good Job! You Guessed my number in "+ str(guessesTaken)+
          " guesses!")
else:
    print("Nope. The number i was thinking of was" + str(secretNumber))