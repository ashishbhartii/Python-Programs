# WAP to print the basic square pattern (multiplication table)

#    1234
#    2468
#    36912
#    481216

n=int(input(" Enter the length/range of the square  pattern --- Enter here ---->"))
print()
print("The square is right below with its range =", n)
print()
i=1
while i<=n:
    j=1
    c=i
    while j<=n:
        print( c*j, end='')
        j=j+1
    print()
    i=i+1 
print()
print("Thank You for Choosing us _/\_")  
print() 
