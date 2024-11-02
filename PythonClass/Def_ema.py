def ema(a):
    if a%2==0:
        b=int(input("Enter a number: "))
        c=int(input("Enter a number: "))
        if b>c:
            return a+c
        else:
            return a+b
    else:
        print("The number is odd!")
        
#calling
a=int(input("Enter you number: "))
d=ema(a)
print(d)
