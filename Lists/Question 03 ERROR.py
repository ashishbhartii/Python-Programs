#  3> WAP to create a list of integers and do arithematic opeartions like sum, mul on them.

def add(a):
    sum=0
    for i in range (0,n1):
        sum=sum+a[i]
    print(f"Here the sum of list {a} is {sum}")

def sub(a):
    sub=0
    for i in range (0,n1):
        sub=sub-a[i]
    print(f"Here the subraction of list {a} is {sub}")
        
def mul(a):
    mul=1
    for i in range (0,n1):
        mul=mul*a[i]
    print(f"Here the Multiplication of list {a} is {sub}")
a=[]
print()
n1=int(input("Enter the range of element for LIST A--- HERE--->"))
print()
for i in range(0,n1):
    n1=int(input(f'Enter the {i} th element in LIST A -- HERE -->'))  
    a.append(n1) 

print()

print("WELCOME to Arithematic Operations")  
print()
print("Choose Between the following option for better result:")
print()
print("Option 01 -> add")
print("Option 02 -> sub")
print("Option 03 -> mul")
print()
n2=input("Enter Your Choice from the above Excatly as mentioned -- HERE-->")
print()
if n2==add:
    add(a)
elif n2==sub:
    sub(a)
else:
    mul(a)

