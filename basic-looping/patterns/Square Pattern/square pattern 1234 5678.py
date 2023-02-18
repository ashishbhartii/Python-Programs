# WAP to print the basic square pattern 

#    1234
#    5678
#    891011
#    12131415

n=int(input(" Enter the length/range of the square  pattern --- Enter here ---->"))
print()
print("The square is right below with its range =", n)
print()
i=1
c=1
while i<=n:
    j=1
    while j<=n:
        print( c, end='')
        c=c+1
        j=j+1
    print()
    i=i+1 
print()
print("Thank You for Choosing us _/\_")  
print() 
