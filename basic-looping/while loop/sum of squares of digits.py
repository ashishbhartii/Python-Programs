# WAP to find the SUM of squares of Digits.

n=int(input("Enter the number whose digit's squares and later its sum is to be calculated--- HERE---> "))
count=0
r=0
while n>0:
    r=n%10
    print(r,"^2  + ", end='')
    count=count+(r*r)
    n=n//10
print(" = ",end='')
print(count)
print()