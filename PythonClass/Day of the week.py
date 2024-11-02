print('''
Choose a day of the week
1. Sunday
2. Monday
3. Tuesday
4. Wednesday
5. Thursday
6. Friday
7. Saturday
''')
a=int(input("Type the number for the day of the week here: "))
if a==1:
    print("Sunday")
elif a==2:
    print("Monday")
elif a==3:
    print("Tuesday")
elif a==4:
    print("Wednesday")
elif a==5:
    print("Thursday")
elif a==6:
    print("Friday")
elif a==7:
    print("Saturday")
else:
    print("Please choose a valid number!")
    exit()
