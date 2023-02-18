# WAP to input two tuple and swap their values.

# note: We cannot use append function with tuple directly instead convert tuple in list and then append the 
#        items & reconvert it.
print()

print("LETS BEGIN....")
print()
tup1=()
y1=list(tup1)
n=int(input("Enter the number of elements you want the tuple 1 to consist --HERE-->"))
print()
for i in range (n):
    n1=input(f"Enter the {i}th element of the tuple 1 -->")
    y1.append(n1)
print()
tup2=()
y2=list(tup2)
n2=int(input("Enter the number of elements you want the tuple 1 to consist --HERE-->"))
print()
for j in range (n2):
    n1=input(f"Enter the {j}th element of the tuple 2 -->")
    y2.append(n1)
print()
print("THE APPENDING Ends HERE !!")
print()
z1=tuple(y1)
z2=tuple(y2)
print(f"THE ORIGINAL TUPLE 1 IS {z1} && ORIGINAL TUPLE 2 id {z2}")
print()
z1,z2=z2,z1
print(f"THE SWAPPED TUPLE 1 IS {z1} && SWAPPED TUPLE 2 id {z2}")
print()
print("THANK YOU FOR CHOOSING US _/\_")