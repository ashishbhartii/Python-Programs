# 20 > WAP to print integers between 1 to n print 'Fizz' for the numbers divisible by 3 and print 'BUZZ' 
#      if the numbers are divisble by 5 and print 'FIZZBUZZ' if the numbers are divisible by both 3 & 5.

print()
n=int(input("Enter the range of elements the list should contain --HERE-->"))
li=[]
print()
for i in range (1,n+1):
    if i % 3 == 0 and i % 5 == 0:
        li.append("FIZZ-BUZZ")
    elif i % 3 == 0:
        li.append("FIZZ")
    elif i % 5 == 0:
        li.append("BUZZ")
    else:
        li.append(i)
print()
print(f"The NEWLY Formed List is {li}")
print()
print("THANK YOU for Chooding us _/\_")    