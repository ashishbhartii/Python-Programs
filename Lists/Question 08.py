# 8> WAP to create a list by taking input from the user numeric and find its squares and stor it 
#    into another list & display both.

print()
n=int(input("Enter the range of elements the list should contain --HERE-->"))
li=[]
print()
for i in range (0,n):
    n1=int(input(f"Enter the element at {i} th index -- HERe-->"))
    li.append(n1)
print()
sq=[]
for j in range (0,n):
    p=li[j]**2
    sq.append(p)


print()
print(f"The ORIGINAL Formed List is {li}")
print()
print(f"The Square Formed List is {sq}")
print()
print("THANK YOU for Chooding us _/\_")    
