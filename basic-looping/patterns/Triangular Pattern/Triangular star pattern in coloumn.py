# WAP to print the trainagular pattern 

#  1
#  2*
#  3*4
#  4*5*
print()
n= int(input("Enter the no of rows you wish in your Questioned TRIANGULAR Pattern --- HERE--->"))
print()
i=1
while i<=n:
    j=1
    p=i
    while j<=i:
        if j%2!=0:
         print(p,end='')
         p=p+1
        else:
         print('*',end='')
         p=p+1
           

        j=j+1
    print()
    i=i+1
print()
print("THANK YOU for Choosing us _/\_")
print()        