# WAP to check whethera number is palindrome or not.

n=int(input("Enter the number to be chevked for PALINDROME--- HERE---> "))
temp=n
r=0
c=0
print()
while n>0:
    r=n%10
    c=(c*10)+r
    n=n//10


if c==temp:
    print("The entered word ",end='')
    print(temp,end='')
    print(" is PALINDROME")
else:
    print("The entered word ",end='')
    print(temp,end='')
    print("is NOT PALINDROME")

print()
print("THANK YOU FOR CHOOSING US _/\_")