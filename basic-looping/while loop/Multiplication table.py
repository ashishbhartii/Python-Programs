# WAP to find the multiplication table of desired number

n=int(input("ENTER the range for multiplication table --HERE-->"))
num=int(input("ENTER the number whose multiplication table is to be calculated --HERE-->"))
print()
print("The Multiplication of ", num ,"goes like below:")
i=1
mul=1
while i<=n:
    print(num ," *  ", end='')
    print(i , " = ", end='')
    mul=num*i
    print(mul)
    i=i+1
print()
print("THANK YOU _/\_")

