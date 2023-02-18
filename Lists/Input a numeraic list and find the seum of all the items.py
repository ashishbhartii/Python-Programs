# WAP to enter a numeric list and then find the sum of eeven and odd and total seperately

print()
n=int(input("Enter the total number of elements for the list ---->"))
print()
sum=0
sumeven=0
sumodd=0
li=[]
lieven=[]
liodd=[]
print()
for i in range (n+1):
    n1=int(input(f'Enter The {i}th of the listt ---here-->'))
    li.append(n1)


for j in range (n+1) :
    if li[j]%2!=0:
        sum=sum+li[j]
        sumodd = sumodd+li[j] 
        liodd.append(li[j])
    else:
        sum=sum+li[j]
        sumeven = sumeven+li[j] 
        lieven.append(li[j])

print()        
print(f'The sumy of elements of list {li}  is {sum}')
print()        
print(f'The sumy of odd elements of list {liodd}  is {sumodd}')
print()        
print(f'The sumy of even elements of list {lieven}  is {sumeven}')  
print()
print("THANK YOU For Choosing US _/\_") 