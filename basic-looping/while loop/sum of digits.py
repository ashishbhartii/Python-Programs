# WAP to find the SUM of Digits.

n=int(input("Enter the number whose didhit sum is to be calculated--- HERE---> "))
count=0
r=0
while n>0:
    r=n%10
    print(r," + ", end='')
    count=count+r
    n=n//10
print(" = ",end='')
print(count)
print()