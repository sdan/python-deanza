food = {
    'apple':'sauce',
    'peach':'cobbler',
    'carrot':'cake',
    'strawberry':'sorbet',
    'banana':'cream pie'
}
#print(food)
food.update({'mango':'sticky rice'})
food['strawberry'] = 'shortcake'
del food['carrot']
print("apple dessert is:",food['apple'])
print("banana dessert exists:",'banana' in food)
print("pear dessert exists:",'pear' in food)
print(food.keys())
print(food.values())
print(food.items())

capitols1 = {
    'Alabama':'Montgomery',
    'Alaska':'Juneau', 
    'Arizona':'Phoenix', 
    'Arkansas':'Little Rock', 
    'California':'Sacramento'
}
capitols2 = {
    'California':'Sac',
    'Colorado':'Denver',
    'Connecticut':'Hartford'
}

capitols1.update(capitols2)
capitols1 = sorted(capitols1.values())
print("Sorted state capitols:",capitols1)

class1 = set(['Li', 'Audry', 'Jia', 'Migel', 'Tanya'])
class2 = set(['Sasha', 'Migel', 'Tanya', 'Hiroto', 'Audry'])
class1.add('John')
print("Students in both classes:",sorted(class1.intersection(class2)))
print("All students:",sorted(class1.union(class2)))
print("Sasha is in class1:",'Sasha' in class1)
