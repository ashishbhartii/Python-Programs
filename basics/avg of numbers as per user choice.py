# WAP to print the avg of the numbers input by the user 

n1= int(input("Enter the numbers to be considered ->"))
i=1
avg=0
sum=0
while i<=n1:
    p=int(input("Enter the number-->"))
    sum=sum+p
    i=i+1

avg=sum/n1
print()
print("the avearge of the considered numbers are " )
print(avg)
