# WAP to reverse the multiples of given numbers within a given range

n=int(input("Enter the range for natural numbers-->"))
num=int(input("Enter the number whose multiple is to be found -->"))

print()
print("The multiples of" , num , "in revese order are down below :")
i=n
while i>0:
    if i%num==0:
        print(i," ",end="")
    i=i-1
print()    
print("THATS All")