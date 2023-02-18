# WAP to print the Hollow Box square pattern by the side as an input

#    ********
#    **    **
#    * *  * *
#    *  **  *
#    * *  * *  
#    **    **  
#    ********
#   
print()
n=int(input("Enter the length as the side pf the Hollow X Boxsquare  --- Enter here ---->"))
print()
print("The square is right below with ite length =", n)
print()
i=1
c=1
p=1
while i<=n:
    j=1
    while j<=n:
        p=n-c
        if i==1 or i==n or j==1 or j==n or i==j or j==p:
            print("*",end='')   
        else:
            print(' ',end='')
        c=c+1    
        j=j+1    
    print()
    i=i+1 

print()
print("Thank You for Choosing us _/\_")  
print() 
