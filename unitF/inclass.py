def main():
    hello()
    help(hello)
    print(hello.__doc__)

def hello():
    """This function prints Hello World"""
    print("Hello world")


def printListElement(list,index):
    try:
        print(list[index])
    except:
        print("Error: bad index number.")
myList = [0,1,2]
printListElement(myList,3)
        


    
myInt = 3
myList = [0,1,2]
print("Original ID of myInt in main is",id(myInt))
print("Original ID of myList in main is",id(myList))
print("Original ID of myList's last element in main is",id(myList[2]))

def byVal(value):
    print("Original ID of parameter in byVal",id(value))
    value+=7
    print("ID of parameter in byVal after change",id(value))
    
def byRef(value):
    print("Original ID of parameter in byRef",id(value))
    print("Original ID of parameter's last element in byRef",id(value[-1]))
    value[-1]+=7
    print("ID of parameter in byRef after change",id(value))
    print("ID of parameter's last element in byRef after change",id(value[-1]))
    

byVal(myInt)
byRef(myList)
print("ID of myInt in main after call to byVal is",id(myInt))
print("ID of myList in main after call to byRef is",id(myList))
print("ID of myList's last element in main after call to byRef is",id(myList[-1]))
print("myInt is now:",myInt)
print("myList is now:",myList)

if __name__ == "__main__":
    main()

'''
    Hello world
    Help on function hello in module __main__:
    
    hello()
    This function prints Hello World
    

Error: bad index number.

Original ID of myInt in main is 4420023712
Original ID of myList in main is 4455433800
Original ID of myList's last element in main is 4420023680
Original ID of parameter in byVal 4420023712
ID of parameter in byVal after change 4420023936
ID of myInt in main after call to byVal is 4420023712
Original ID of parameter in byRef 4455433800
Original ID of parameter's last element in byRef 4420023680
ID of parameter in byRef after change 4455433800
ID of parameter's last element in byRef after change 4420023904
ID of myList in main after call to byRef is 4455433800
ID of myList's last element in main after call to byRef is 4420023904
myInt is now: 3
myList is now: [0, 1, 9]
'''

