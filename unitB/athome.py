''' 
Surya Dantuluri
CIS 41A   Winter 2019 
Unit B take-home assignment
'''

# First Script
string = input("Enter input:")
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

qsbeads = int(input("Enter number of small beads:"))
qmbeads = int(input("Enter number of medium beads:"))
qlbeads = int(input("Enter number of large beads:"))

tsbeads = SBEADS*qsbeads
tmbeads = MBEADS*qmbeads
tlbeads = LBEADS*qlbeads
total = tsbeads+tmbeads+tlbeads

print("SIZE       QTY   COST PER BOX      TOTALS")
print(f"Small       {qsbeads}           {SBEADS:.2f}       {tsbeads:.2f}")
print(f"Medium      {qmbeads}            {MBEADS:.2f}       {tmbeads:.2f}")
print(f"Large       {qlbeads}            {LBEADS:.2f}       {tlbeads:.2f}")
print(f"TOTAL                              {total:.2f}") 

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

Enter number of small beads:10
Enter number of medium beads:9
Enter number of large beads:8
SIZE       QTY   COST PER BOX      TOTALS
Small       10           9.20       92.00
Medium      9            8.52       76.68
Large       8            7.98       63.84
TOTAL                              232.52
''' 