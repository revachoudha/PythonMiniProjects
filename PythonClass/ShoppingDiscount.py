a=int(input("Write your total shopping amount: "))
if a>=20000 and a<100000:
    b=a*0.1
    print("Your discount is ", b)
    print("Your total is ",a-b)
elif a>=100000:
    b=a*0.05
    print("Your discout is ", b)
    print("Your total is ",a-b)
else:
    print("Sorry, you don't get a discount")
