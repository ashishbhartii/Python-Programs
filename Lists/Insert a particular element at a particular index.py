# WAP to enter a string convert it into a list and then insert an element at a particular index in a list.


print()
n=input("Enter the string to be operated here ---->")
print()
li=n.split()
n1=input("Enter the element which is to be inserted ---- here ---->")
print(f"The ORIGINAL LIST is here---> {li}")
print()
n2=int(input(f"Enter the index at which the {n1} is to be inserted here--->"))
print()
#for i in range (len(li)):
li.insert(n2,n1)
print(f'The modified list id here {li}')        
print()
print("THANK YOU For Choosing US _/\_")  

