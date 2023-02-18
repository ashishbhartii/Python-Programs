# WAP to print the trainagular pattern 

#  1
#  32
#  345
#  7654
print()
n= int(input("Enter the no of rows you wish in your Questioned TRIANGULAR Pattern --- HERE--->"))
print()
i=1
num=1
k=1
while i<=n:
    j=1
    while j<=i:
        if i%2!=0:
            print(num,end='')
            num=num+1
        else:
            print(num,end='')
            num=num-1

        j=j+1
    num=num+k
    if i%2!=0:
        k=k+2    
    print()
    i=i+1
print()
print("THANK YOU for Choosing us _/\_")
print()        