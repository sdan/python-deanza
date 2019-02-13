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
print("d) list3 is:",list3)
print("e) list3 contains a 3:",3 in list3)
print("f) list3 contains {0} 3s".format(list3.count(3)))
print("g) The index of the first 3 contained in list3 is",list3.index(3))
first3 = list3.pop(list3.index(3))
print("h) first3 =",first3)
list4 = copy.deepcopy(list3)
list4.sort()
print("j) list3 is now:",list3)
print("j) list4 is:",list4)
print("k) Slice of list3 is:",list3[2:5])
print("l) Length of list3 is:",len(list3))
print("m) The max value in list3 is",max(list3))
print("n) Sorted list3 is:",sorted(list3))
list5 = [list1,list2]
print("o) list5 is:",list5)
print("p) Value 4 from list5:",list5[1][3])

# Second Script
a = 9
b = 14
print("b) binary of a =",bin(a))
print("b) binary of b =",bin(b))
print("c) binary of a & b =",bin(a&b))
print("d) binary of a | b =",bin(a|b))

''' 
Execution results:

d) list3 is: [1, 3, 5, 1, 2, 3, 4]
e) list3 contains a 3: True
f) list3 contains 2 3s
g) The index of the first 3 contained in list3 is 1
h) first3 = 3
j) list3 is now: [1, 5, 1, 2, 3, 4]
j) list4 is: [1, 1, 2, 3, 4, 5]
k) Slice of list3 is: [1, 2, 3]
l) Length of list3 is: 6
m) The max value in list3 is 5
n) Sorted list3 is: [1, 1, 2, 3, 4, 5]
o) list5 is: [[1, 3, 5], [1, 2, 3, 4]]
p) Value 4 from list5: 4


b) binary of a = 0b1001
b) binary of b = 0b1110
c) binary of a & b = 0b1000
d) binary of a | b = 0b1111
''' 
