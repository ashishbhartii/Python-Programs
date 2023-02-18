# Write a program to find the fibonacci series till the nth term.

n=int(input("Enter the term range for fibonacci series-->"))
print()
i=1
a=0
b=1
c=0
print(0," ",end='')
print(1," ",end='')
while i<=n:
    c=a+b
    print(c," ",end='')
    a=b
    b=c 
    i=i+1
print()
