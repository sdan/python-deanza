import math
# 
# Surya Dantuluri
# CIS 41A Winter 2019
# In-class assignment I
#

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def getArea(self):
        return (math.pi)*(self.radius**2)

class Cylinder(Circle):
    def __init__(self, radius, height):
        super(Cylinder, self).__init__(radius)
        self.height = height
        
    def getVolume(self):
        area = super(Cylinder, self).getArea()
        return self.height*area

bigCircle = Circle(4)
bigCylinder = Cylinder(2,5)


print('Circle area is:',round(bigCircle.getArea(), 2))
print('Cylinder volume is:',round(bigCylinder.getVolume(),2))
