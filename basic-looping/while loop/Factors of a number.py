# WAP to print all the factors of the given number

n=int(input("Enter the number whose factor is to be known-->"))
print()
i=1
while i<=n:
    if n%i==0:
        print(i," ", end='')
    i=i+1

print()

print("THANK YOU")