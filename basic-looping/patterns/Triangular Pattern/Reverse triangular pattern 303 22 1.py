# WAP to print the trainagular pattern 

#  4004
#  303
#  22
#  1
print()
n= int(input("Enter the no of rows you wish in your Questioned TRIANGULAR Pattern --- HERE--->"))
print()
i=n
while i>0:
    j=1
    while j<=i:
        if j==1 or j==i:
            print(i,end='')
        else:
            print(0,end='')

        j=j+1
    print()
    i=i-1
print()
print("THANK YOU for Choosing us _/\_")
print()        