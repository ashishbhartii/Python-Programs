# WAP to print the trainagular pattern 

#  1
#  32
#  654
#  10987
print()
n= int(input("Enter the no of rows you wish in your Questioned TRIANGULAR Pattern --- HERE--->"))
print()
i=1
p=0
c=1
while i<=n:
    j=1
    p=i+c
    q=p
    while j<=i:
        print(q,end='')
        q=q-1
        j=j+1
    print()
    c=c+1
    i=i+1
print()
print("THANK YOU for Choosing us _/\_")
print()        