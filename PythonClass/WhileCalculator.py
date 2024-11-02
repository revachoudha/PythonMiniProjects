while True:
    print('''
     Choose an operation:
     1. +
     2. -
     3. *
     4. /
     5. Exit the program
    ''')
    a=float(input("enter your choice"))
    if a>=1 and a<=4:
        b=float(input("Enter your first number"))
        c=float(input("Enter you second number"))
    if a==1:
        print(b+c)
    elif a==2:
        print (b-c)
    elif a==3:
        print (b*c)
    elif a==4:
        print (b/c)
    elif a==5:
        print("See you next time!")
        break
    else:
        print("You entered an invalid operation number")
