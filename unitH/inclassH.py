# 
# Surya Dantuluri
# CIS 41A Winter 2019
# In-class assignment H
#

class StateData:
    def __init__(self, name, abbreviation, region, population):
        self.name = name
        self.abbreviation = abbreviation
        self.region = region
        self.population = population
        
    def __str__(self):
        return self.name
    
    def displayState(self):
        print(self.name+' ('+self.abbreviation+') is in the '+self.region+' region and has a population of '+str(self.population))
        

Cali = StateData('California', 'CA', 'West', 39250000)

print(Cali.__str__())
Cali.displayState()

class StateData2:
    def __init__(self, name):
        self.name = name
    
    def setRegion(self, region):
        self.region = region
    
    def getRegion(self):
        return self.region    


Cal = StateData2("California")
Cal.setRegion("West")
Cal.pop = 39250000
print(Cal.name)
print(Cal.getRegion())
print(Cal.region)
print(Cal.pop)

class StateData2:

    def __init__(self):
        self.public = "Public"
        self._protected = " Protected"
        self.__private = " Private"

a = StateData2()
print(a.public)
print(a._protected)
print(a._StateData2__private)