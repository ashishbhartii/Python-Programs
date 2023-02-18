# 5> WAP to create a list by taking input from the user and append some items by taking input from the user.



print()
n=int(input("Enter the range of elements the list should contain --HERE-->"))
li=[]
print()
for i in range (0,n):
    n1=input(f"Enter the element at {i} th index -- HERe-->")
    li.append(n1)
print()
opt=int(input("Enter the number of elements that has to be appended in the LIST-->"))
for j in range (0,opt):
   n1=input("Enter the {j} th new element to be appended -- here-->")
   li.append(n1)

print()
print(f"The NEWLY Formed List is {li}")
print()
print("THANK YOU for Chooding us _/\_")    
