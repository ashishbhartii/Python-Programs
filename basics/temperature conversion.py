# WAP for temperature conversion.

temp=input("Enter Your choice to be converted to *CELCIUS  *FARENHEIT ---->")
print()


if (temp=="celcius" or temp=="CELCIUS"):
    f=int(input("Enter the temperature in Farenheit-->"))
    celcius=[5*(f-32)/9]
    int(celcius)
    kelvin= celcius+273
    print("The converted temperature in CELCIUS is  =  ", end='')
    print(celcius)
    print()
    print("Also its KELVIN equivalent is  =  ", end='')
    print(kelvin)

if (temp=="farenheit" or temp=="FARENHEIT"):
    c=int(input("Enter the temperature in CELCIUS-->"))
    farenheit=[(9*c)/5]+32
    kelvin=c+273
    print("The converted temperature in FARENHEIT is  =  ", end='')
    print(farenheit)
    print()
    print("Also its KELVIN equivalent is  =  ", end='')
    print(kelvin)

print("THANK YOU FOR CHOOSING US  _/\_ ")