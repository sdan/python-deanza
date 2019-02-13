height = height//2 #in: 24, o:12, in:7, o:3, in:7.3, o:3.0
3.14159 rounded to 4 decimal places = round(3.14159,4))
186282 rounded to the nearest hundred = round(186282,-2))
Minimum of 6, -9, -3, 0 = min(6,-9,-3,0))
number = 2.321, float = 2.312
string.isupper() Enter input:ABC123: True
string.isdigit() False
string.isalpha() False
"And now for something completely different"[:7][38:][14:16][::2][::-1]
And now, rent, me, Adnwfrsmtigcmltl ifrn, tnereffid yletelpmoc gnihtemos rof won dnA
print(f"Small       {qsbeads}           {SBEADS:.2f}       {tsbeads:.2f}")
print("{0:<10}{1:>2}{2:>15.2f}{3:>11.2f}".format("Medium", qmbeads, MBEADS, tmbeads))
Medium     9           8.52      76.68
print("{0:<32}{1:.2f}".format("TOTAL", total))
TOTAL                           232.52
print("{0:<9}{1:<6}{2:<17}{3:<5}".format("SIZE", "QTY", "COST PER BOX", "TOTALS"))
SIZE     QTY   COST PER BOX     TOTALS
"Believe you can and you're halfway there."

# First Script
string = input("Enter input: ")
print(string.isupper())
print(string.isdigit())
print(string.isalpha())
var = "Type, type, type away.\nCompile. Run. Hip hip hooray!\nNo error today!"
print(var)
quote = "And now for something completely different"
print(quote[:7])
print(quote[38:])
print(quote[14:16])
print(quote[::2])
print(quote[::-1])
pattern1 = ".~*'"
pattern2 = pattern1+pattern1[::-1]
print(pattern2 * 5)
# Second Script
SBEADS = 9.20
MBEADS = 8.52
LBEADS = 7.98
qsbeads = int(input("Enter number of small beads: "))
qmbeads = int(input("Enter number of medium beads: "))
qlbeads = int(input("Enter number of large beads: "))
tsbeads = SBEADS*qsbeads
tmbeads = MBEADS*qmbeads
tlbeads = LBEADS*qlbeads
total = tsbeads+tmbeads+tlbeads
print("{0:<9}{1:<6}{2:<17}{3:<5}".format("SIZE", "QTY", "COST PER BOX", "TOTALS"))
print("{0:<10}{1:>2}{2:>15.2f}{3:>11.2f}".format("Small", qsbeads, SBEADS, tsbeads))
print("{0:<10}{1:>2}{2:>15.2f}{3:>11.2f}".format("Medium", qmbeads, MBEADS, tmbeads))
print("{0:<10}{1:>2}{2:>15.2f}{3:>11.2f}".format("Large", qlbeads, LBEADS, tlbeads))
print("{0:<32}{1:.2f}".format("TOTAL", total))
'''
    Execution results:
    
    Enter input: ABC123
    True
    False
    False
    Type, type, type away.
    Compile. Run. Hip hip hooray!
    No error today!
    And now
    rent
    me
    Adnwfrsmtigcmltl ifrn
    tnereffid yletelpmoc gnihtemos rof won dnA
    .~*''*~..~*''*~..~*''*~..~*''*~..~*''*~.
    Enter number of small beads: 10
    Enter number of medium beads: 9
    Enter number of large beads: 8
    SIZE     QTY   COST PER BOX     TOTALS
    Small     10           9.20      92.00
    Medium     9           8.52      76.68
    Large      8           7.98      63.84
    TOTAL                           232.52
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

