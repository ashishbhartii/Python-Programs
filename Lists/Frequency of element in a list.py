# WAP to enter a string convert it into a list and then find the frequency of a particular element

print()
n=input("Enter the string to be operated here ---->")
print()
li=n.split()
count=0
n1=input("Enter the element whose freuency is to be found ---- here ---->")
print()
for i in range (len(li)):
    if n1== li[i]:
        count=count+1
print(li)        
print(f'The frequency of {n1} in the above mentioned string is {count}')  
print()
print("THANK YOU For Choosing US _/\_")  

