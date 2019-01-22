''' 
Surya Dantuluri
CIS 41A   Winter 2019 
Unit B take-home assignment
'''

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
Enter number of small beads: 5
Enter number of medium beads: 10
Enter number of large beads: 15
SIZE     QTY   COST PER BOX     TOTALS
Small      5           9.20      46.00
Medium    10           8.52      85.20
Large     15           7.98     119.70
TOTAL                           250.90
'''
