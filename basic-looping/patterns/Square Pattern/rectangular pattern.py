# WAP to print the basic rectangular pattern by the length and breadth as an input from the user

# Coloumn/length= 4 row/width= 3

#    ***
#    ***
#    ***
#    ***

rows=int(input(" Enter the width or row in the desired rectangle  --- Enter here ---->"))
coloumn=int(input(" Enter the length or coloumn in the desired  --- Enter here ---->"))
print()
print("The Rectangle is right below with ite length = ", coloumn , " & width = ", rows )
print()
i=1
while i<=coloumn:
    j=1
    while j<=rows:
        print('*', end='')
        j=j+1
    print()
    i=i+1 
print()
print("Thank You for Choosing us _/\_")  
print() 