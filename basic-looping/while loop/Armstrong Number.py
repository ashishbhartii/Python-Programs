# WAP to check whether a number is Armstrong number or not

n=int(input("Enter the number to be checked for Armstrong  -> "))
temp=n
num=n
c=0
r=0
r1=0
arm=0
while n>0:
    r=n%10
    c=c+1
    n=n//10

while num>0:
    r1=num%10
    arm=arm+(r1**c)
    num=num//10
    

if arm==temp:
    print(temp," is an ",end='')
    print("ARMGSTRONG Number")
else:
    print(temp," is not an ",end='')
    print("NOT AN ARMGSTRONG Number")

