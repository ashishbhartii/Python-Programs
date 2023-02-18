# WAP to create a list having the elements as the words of the sting, 
#  and print the words in a new list which has letter "s".

print()
n=int(input("Enter the range of elements the list should contain --HERE-->"))
li=[]
print()
for i in range (n+1):
    n1=input(f"Enter the element at {i} th index -- HERe-->")
    li.append(n1)
print()
for j in range(n):
    for k in range(len(li[j])):
        if li[j][k]=='s' or li[j][k]=='S':
            print(li[j])
print()
print(f"The NEWLY Formed List is {li}")
print()
print("THANK YOU for Chooding us _/\_")  