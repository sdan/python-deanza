''' 
Surya Dantuluri
CIS 41A   Fall 2018 
Unit A take-home assignment 
'''

import math

# Basic math and string operations
print("3^2.5 =", 3**(2.5))

b = 2
b+=3
print("2+3 =",b)

c = 12
c/=4
print("12/4 =",c)

d = 5%3
print("Remainder of 5 divided by 3 =",d)

# Built-in functions abs, round, and min
print("Absolute value of 5-7 =",abs(5-7))

print ("3.14159 rounded to 4 decimal places =",round(3.14159,4))

print("186282 rounded to the nearest hundred =",round(186282,-2))

print("Minimum of 6, -9, -3, 0 =", min(6,-9,-3,0))

# Functions from the math module
number = float(input("Enter in a number: "))

# Print square root of inputted variable rounded to 2 decimal places
print("Square root of the number, rounded to two decimal places =",round(math.sqrt(number),2))

# Print base-10 logarithm of inputted variable rounded to 2 decimal places
print("Base-10 log of the number, rounded to two decimal places =",round(math.log10(number),2))

# Complex numbers
z1 = 4+3j
z2 = 2+2j
z3 = z1*z2
print("Product of 4+3j and 2+2j is =",z3)



''' 
Execution results: 
3^2.5 = 15.588457268119896
2+3 = 5
12/4 = 3.0
5 mod 3 = 2
Absolute value of 5-7 = 2
3.14159 rounded to 4 decimal places = 3.1416
186282 rounded to the nearest hundred = 186300
Minimum of 6, -9, -3, 0 = -9
Enter in a number: 7.6
Square root of the number, rounded to two decimal places = 2.76
Base-10 log of the number, rounded to two decimal places = 0.88
Product of 4+3j and 2+2j is = (2+14j)
''' 
