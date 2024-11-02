#take 3 input, ID, phone number and password
#ID should be at least 8 numbers, letters or underscores.. no spaces
#password should be a combination of capital letters lowercase letters and can only be 10 characters long.
# Phone number can only be 10 DIGITS
upper=lower=digit=0
space=0
uc=0
alnum=un=0
other=0
id=input("Enter you ID: ")
if len(id)>=8:
    for i in id:
        if i.isalnum():
            alnum=alnum+1
        elif i=="_":
            uc=uc+1
        else:
            other=other+1
    if alnum>=1 and other==0:
        print("You ID is correct!")
        pas=input("Enter a password: ")
        if len(pas)>=5:
            for i in pas:
                if i.isdigit():
                    digit=digit+1
                elif i.isupper():
                    upper=upper+1
                elif i.islower():
                    lower=lower+1
                elif i.isspace():
                    space=space+1
                else:
                    uc=uc+1
            if digit>=1 and upper>=1 and lower>=1 and space==0 and uc>=1:
                print("Your password works! Make sure it has a goood strength")
            else:
                print(" You password does not have either an number or letters or are not a combination of uppercase letters or lowercase letter!")
        else:
            print("You do not have a long enough password, it has to be more than 5 character!")
    else:
        print("id may contain only al,no and underscore")
else:
   print("Please make you ID more than 8 characters!")
