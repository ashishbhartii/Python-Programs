# 14. WAP to create a list by taking input from the user & find the index of a 
#     particular element taken as an input from the user.

print()
n=int(input("Enter the range of elements the list should contain --HERE-->"))
li=[]
print()
for i in range (n+1):
    n1=input(f"Enter the element at {i} th index -- HERe-->")
    li.append(n1)
n1=input("Enter the element whose index is to be found-->")
print()
for j in range(n+1):
    if li[j] == n1:
        print(f"The index of [{n1}] in the given list {li} is [{j}] ")

print()
print(f"The  Formed List is {li}")
print()
print("THANK YOU for Chooding us _/\_")  