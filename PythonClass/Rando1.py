#random number 25-50, 25-35, buzz or not, 36-50, square


def rando1():
    import random
    a=random.randint(25,50)
    if a<36:
        if a%10==7 or a%7==0:
            print("your number is BUZZ")
        else:
            print("your number is not BUZZ")
    else:
        print("square of your number is", a**2)
