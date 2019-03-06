''' 
Surya Dantuluri
CIS 41A   Winter 2019 
Unit H take-home assignment
'''

    
class BritCoins:
    __coinValues = {"pound":240, "shilling":12, "penny":1} #value of each type of coin in pennies 
    
    def __init__(self, **kwargs):
        self.totalPennies =0
        for key in kwargs:
            self.totalPennies+=kwargs[key] * BritCoins.__coinValues[key]
    def __add__(self,other):
        add = self.totalPennies+other.totalPennies
        return BritCoins(penny = add)
    def __sub__(self,other):
        sub = self.totalPennies-other.totalPennies
        return BritCoins(penny = sub)       
    def __str__(self):
        pounds = self.totalPennies// 240
        shillings = (self.totalPennies- (pounds *240))//12
        pennies = self.totalPennies - (pounds *240) - (shillings*12)
        return str(pounds) +" pounds " +str(shillings) + " shillings " + str(pennies) + " pennies "
    




#Part 2
def main2():
    uspres2()
    
def uspres2():
    presCount = {}
    file = open("USPresidents.txt","r")
    line = file.readline() 
    while line != "" :    
        space = line.split()
        if space[0] in presCount:
            presCount[space[0]] += 1
        else:
            presCount[space[0]] = 1
        line = file.readline()  
        
    topTen = {"CA", "TX", "FL", "NY", "IL", "PA", "OH", "GA", "NC", "MI"}
    
    topBorn = set(topTen & presCount.keys())
    
    print (len(topBorn), "of the", len(topTen), "high population states have had presidents born in them:")
    for elm in sorted(topBorn):
        print (elm, presCount[elm])   
    

#Part 3
def firstScript():
    Message1 = {'temperature':550}
    Message2 = {'temperature':475}
    Message3 = {'temperature':450, 'miscError': 404}
    Message4 = {'CO2level':.18}
    Message5 = {'CO2level':.2, 'miscError':503}  
    overseerSystem(**Message1)
    overseerSystem(**Message2)
    overseerSystem(**Message3)
    overseerSystem(**Message4)
    overseerSystem(**Message5)
    
def overseerSystem(**kwargs):
    if 'temperature' in kwargs:
        if kwargs['temperature'] > 500:
            print("Warning: Temperature is", kwargs['temperature'])
    if 'CO2level' in kwargs:
        if kwargs['CO2level'] > 0.15:
            print("Warning: CO2 level is", kwargs['CO2level'])
    if 'miscError' in kwargs:
        print("miscError #", kwargs['miscError'])
    



if __name__ == '__main__':
    firstScript()

    c1 = BritCoins(pound= 4, shilling=24 , penny= 3)
    c2 = BritCoins(pound=3, shilling=4, penny= 5)
    c3 = c1.__add__(c2)
    c4 = c1.__sub__(c2)
    print(c1)
    print(c2)
    print(c3)
    print(c4) 
    
''' 
Execution results:

The state with the most presidents is VA with 8 presidents:
George_Washington
James_Madison
James_Monroe
John_Tyler
Thomas_Jefferson
William_Henry_Harrison
Woodrow_Wilson
Zachary_Taylor

8 of the 10 high population states have had presidents born in them:
CA 1
GA 1
IL 1
NC 2
NY 5
OH 7
PA 1
TX 2

Warning: Temperature is 550
miscError # 404
Warning: CO2 level is 0.18
Warning: CO2 level is 0.2
miscError # 503
'''
