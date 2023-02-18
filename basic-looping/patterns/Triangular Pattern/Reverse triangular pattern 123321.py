# WAP to print the trainagular pattern 

#  123454321
#  1234321
#  12321
#  121
print()
n= int(input("Enter the no of rows you wish in your Questioned TRIANGULAR Pattern --- HERE--->"))
print()
i=n
while i>0:
    j=1
    while j<=i:
        print(j,end='')
        j=j+1
    p=j    
    while  p>0:
        print(p,end='')   
        p=p-1
    print()
    i=i-1
print()
print("THANK YOU for Choosing us _/\_")
print()        