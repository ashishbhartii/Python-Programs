# 4> WAP to create a list by taking input from the user and remove an item from the list by taking as an 
#    input from the user.

print()
n=int(input("Enter the range of elements the list should contain --HERE-->"))
li=[]
print()
for i in range (0,n):
    n1=input(f"Enter the element at {i} th index -- HERe-->")
    li.append(n1)
print()
opt=input("Enter the element to be popped out from the LIST-->")
for j in range (0,n):
   if opt==li[j]:
       li.pop(j)

print()
print(f"The NEWLY Formed List is {li}")
print()
print("THANK YOU for Chooding us _/\_")    
