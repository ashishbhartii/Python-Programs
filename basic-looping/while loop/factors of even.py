# WAP to print all the factors of even number within a given range

n=int(input("Enter the range for even numbers-->"))
print()
i=1
while i<=n:
    if i%2==0:
        j=1
        print(i ," is an even number whose factors are   ", end='')
        while j<=i:
            if i%j==0:
                print(j," ", end='')
            j=j+1
    print()
    i=i+1

print()

print("THANK YOU")