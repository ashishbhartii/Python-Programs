# 6> WAP to create a list by taking input from the user and slice some part of it by taking 
#    input from the user.

print()
n=int(input("Enter the range of elements the list should contain --HERE-->"))
li=[]
print()
for i in range (0,n):
    n1=input(f"Enter the element at {i} th index -- HERe-->")
    li.append(n1)
print()
r1=int(input("Enter the First index range to begin slicing from-->"))
r2=int(input("Enter the last index range to begin slicing from-->"))
p=li[r1:r2]

print()
print(f"The NEWLY Formed List is {p}")
print()
print("THANK YOU for Chooding us _/\_")    