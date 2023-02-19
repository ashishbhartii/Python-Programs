# 8>  WAP to input a string sentence and check for a particular word in that string along with its frequency.

print()
print("LETS BEGIN.. !!!")
print()
n=input("Enter the string that you want to be to searched for a particular string -->")
print()
li=[]
li=n.split()
n1=input("Enter the Word that you want to be to searched  -->")
print()
c=0
p=0
for i in li:
    c=c+1
    if n1==i:
        p=p+1
print(f"{n1} is present in the string [{n}]  with its frequency is {p}")
print()
print(f'Thank you for Choosing us _/\_')
print()