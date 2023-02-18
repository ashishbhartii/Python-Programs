# WAP to print the sum of even natural numbers till the given range

n=int(input("Enter the range for printing even natural numbers-->"))
i=1
print()
print("The even natural numbers Begins now ------ till   ",end='')
print(n)
sum=0
print()
while i<=n:
    if i%2==0:
        sum=sum+i
    i=i+1

print()
print(sum,"<-- is the sum of even natural numbers")
print("THANK YOU")