# WAP to input a tuple and Check if all item are same in it or not.

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
print("THE checking for similar items starts HERE !!")
print()
z=tuple(y)
c=0
for j in range(n):
    for k in range(n):
        if z[j]==z[k]:
            break
        else:
            c=c+1
if c>0:
    print(f"THE DESIRED TUPLE IS {z} has Unique ITEMS")
else:
    print(f"THE DESIRED TUPLE IS {z} has repeted same ITEMS")
print()
print("THANK YOU FOR CHOOSING US _/\_")