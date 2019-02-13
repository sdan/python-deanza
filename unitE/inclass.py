import random
''' 
Surya Dantuluri
CIS 41A   Winter 2019 
Unit E take-home assignment 
'''

# Script 1
def plantedInVegetableGarden(type,height):
    if(type=="Vegetable"):
        return True
    else:
        return 

def plantedInLowGarden(type,height):
    if(type=="Flower" and (int(height)<3 or int(height)==3)):
        return True
    else:
        return 

def plantedInHighGarden(type,height):
    if(type=="Flower" and (int(height)<6 or int(height)==6)):
        return True
    else:
        return 

plantName = input("Please enter the plant name: ")
plantType = input("Please enter the plant type: ")
plantHeight = input("Please enter the plant height: ")

whichGarden = []

if(plantedInVegetableGarden(plantType,plantHeight)):
    whichGarden.append("Vegetable Garden")
    
if(plantedInLowGarden(plantType,plantHeight)):
    whichGarden.append("Low Garden")
    
if(plantedInHighGarden(plantType,plantHeight)):
    whichGarden.append("High Garden")

if(len(whichGarden)==0):
    print("A",plantName,"cannot be planted in any Garden")
if(len(whichGarden)==1 or len(whichGarden)>1 or len(whichGarden)>2):
    print("A",plantName,"can be planted in the",whichGarden[0],end="")
    if(len(whichGarden)>1):
        print(" or",whichGarden[1])
        if(len(whichGarden)>2):
            print("or ",whichGarden[2])

# Script 2
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

# Script 3
quote = "Believe you can and you're halfway there."

iterate = 0
for findA in quote:
    if(findA=="a"):
        print("a found at index",iterate)
    iterate+=1

rows = int(input('Please enter the number of rows for the multiplication table: '))
    
for i in range(rows):
    for j in range(i+1):
        print ((i+1)*(j+1), end=" ")
    print("")

''' 
Execution results: 

Please enter the plant name: Lily
Please enter the plant type: Flower
Please enter the plant height: 3
A Lily can be planted in the Low Garden or High Garden

Please enter the plant name: Bonsai
Please enter the plant type: Tree
Please enter the plant height: 2
A Bonsai cannot be planted in any Garden

Please enter the plant name: Carrots
Please enter the plant type: Vegetable
Please enter the plant height: 1
A Carrots can be planted in the Vegetable Garden

Please enter the plant name: Corn
Please enter the plant type: Vegetables
Please enter the plant height: 8
A Corn cannot be planted in any Garden

Please enter the plant name: Rose
Please enter the plant type: Flower
Please enter the plant height: 5
A Rose can be planted in the High Garden

Please enter the plant name: Sunflower
Please enter the plant type: Flower
Please enter the plant height: 8
A Sunflower cannot be planted in any Garden

Welcome to the guessing game.
You need to guess a number from 1 to 100.
What is your guess: 50
Guess is too high.
What is your guess: 25
Guess is too high.
What is your guess: 12
Guess is too high.
What is your guess: 5
Guess is too low.
What is your guess: 6
Congratulations!
You guessed the secret number in 5 guesses!

a found at index 13
a found at index 16
a found at index 28
a found at index 32

Please enter the number of rows for the multiplication table: 12
1 
2 4 
3 6 9 
4 8 12 16 
5 10 15 20 25 
6 12 18 24 30 36 
7 14 21 28 35 42 49 
8 16 24 32 40 48 56 64 
9 18 27 36 45 54 63 72 81 
10 20 30 40 50 60 70 80 90 100 
11 22 33 44 55 66 77 88 99 110 121 
12 24 36 48 60 72 84 96 108 120 132 144 

''' 
