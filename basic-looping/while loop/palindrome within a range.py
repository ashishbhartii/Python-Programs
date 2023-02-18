# WAP to check whethera number is palindrome or not.

n1=int(input("Enter the starting to be checked for PALINDROME--- HERE---> "))
n2=int(input("Enter the terminating to be checked for PALINDROME--- HERE---> "))
i=n1
while i<=n2:

    temp=i
    x=i
    r=0
    c=0
    print()
    while x>0:
        r=x%10
        c=(c*10)+r
        x=x//10


    if c==temp:
        print("The entered word ",end='')
        print(temp,end='')
        print(" is PALINDROME")
#    else:
#         print("The entered word ",end='')
#         print(temp,end='')
#         print("is NOT PALINDROME")
    i=i+1

print()
print("THANK YOU FOR CHOOSING US _/\_")