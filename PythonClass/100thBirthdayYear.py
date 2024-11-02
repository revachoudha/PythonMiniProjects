 print("Hello! Would you like to find out which year your 100th birthday will be?")
a=input("Enter your name here: ")
b=int(input("Enter your age here: "))
c=int(input("What year was your last birthday? "))
if c==2020 or c==2021:
    d=c-b+100
    print(a,", You will turn 100 years old in the year",d)
