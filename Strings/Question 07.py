# WAP to input a string and find the number of vowels and consonents used.

print()
print("LETS BEGIN.. !!!")
print()
n=input("Enter the string that Whose Vowels & Consonents is to be counted -->")
print()
c=0
p=0
q=0
for i in n:
    if i=='a' or i=='e' or i =='i' or i =='o' or i =='u' or i=='A' or i=='E' or i =='I' or i =='O' or i =='U':
        c=c+1
    elif i ==' ':
        p=p+1
    else:
        q=q+1
print()
print("The calculated count of Vowels and Consonents goes like  ")
print()
print(f'The desired string is [ {n} ] consist of [ {c} ] Vowels & [ {q} ] Consonents along with [ {p} ] Whitespaces')
print()
print("Thank You for Choosing Us _/\_")