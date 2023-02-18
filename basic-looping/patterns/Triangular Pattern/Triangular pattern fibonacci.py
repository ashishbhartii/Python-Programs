# WAP to print the trainagular pattern 

#  0
#  11
#  235
#  8132134
print()
n= int(input("Enter the no of rows you wish in your Questioned TRIANGULAR Pattern --- HERE--->"))
print()
i=2
a=0
b=1
c=0
print(0)
while i<=n:
    j=1
    
    while j<=i:
        c=a+b
        print(c,end='')
        a=b
        b=c
        j=j+1
    print()
    i=i+1
print()
print("THANK YOU for Choosing us _/\_")
print()        