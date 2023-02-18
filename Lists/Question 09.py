# 9> Given a two Python list. Write a program to iterate both lists simultaneously and display 
#     items from list1 in original order and items from list2 in reverse order.

print()
n=int(input("Enter the range of elements the list A should contain --HERE-->"))
li1=[]
li2=[]
print()
for i in range (n+1):
    n1=input(f"Enter the element at {i} th index -- HERe-->")
    li1.append(n1)
print()
n2=int(input("Enter the range of elements the list B should contain --HERE-->"))
print()
for j in range (n2+1):
    n3=input(f"Enter the element at {j} th index -- HERe-->")
    li2.append(n3)

print(f"The NEWLY Formed List A is {li1[::]}")
print()
print(f"The NEWLY Formed List B is {li2[::-1]}")
print()
print("THANK YOU for Chooding us _/\_")    