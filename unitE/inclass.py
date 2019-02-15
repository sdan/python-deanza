#Script 1

scifi = ['Alien','Solaris','Inception','Moon']
comedy = ['Borat','Idiocracy','Superbad','Bridesmaids']
inputMove = input("Please enter a movie title:")
if(inputMove in scifi):
    print(inputMove,"is a scifi movie.")
elif(inputMove in comedy):
    print(inputMove,"is a comedy movie.")
else:
    print("Sorry, I don't know what kind of movie",inputMove,"is.")

#Script 2

for x in range(10,-1,-2):
    print(x)

movies = {
    "The Wizard of Oz":1939,
    "The Godfather":1972,
    "Lawrence of Arabia":1962,
    "Raging Bull":1980
}
for name, year in sorted(movies.items()):
    print(name,"was made in",year)

