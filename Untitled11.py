def gcd(a,b):
    if(b==0):
        print(a)
    else:
        gcd(b,a%b)
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
gcd(a,b)
