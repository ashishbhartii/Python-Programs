# 13> WAP to create a list by taking input from the user and remove all the even nos and print the new list.

print()
n=int(input("Enter the range of elements the list should contain --HERE-->"))
li=[]
print()
for i in range (n+1):
    n1=int(input(f"Enter the element at {i} th index -- HERe-->"))
    li.append(n1)
for j in li:
    if j % 2 == 0:
        li.pop(j)
print()
print(f"The NEWLY Formed List is {li}")
print()
print("THANK YOU for Chooding us _/\_")    