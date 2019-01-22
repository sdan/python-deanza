import copy
''' 
Surya Dantuluri
CIS 41A   Winter 2019 
Unit C take-home assignment
'''

# First Script
list1 = []
list1.extend((1,3,5))

list2 = [1,2,3,4]

list3 = list1+list2
print(list3)

print(3 in list3)
print(list3.count(3))
print(list3.index(3))
first3 = list3.pop(list3.index(3))
print(first3)
list4 = copy.deepcopy(list3)
list4.sort()

print(list3)
print(list4)

list5 = [list1,list2]
print(list5)
print(list5[1][3])


# Second Script
a = 9
b = 14

print("b) binary of a =",bin(a))
print("b) binary of b =",bin(b))
print("c) binary of a & b =",bin(a&b))
print("d) binary of a | b =",bin(a|b))

''' 
Execution results: 
[1, 3, 5, 1, 2, 3, 4]
True
2
1
3
[1, 5, 1, 2, 3, 4]
[1, 1, 2, 3, 4, 5]
[[1, 3, 5], [1, 2, 3, 4]]
4

b) binary of a = 0b1001
b) binary of b = 0b1110
c) binary of a & b = 0b1000
d) binary of a | b = 0b1111
''' 