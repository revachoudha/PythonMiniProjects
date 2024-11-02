print('''
Choose an option:
1. Find out if you're an adult or child
2. Find out if a number is buzz or not
3. Find out if a number is even or odd
4. Find out if a number is negative, positive, or zero
5. Leave the program
''')
n=int(input("Enter the number for the option that you chose here: "))
if n==1:
    print("Let's find out if you're an adult or a child!")
    a=int(input("Enter your age here: "))
    if a>=18:
        print("You are an adult")
    else:
        print("You are a child")
    print("Goodbye!")
    exit()
elif n==2:
    print("Let's find out if your number is a buzz number!")
    a=int(input("Enter your number here: "))
    if a%7==0 or a%10==7:
        print(a, "is buzz!")
    else:
        print(a, "is NOT buzz!")
    print("Goodbye!")
    exit()
elif n==3:
    print("Let's find out if your number is even or odd!")
    a=int(input("Enter your number here: "))
    if a%2==0:
        print(a,"is even!")
    else:
        print(a,"is odd!")
    print("Goodbye!")
    exit()
elif n==4:
    print("Let's find out if your number is negative or positive!")
    a=int(input("Enter a number here: "))
    if a<0:
        print(a, "is negative")
    elif a>0:
        print(a, "is positive")
    else:
        print(a, "is neither negative nor positve. It is zero!")
    print("Goodbye!")
    exit()
elif n==5:
    print("Okay, I hope to see you again! Bye!")
    exit()
else:
    print("Please choose a valid choice!")
    exit()
