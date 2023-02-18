# WAP to enter a string convert it into a list and then ireplace an element at a particular index in a list.


print()
n=input("Enter the string to be operated here ---->")
print()
li=n.split()
print(f"The ORIGINAL LIST is here---> {li}")
print()
n1=input("Enter the element which is to be Replaced WITH ---- here ---->")
print()
n2=int(input(f"Enter the index at which the {n1} is to be replaced here--->"))
print()
li.pop(n2)
li.insert(n2,n1)
print(f'The modified list id here {li}')        
print()
print("THANK YOU For Choosing US _/\_")  
