# WAP to check whether a number is PRIME or NOT

n=int(input("Enter the number to be validated for prime -->"))
i=1
print()
c=0
while i<=n:
    if n%i==0:
        c=c+1
    i=i+1
if c==2:
    print (n,end='')
    print ("  is PRIME ")
else:
    print(n,end='')
    print ("  is not PRIME ")
print()
print("THANK YOU")