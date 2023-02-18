# WAP to print the sum of even & Odd natural numbers till the given range sperately

n=int(input("Enter the range for printing even natural numbers-->"))
i=1
print()
print("The sum of even & odd natural numbers Begins now ------ till   ",end='')
print(n)
ev=0
od=0
print()
while i<=n:
    if i%2==0:
        ev=ev+i
    else:
        od=od+i
    i=i+1

print()
print(ev,"<-- is the sum of even natural numbers")
print(od,"<-- is the sum of odd natural numbers")
print("THANK YOU")