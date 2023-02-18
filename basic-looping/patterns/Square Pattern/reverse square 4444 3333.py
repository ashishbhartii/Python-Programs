# WAP to print the reverse square pattern 

#    4444
#    3333
#    2222
#    1111

n=int(input("Enter the length/range of the reverse square  pattern --- Enter here ---->"))
print()
print("The reversed square pattern is right below with its range =", n)
print()
i=n
while i>0:
    j=1
    while j<=n:
        print( i, end='')
        j=j+1
    print()
    i=i-1 
print()
print("Thank You for Choosing us _/\_")  
print() 
