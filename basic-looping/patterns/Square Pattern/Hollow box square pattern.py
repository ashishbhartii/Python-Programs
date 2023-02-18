# WAP to print the Hollow Box square pattern by the side as an input

#    ****
#    *  *
#    *  *
#    ****
print()
n=int(input("Enter the length as the side pf the Hollow Boxsquare  --- Enter here ---->"))
print()
print("The square is right below with ite length =", n)
print()
i=1
while i<=n:
    j=1
    while j<=n:
        if i==1 or i==n:
            print("*",end='')
        elif j==1 or j==n:
            print("*",end='')    
        else:
            print(' ',end='')
        j=j+1    
    print()
    i=i+1 

print()
print("Thank You for Choosing us _/\_")  
print() 
