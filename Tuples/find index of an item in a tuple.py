# WAP to input a tuple and find the index of a particular item.

# note: We cannot use append function with tuple directly instead convert tuple in list and then append the 
#        items & reconvert it.
print()

print("LETS BEGIN....")
print()
tup=()
y=list(tup)
n=int(input("Enter the number of elements you want the tuple to consist --HERE-->"))
print()
for i in range (n):
    n1=input(f"Enter the {i}th element of the tuple -->")
    y.append(n1)
print()
print("THE SEARCH STARTS HERE !!")
print()
n2=input("ENTER THE ELEMENT WHOSE INDEX IS TO BE FOUND HERE-->")
z=tuple(y)
print()
c=0
for j in range(n):
    if z[j]==n2:
        print(f"The index of the {n2} in the tuple {z} is == {j}")
    else:
        c=c+1
if c>0:
    print("SORRY !!! The item doesnot match the tuple")
print()
print("THANK YOU FOR CHOOSING US _/\_")