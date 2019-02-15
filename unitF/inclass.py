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
