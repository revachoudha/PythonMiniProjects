#wap to take a string from the user and print the reverse case of all letters
a=input("Enter a string: ")
b=""
for i in a:
    if i.islower():
        b=b+i.upper()
    elif i.isupper():
        b=b+i.lower()
    else:
        b=b+i
print("The reverse of your string is", b)
