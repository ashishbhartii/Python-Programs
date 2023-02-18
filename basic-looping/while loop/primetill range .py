# WAP to find prime numbers till a given range

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
    i=i+1    
print()
print("THANK YOU")