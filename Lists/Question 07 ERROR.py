# WAP to concatenate two lists by king input from the user in a chain format.

li1=[]
li2=[]
li3=[]
print()
n1=int(input("Enter the range of elements for list 01 ---HERE--->"))
print()

for i in range (n1+1):
    new1=input(f"Enter the {i} th element of the List 01 --->")
    li1.append(new1)
print()
n2=int(input("Enter the range of elements for list 02 ---HERE--->"))
for j in range (n2+1):
    new2=input(f"Enter the {j} th element of the List 02 --->")
    li2.append(new2)
print()    
ind=0
p=n1+n2
for k in range(p):
    li3.append(li1)
    li3.append(li2)
print()
print(f"The List 01 is ---> {li1}")
print()
print(f"The List 02 is ---> {li2}")
print()
print(f"The NEW Appended List 03 is ---> {li3}")
print()
print("THANK YOU for Choosing US _/\_")