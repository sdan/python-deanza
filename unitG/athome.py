''' 
Surya Dantuluri
CIS 41A   Winter 2019 
Unit G take-home assignment 
'''


def findPopulation(just):
    return int(''.join(i for i in just if i.isdigit()))

file = open("States.txt", "r") 
cool = []
for line in file:
    if("Midwest" in line):
        cool.append(line)
cool.sort(reverse=True,key=findPopulation)
print("Highest population state in the Midwest is:",cool[0])

def findLengthofList(someList):
    return len(someList)
file = open("USPresidents.txt", "r")
dict = {}
for line in file:
    data = line.split()
    state = data[0]
    president = data[1]
    if(state not in dict):
        dict[state] = [president]
    else:
        dict[state].append(president)

most = 0
mostPresidents = 0
for key, value in dict.items():
    if(len(value)>most):
        most = len(value)
        mostPresidents = key
        
print("The state with the most presidents is ",mostPresidents," with",most,"presidents:")
for items in dict[mostPresidents]:
      print(items)

popStates = {'CA', 'TX', 'FL', 'NY', 'IL', 'PA', 'OH', 'GA', 'NC', 'MI'}

print(len(popStates.intersection(dict)),"of the",len(popStates)," high population states have had presidents born in them:")
for key, value in sorted(dict.items()):
    if(key in popStates.intersection(dict)):
        print(key,len(value))



''' 
Execution results: 

Highest population state in the Midwest is: IL Midwest 12802000

The state with the most presidents is  VA  with 8 presidents:
George_Washington
James_Madison
James_Monroe
John_Tyler
Thomas_Jefferson
William_Henry_Harrison
Woodrow_Wilson
Zachary_Taylor
8 of the 10  high population states have had presidents born in them:
CA 1
GA 1
IL 1
NC 2
NY 5
OH 7
PA 1
TX 2

''' 
