# WAP to find the factorial of all the prime numbers till a given range

n=int(input("Enter tthe range till which PRIME nos are to be EXtracted -->"))
i=1
while i<=n:
    print()
    c=0
    j=1
    while j<=i:
        if i%j==0:
            c=c+1
        j=j+1
    if c==2:
        print (i,end='')
        print ("  is PRIME ")
        print()
        i1=1
        fac=1
        p=i
        print("The factorial of ", i, " goes like :")
        print()
        while i1<=i:
            print(p," * ",end='')
            fac=fac*i1
            p=p-1
            i1=i1+1
        print(" = ",end='')
        print(fac) 
    i=i+1    
print()
print("THANK YOU")