#  4>  WAP to input a string and print its length with using len function.

print()
print("LETS BEGIN.. !!!")
print()
n=input("Enter the string that you want to find the length manually -->")
print()
c=0
for i in n:
    if i != " ":
        c=c+1
print(f'The desired length of the string [ {n} ] is --> {c}')