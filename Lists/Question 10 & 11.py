#10 WAP to create a numeric list by input from the user and print the largest & Smallest among all.

print()
n=int(input("Enter the range of elements the list should contain --HERE-->"))
li=[]
print()
for i in range (n+1):
    n1=int(input(f"Enter the element at {i} th index -- HERe-->"))
    li.append(n1)
print()
lar=max(li)
smal=min(li)
print(f"The Entered List is {li}")
print()
print(f"The Largest Number among the List is {lar} & The Smallest Number among the list is {smal}")
print("THANK YOU for Chooding us _/\_")    