#Find the 100th birthday
print("Would you like to find out what year you will turn 100?")
name=input("Please enter your name here: ")
age=int(input("Please enter your age here: "))
birth=int(2021-age)
year=int(birth+100)
message=print(name,"you will turn 100 in the year",year)
print(message)
#ask for a number and print out above message that many times
number=int(input("Please enter a number: "))
i=0
while i<number:
    print(message)
    i=i+1