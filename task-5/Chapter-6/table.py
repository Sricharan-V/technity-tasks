#Table Printer

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(list):
    sorted=[]
    
    for i in range (len(list)):
        strlen= []
        
        for j in range (len(list[i])):
            a=len(list[i][j])
            strlen.append(a)
            strlen.sort(reverse=True)
       
        
        (sorted.append(strlen[0]))
    print(sorted)

    for t in range(len(list[1])):
        for ele in range(len(list)):
            print(list[ele][t].rjust(sorted[ele]), end=" ")
        print()
            
printTable(tableData)