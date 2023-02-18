# WAP to print the even natural numbers till the given range

n=int(input("Enter the range for printing even natural numbers-->"))
i=1
print()
print("The even natural numbers Begins now ------ till   ",end='')
print(n)
print()
while i<=n:
    if i%2==0:
        print(i)
    i=i+1

print()
print("THANK YOU")