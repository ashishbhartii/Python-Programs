# 2> WAP to create two lists by taking input from the user and conatenate it using '+' operator , 
#    using append function & using extend function

def addoperation(a,b):
    c=[]
    c=a+b
    print(f"Heres Concatenated list {c} using + operator for you")

def append_Function(a,b):
    a.append(b)
    print(f"Heres Concatenated list {a} using Append Function for you")
        
def extend_Function(a,b):
    a.extend(b)
    print(f"Heres Concatenated list {a} using Extend Function for you")
a=[]
b=[]
print()
n1=int(input("Enter the range of element for LIST A--- HERE--->"))
print()
for i in range(0,n1):
    n1=input(f'Enter the {i} th element in LIST A -- HERE -->')  
    a.append(n1) 

print()
n2=int(input("Enter the range of element for LIST B--- HERE--->"))
print()
for j in range(0,n2):
    n1=input(f'Enter the {j} th element in LIST B -- HERE -->')  
    b.append(n2)   
print()  
print("WELCOME to CONCATENATING Operations")  
print()
print("Choose Between the following option for better result:")
print()
print("Option 01 -> addoperation")
print("Option 02 -> append_Function")
print("Option 03 -> extend_Function")
print()
n3=input("Enter Your Choice from the above Excatly as mentioned -- HERE-->")
print()
if n3==addoperation:
    addoperation(a,b)
elif n3==append_Function:
    append_Function(a,b)
else:
    extend_Function(a,b)

