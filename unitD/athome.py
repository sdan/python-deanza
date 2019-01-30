from collections import namedtuple
''' 
Surya Dantuluri
CIS 41A   Winter 2019 
Unit D take-home assignment
'''

class1 = set(['Li', 'Audry', 'Jia', 'Migel', 'Tanya'])
class2 = set(['Sasha', 'Migel', 'Tanya', 'Hiroto', 'Audry'])
class3 = set(['Migel', 'Zhang', 'Hiroto', 'Anita', 'Jia'])
print("Students in all three classes:",sorted(class1.intersection(class2).intersection(class3)))
print("All students:",sorted(class1.union(class2).union(class3)))
print("Students in class1 but not class2 or class3:",class1.difference(class2.union(class3)))
list = [1,2,3]
list[1], list[2] = list[2], list[1]
print(list)
Casablanca = ("Casablanca", 1942, "romantic drama")
title = casa[0]
year = casa[1]
genre = casa[2]
print("My favorite movie is:",title)
Movie = namedtuple('Movie', 'title year genre')
sometuple = Movie(title="Casablanca", year=1942, genre="romantic drama")
print("My favorite movie is:",sometuple.title)

Moviestars = namedtuple('Moviestars', 'title, year, genre, stars')
favoritemovie = Moviestars(title="Casablanca", year=1942, genre="romantic drama", stars=["Humphrey Bogart", "Ingrid Bergman"])
favoritemovie.stars.append("Claude Rains")
print("My favorite star is:",favoritemovie.stars[1])
print(favoritemovie)




''' 
Execution results: 

Students in all three classes: ['Migel']
All students: ['Anita', 'Audry', 'Hiroto', 'Jia', 'Li', 'Migel', 'Sasha', 'Tanya', 'Zhang']
Students in class1 but not class2 or class3: {'Li'}
[1, 3, 2]
My favorite movie is: Casablanca
My favorite movie is: Casablanca
My favorite star is: Ingrid Bergman
Moviestars(title='Casablanca', year=1942, genre='romantic drama', stars=['Humphrey Bogart', 'Ingrid Bergman', 'Claude Rains'])

''' 