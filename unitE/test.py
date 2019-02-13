


import random

secretNum = random.randint(1,100)

print("Welcome to the guessing game.")
print("You need to guess a number from 1 to 100.")

guess=0
counter=0

while (guess != secretNum):
    guess = int(input("What is your guess: "))
    counter+=1
    
    if(guess < secretNum):
        print('Guess is too low.')
    elif(guess > secretNum):
        print('Guess is too high.')
    else:
        print("Congratulations!")
        print('You guessed the secret number in',counter,'guesses!')
