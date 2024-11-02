def num():
    a=int(input("Enter a number: "))
    if a==0:
        print("Your number is zero")
    elif a>0:
        print("Your number is positive")
    else:
        print("Your number is negative")
    i=1
    while i<=12:
        print(i*a)
        i=i+1
num()
