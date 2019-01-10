name = (str(input("Enter your name")))
print(name.upper())
print(len(name)-1)
print(name[3])

name2 = name.replace("o", "x")
print(name2)
print(name)






quote = "Believe you can and you're halfway there."
print(quote.count('a'))

first_instance = quote.find("a")
print(first_instance)

second_instance = quote.find("a", first_instance+1)
print(second_instance)

third_instance = quote.find("a", second_instance+1)
print(third_instance)

fourth_instance = quote.find("a", third_instance+1)
print(fourth_instance)