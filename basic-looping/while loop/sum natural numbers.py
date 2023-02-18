# WAP to print the sum of natural numbers till the given range

n=int(input("Enter the range for printing natural numbers-->"))
i=1
print()
print("The even natural numbers Begins now ------ till   ",end='')
print(n)
sum=0
print()
while i<=n:
    
    sum=sum+i
    i=i+1

print()
print(sum,"<-- is the sum of even natural numbers")
print("THANK YOU")