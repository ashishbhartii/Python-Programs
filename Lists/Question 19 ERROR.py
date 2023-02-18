# 19> WAP to use range function and create a sepertae list of PRIME numbers.

print()
n=int(input("Enter the range of elements the list should contain --HERE-->"))
li=[]
print()
for i in range (n+1):
    n1=int(input(f"Enter the element at {i} th index -- HERe-->"))
    li.append(n1)
prime=[]
print()
c=0
for j in range(n+1):
    for k in range (1,li[j]):
        if li[j] % k == 0:
            c=c+1
    
    if c == 2:
        prime.append(li[j])
           

print(f"The Original List is {li} & the NEWLY Formed List of prime numbers are {prime}")
print()
print("THANK YOU for Chooding us _/\_")    