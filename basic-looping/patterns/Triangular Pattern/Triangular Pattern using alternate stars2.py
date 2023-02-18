# WAP to print the trainagular pattern 

#  1
#  **
#  123
#  ****
print()
n= int(input("Enter the no of rows you wish in your Questioned TRIANGULAR Pattern --- HERE--->"))
print()
i=1
while i<=n:
    j=1
    while j<=i:
        if i%2!=0:
         print(j,end='')
        else:
         print('*',end='')
        j=j+1
    print()
    i=i+1
print()
print("THANK YOU for Choosing us _/\_")
print()        