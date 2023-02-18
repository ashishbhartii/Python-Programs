# 18> WAP to use range function and create a sepertae list of even numbers.

print()
n=int(input("Enter the range of elements the list should contain --HERE-->"))
li=[]
print()
for i in range (n+1):
    n1=int(input(f"Enter the element at {i} th index -- HERe-->"))
    li.append(n1)
eve=[]
print()
for j in range(n+1):
    if li[j] % 2 == 0:
        eve.append(li[j])

print(f"The Original List is {li} & the NEWLY Formed List is {eve}")
print()
print("THANK YOU for Chooding us _/\_")    