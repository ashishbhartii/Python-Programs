# WAP to reverse elements in the list without changing their index.

n=input("Enter the string in the list-- HERE-->")
print()
li=n.split()
li1=[]
print(f"The original created List is = {li}")
print()
for i in range(len(li)):
    for j in range(len(li[i])):
        li1.append(li[i][::-1])
#li.reverse()


print(f"The Reversed created List is = {li1}")
print()
print("THANK YOU for Choosing US _/\_")