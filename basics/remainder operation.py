# WAP to perform remainder operation.

n1= int(input("Enter the first number ->"))
n2= int(input("Enter the second number ->"))
print()
if n1>n2:
    rem =n1%n2
    print("The remainder when n1 % n2 is-->", end='')
    print(rem)
else:
    rem =n2%n1
    print("The remainder when n2 % n1 is-->", end='')
    print(rem)    
