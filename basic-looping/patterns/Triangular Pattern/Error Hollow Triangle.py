# WAP to print the basic triangular pattern by the side as an input

#    ********
#    ***  ***
#    **    **
#    *      *

n=int(input(" Enter the range for the triangular pattern  --- Enter here ---->"))
print()
print("The Triangular pattern with its base is =", n)
print()
i=n
while i>0:
    j=1
    while j<=i:
        print('*', end='')
        j=j+1
    print()
    i=i-1 
    
print()
print("Thank You for Choosing us _/\_")  
print() 
