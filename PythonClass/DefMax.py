#waf which takes 2 parameters and finds the max out of 2
def max(a,b):
    if a>b:
        print(a, "is greater")
    elif b>a:
        print(b, "is greater")
    else:
        print("They are equal!")
#calling
a=int(input("Enter your first number: "))
b=int(input("Enter your second number: "))
max(a,b)
