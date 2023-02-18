# WAP to print the factorial of the input number

n=int(input("Enter the number whose factorial is to be calculated--- HERE---> "))
i=1
fac=1
p=n
print("The factorial of ", n, " goes like :")
print()
while i<=n:
    print(p," * ",end='')
    fac=fac*i
    p=p-1
    i=i+1
print(" = ",end='')
print(fac) 
print("THANK YOU")   