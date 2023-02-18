# WAP to print the trainagular pattern 

#  43211234
#  321123
#  2112
#  11
print()
n= int(input("Enter the no of rows you wish in your Questioned TRIANGULAR Pattern --- HERE--->"))
print()
i=n
while i>0:
    j=i
    while j>0:
        print(j,end='')
        j=j-1
    p=j    
    while  p<=i:
        print(p,end='')   
        p=p+1
    print()
    i=i-1
print()
print("THANK YOU for Choosing us _/\_")
print()        