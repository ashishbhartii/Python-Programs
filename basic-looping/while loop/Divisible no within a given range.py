# WAP to print all the multiple of a given number within a given range.

n1=int(input("Enter the START range for printing even natural numbers-->"))
n2=int(input("Enter the TERMINATING range for printing even natural numbers-->"))
print()
n3=int(input("Enter the number whose multiples are to be extracted -->"))
i=n1
print()
print("  START POINT  ",end='')
print(n1,end="")
print("  END POINT  ",end='')
print(n2)
print()
while i<=n2:
    if i%n3==0:
        print(i," " ,end='')
    i=i+1

print()
print("THANK YOU")