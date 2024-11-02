print('''
 Choose an operation:
 1. +
 2. -
 3. *
 4. /
''')
a=int(input("Enter your operation number: "))
if a>4:
    a=int(input("Enter valid operation number: "))
elif a<0:
    a=int(input("Enter valid operation number: "))
else:
    print ("Now enter your numbers")
b=int(input("Enter 1st number: "))
c=int(input("Enter 2nd number: "))
if a==1:
    print(b+c)
elif a==2:
    print (b-c)
elif a==3:
    print (b*c)
else:
    print (b/c)
