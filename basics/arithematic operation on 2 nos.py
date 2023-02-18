# WAP to print to proceed with arethematic operation on two numbers

n1= int(input("Enter the first number ->"))
n2= int(input("Enter the first number ->"))

sum= n1+n2
if n1>n2:
    diff=n1-n2
else:
    diff=n2-n1

mul=n1*n2
if n1>n2:
    div=n1/n2
else:
    div=n2/n1

if n1>n2:
    rem=n1%n2
else:
    rem=n2%n1


print("the sum of sum numbers are " )
print(sum)
print("the difference of sum numbers are " )
print(diff)
print("the multiplication of sum numbers are " )
print(mul)
print("the division of sum numbers are " )
print(div)
print("the sum of remainder numbers are " )
print(rem)