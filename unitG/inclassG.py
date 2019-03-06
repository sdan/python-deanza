# 
# Surya Dantuluri
# CIS 41A Winter 2019
# In-class assignment G
#

#Part 1
file = open("ZenOfPython.txt", "w+")
file.write("Beautiful is better than ugly."+'\n'+"Explicit is better than implicit."+'\n')
file.close()
file = open("ZenOfPython.txt", "a")
file.write("Readability counts."+'\n'+"If the implementation is hard to explain, it's a bad idea.")
file.close()
file = open("ZenOfPython.txt", "r")

line = file.readline()
while line != "":
	print(line.rstrip('\n'))
	line = file.readline()
print()
file.close()

#Part 2
d = {}
with open("Cities.csv") as f:
	for line in f:
		# someList = line.split(',')
		# print(someList)
		# print(len(someList))
		# cities = someList[0]
		# state = someList[1]
		# pop = someList[2]
		cities, state, pop = line.split(',')
		info = (cities, state)
		d[info] = pop

for key, value in d.items():
	print(key[0],key[1],value)


inputCity = input("Please enter a city:")
inputState = input("Please enter a state:")
inputTuple = (inputCity, inputState)

print(inputCity,inputState,"has a population of",d[inputTuple])
