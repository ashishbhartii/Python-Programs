# 2> WAP to input a string and print very character of it in seperate lines or 
#    every character of it in seperate lines.

print()
print("LETS BEGIN.. !!!")
print()
n=input("Enter the Choice between words or letters -->")
print()
if n == "words" or n=="Words" or n=="WORDS":
    print()
    a=input("Enter the string that you want to be operated ---HERE--->")
    li=[]
    li=a.split()
    print()
    print("Here are the words seperated from the string sentence")
    print()
    for i in li:
        print(i)
    print()
    print("Thank you for choosing s _/\_")
elif n == "Letters" or n=="LETTERS" or n == "letters":
    print()
    b=input("Enter the string that you want to be operated ---HERE--->")
    print()
    print("Here are the letters seperated from the string sentence")
    print()
    for j in b:
        print(j)
    print()
    print("Thank you for choosing s _/\_")

