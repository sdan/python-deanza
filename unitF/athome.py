''' 
Surya Dantuluri
CIS 41A   Winter 2019 
Unit F take-home assignment 
'''

def main():
    invoice(20,4,shipping=8)
    invoice(15,3,handling=15)
    printGroupMembers("Group A", "Li", "Audry", "Jia") 
    groupB = ["Group B", "Sasha", "Migel", "Tanya", "Hiroto"] 
    printGroupMembers(*groupB)
    raggedTable = buildBell(7)
    printBell(raggedTable)
    
def invoice(unitPrice, quantity, shipping=10, handling=5):
    print("Cost (unitPrice x quantity)",unitPrice*quantity)
    print("Shipping =",shipping)
    print("Handling =",handling)
    print("Total =",unitPrice*quantity+shipping+handling)
    print()

def printGroupMembers(name,*args):
    print("Members of ",name)
    print(*args,sep="\n")
    
def buildBell(rows):
    bell = [[1]*(rows+1) for _ in range(rows+1)]
    for i in range(1, rows+1):
        bell[i][0] = bell[i-1][i-1]
        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
    return bell

def printBell(raggedTable):
    for i in range(len(raggedTable)):
        for j in range(0, i+1):
            rjustString = str(raggedTable[i][j])
            print(rjustString.rjust(5), end='')
        print('\n') 
 
    
if __name__ == "__main__":
    main()

'''
Execution results: 

Cost (unitPrice x quantity) 80
Shipping = 8
Handling = 5
Total = 93

Cost (unitPrice x quantity) 45
Shipping = 10
Handling = 15
Total = 70

Members of  Group A
Li
Audry
Jia
Members of  Group B
Sasha
Migel
Tanya
Hiroto
    1

    1    2

    2    3    5

    5    7   10   15

   15   20   27   37   52

   52   67   87  114  151  203

  203  255  322  409  523  674  877

  877 1080 1335 1657 2066 2589 3263 4140
'''
