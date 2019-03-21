import random
''' 
Surya Dantuluri
CIS 41A  Winter 2019 
Unit J take-home assignment 
'''
sim=0
simulations = []

for x in range(0,10000):
	prize=0
	sim = random.randint(1, 6)
	while(sim in range(4,7)):
		prize = prize+sim
		sim = random.randint(1, 6)
	simulations.append(prize)

max = 0
sum = 0

for number in simulations:
	if(number>max):
		max = number
	sum+=number

print("Average amount won =",(sum/len(simulations)))
print("Max amount won =",max)

'''
Execution results:

Average amount won = 5.0181
Max amount won = 61

Just as a thought experiment, would you pay $3 for a chance to play this game?
No I wouldn't since I don't like the odds of gambling.
'''