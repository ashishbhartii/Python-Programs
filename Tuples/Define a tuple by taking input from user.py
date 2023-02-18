# WAP to input a tuple and print it.

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
print("THE APPENDING Ends HERE !!")
print()
z=tuple(y)
print(f"THE DESIRED TUPLE IS {z}")
print()
print("THANK YOU FOR CHOOSING US _/\_")