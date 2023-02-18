# WAP to print the factorial of the input number

n=int(input("Enter the range till where factorial is to be calculated--- HERE---> "))
i=1
while i<=n:
    j=1
    fac=1
    p=i
    print()
    print("The factorial of ", i , " goes like :")
    print()
    while j<=i:
        print(p," * ",end='')
        fac=fac*j
        p=p-1
        j=j+1
    print(" = ",end='')
    print(fac) 
    i=i+1
print("THANK YOU")   