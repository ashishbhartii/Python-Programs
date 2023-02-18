# WAP to input a list from the user and print element at every index.

li=[]
n=int(input("Enter the desired number of elements in the list --- HERE--->"))
for i in range (n+1):
    n1=input(f"Enter the {i} th ELEMENT in the list -->")
    li.append(n1)
print()    
print("THANK YOU for Putting in the VALUES ")
print()
for j in range(n+1):
    print (f'The Desired elements of the list at {j}th is here--->{li[j]}')
print()
print("THANK YOU For Choosing IS _/\_")