#wap to store deli collections on a list and give an option to change the list
a=int(input("How many days of collection do you want to store?"))
l=[]
for i in range(a):
    b=int(input("Enter a number: "))
    l.append(b)
print(l)
while True:
    print('''
    Here are your options to change the list
    1. Insert a new element in the list
    2. Update
    3. Display all
    4. Delete
    5. Search
    6. Count
    7. Sort
    8, Exit
    ''')
    c=int(input("Enter your choice: "))
    if c==1:
        print('''
    You can:
    1. Add a number at the end
    2. Add a number in a specific position
    ''')
        d=int(input("Enter your choice: "))
        e=int(input("Enter the element you want to add: "))
        if d==1:
            l.append(e)
        elif d==2:
            f=int(input("Where would you like to add the number? "))
            l.insert(f-1,e)
        else:
            print("You gave an invalid input! Please pick 1 or 2!")
    elif c==2:
        g=int(input("Which position do you want to update? "))
        h=int(input("What number do you want to replace it with? "))
        l[g-1]=h
    elif c==3:
        for i in l:
            print(i)
    elif c==8:
        print("See you soon!")
        break
