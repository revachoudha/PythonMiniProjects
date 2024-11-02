#wap to take a string from user and count number of digits and letters

a=input("Enter a string:")
number,letter,space,lower,upper=0,0,0,0,0
for i in a:
    if i.isalpha():
        letter=letter+1
        if i.islower():
            lower=lower+1
        elif i.isupper():
            upper=upper+1
    elif i.isdigit():
        number=number+1
    elif i.isspace():
        space=space+1
    elif i.islower():
        lower=lower+1
    elif i.isupper():
        upper=upper+1
print("The number of letters in the string that you entered is:", letter)
print("The number of numbers in the string that you entered is:", number)
print("The number of spaces in the string that you entered is:", space)
print("The number of uppercase letters in the string that you entered is:", upper)
print("The number of lowercase in the string that you entered is:", lower)
