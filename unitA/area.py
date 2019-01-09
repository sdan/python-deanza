'''
Surya Dantuluri
CIS 41A   Winer 2019 
Unit A in-class assignment 
'''

height = float(input("height: "))
width = float(input("width: "))
area = height*width #computes area of width and height

print("\n")

print(f"height: {height}")
print(f"width:  {width}")
print(f"area:   {area}")

print("\n")

height = height//2 #uses floor division to divide height in half
width = width//2 #uses floor division to divide width in half
area = height*width #computes area after floor division of height and width by 2

print(f"height: {height}")
print(f"width:  {width}")
print(f"area:   {area}")
