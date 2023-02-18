# WAP to input 3 nos and check whether they can form side of the triangle or not.

n1= int(input("Enter the first number ->"))
n2= int(input("Enter the second number ->"))
n3= int(input("Enter the third number ->"))
if (n1==n2==n3):
    print("Yes!! These sides can be configured into a EQUILATERAL triangle...")
elif (n1==n2 or n2==n3 or n3==1):
    print("Yes!! These sides can be configured into a ISOSCELES triangle...")
elif(n3+n1)>n2:
    print("Yes!! These sides can be configured into a SCALANE triangle...")
elif (n1+n2)>n3:
    print("Yes!! These sides can be configured into a SCALANE triangle...")
elif (n2+n3)>n1:
    print("Yes!! These sides can be configured into a SCALANE triangle...")
else:
    print("Sorry!! These sides cannot be configured into a triangle...")

