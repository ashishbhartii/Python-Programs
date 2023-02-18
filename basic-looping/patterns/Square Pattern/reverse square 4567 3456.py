# WAP to print the reverse square pattern 

#    4567
#    3456
#    2345
#    1234
print()

n=int(input("Enter the length/range of the reverse square  pattern --- Enter here ---->"))
print()
print("The reversed square pattern is right below with its range =", n)
print()
i=n
while i>0:
    j=n
    c=i
    while j>0:
        print( c, end='')
        c=c+1
        j=j-1
    print()
    i=i-1 
print()
print("Thank You for Choosing us _/\_")  
print() 
