import copy

list1 = [2,4.1,'hello']
list2 = copy.copy(list1)
list3 = copy.deepcopy(list1)

print("list1 == list2:",list1==list2)
print("list1 == list3:",list1==list3)
print("list2 == list3:",list2==list3)

print("list1 is list2:",list2 is list3)
print("list1 is list3:",list2 is list3)
print("list2 is list3:",list2 is list3)

print("list1 ID:",id(list1))
print("list2 ID:",id(list2))
print("list3 ID:",id(list3))

list1.append(8)
list2.insert(1, 'goodbye')
del list3[0]

print(list1)
print(list2)
print(list3)