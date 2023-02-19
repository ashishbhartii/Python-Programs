# 7>  7>  WAP to input a string and print and check for a particular letter and its 
#         frequency present in the string.

print()
print("LETS BEGIN.. !!!")
print()
n=input("Enter the string that you want to be to searched for a particular string -->")
print()
n1=input("Enter the letter that you want to be to searched  -->")
print()
c=0
for i in n:
    if n1==i:
        c=c+1
print(f"{n1} letter is present in the string [{n}] with its frequency as --> {c}")
print()
print(f'Thank you for Choosing us _/\_')