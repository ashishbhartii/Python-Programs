# WAP to input a tuple and slice it as per the user.

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
a=int(input("Enter the initial index to begin slicing from --here-->"))
print()
b=int(input("Enter the last index to begin slicing from --here-->"))

print()
print("THE SLICING STARTS HERE !!")
print()
z=tuple(y)
print(f"THE ORIGINAL TUPLE IS {z}")
print()
print(f"THE DESIRED Sliced TUPLE IS {z[a:b+1]}")
print()
print("THANK YOU FOR CHOOSING US _/\_")