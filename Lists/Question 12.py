# 12 WAP that takes two lists and returns True if they have at least one common member.

print()
na=int(input("Enter the range of elements the list A should contain --HERE-->"))
lia=[]
print()
for i in range (na+1):
    n1=input(f"Enter the element at {i} th index -- HERe-->")
    lia.append(n1)
print()
nb=int(input("Enter the range of elements the list b should contain --HERE-->"))
lib=[]
for j in range (nb+1):
    n2=input(f"Enter the element at {j} th index -- HERe-->")
    lib.append(n2)

for k in range (na):
    for l in range(nb):
        if lia[k]==lib[l]:
            print(f"The list A {lia} & the list B {lib} have an element in common which is {lib[l]}")
        
print(f"The list A {lia} & the list B {lib} have nothing in COMMON")
print()

print("THANK YOU for Chooding us _/\_") 