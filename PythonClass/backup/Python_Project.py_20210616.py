while True:
    startup=input("Are you a student or a teacher? ")
    startup=startup.lower()
    if startup=='student':
        print('Welcome, student!')
        while True:
            rollnumber=int(input("Enter your roll number: "))
            import mysql.connector as m
            con=m.connect(host='localhost',user='root',password='mysql',database='python_project')
            cs=con.cursor()
            q='select * from student where rollnumber={}' . format(rollnumber)
            cs.execute(q)
            i=cs.fetchone()
            if i==None:
                print("The roll number you entered is wrong.")
            else:
                print("You are logged into your account!")
                while True:
                    print('''
Student Menu
1. Start test
2. View score
3. Exit
''')
                    choice=int(input("Which number would you like to do? "))
                    if choice==1:
                        print("Start test")
                        q='Select * from Question'
                        cs.execute(q)
                        while True:
                            score=0
                            i=cs.fetchone()
                            if i==None:
                                break
                            else:
                                print(i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5])
                                answer=input("What is the answer? ")
                                if answer==(i[6]):
                                    score=score+2
                                    print("Correct!")
                                else:
                                    print("That was incorrect!")
                        q='insert into student(score) values {}' . format(score)
                        cs.execute(q)
                        con.commit
                        break
                    elif choice==2:
                        print("View score")
                        q='select score from student where rollnumber={}' . format(rollnumber)
                        cs.execute(q)
                        i=cs.fetchone()
                        print(i)
                    elif choice==3:
                        print("See you next time!")
                        exit()
                    else:
                        print("That was not an option! Please choose 1, 2, or 3!")
    elif startup=='teacher':
        print("Welcome, teacher!")
        while True:
            account=input("Do you have an account? (Please answer yes or no) ")
            account=account.lower()
            if account=='yes':
                while True:
                    print("Please login into your account!")
                    employeeid=input("Please enter your Employee ID ")
                    employeeid='"'+employeeid+'"'
                    import mysql.connector as m
                    con=m.connect(host='localhost',user='root',password='mysql',database='python_project')
                    cs=con.cursor()
                    q='select * from Teacher where employeeid={}' . format(employeeid)
                    cs.execute(q)
                    i=cs.fetchone()
                    if i==None:
                        print("The Employee ID you gave is wrong!")
                        break
                    else:
                        cs1=con.cursor()
                        password=input("What is your password? ")
                        password='"'+password+'"'
                        q='select * from teacher where password={}' . format(password)
                        cs1.execute(q)
                        i=cs1.fetchone()
                        if i==None:
                            print("The Password you gave is wrong!")
                            break
                        else:
                            print("You are succesfully logged in!")
                            while True:
                                print('''
Teacher Menu
1. Add a question to the test
2. Update the test
3. Delete a specific question
4. Display the test
5. Add a student
6. Edit student information
7. Remove a student
8. Display the class list
9. Exit
''')
                                choice=int(input("Which number would you like to do? "))
                                if choice==1:
                                    while True:
                                        print("Ok then, let's add a question!")
                                        number=int(input("What is the question number? "))
                                        question=input("What is the question? ")
                                        question='"'+question+'"'
                                        option1=input("What is the first answer choice? ")
                                        option1='"a. '+option1+'"'
                                        option2=input("What is the second answer choice? ")
                                        option2='"b. '+option2+'"'
                                        option2=option2.lower()
                                        option3=input("What is the third answer choice? ")
                                        option3='"c. '+option3+'"'
                                        option4=input("What is the fourth answer choice? ")
                                        option4='"d. '+option4+'"'
                                        answer=int(input("What is the answer to the question? (Please enter 1, 2, 3, or 4.)"))
                                        if answer==1:
                                            answer='"a"'
                                        elif answer==2:
                                            answer='"b"'
                                        elif answer==3:
                                            answer='"c"'
                                        elif answer==4:
                                            answer='"d"'
                                        else:
                                            print("The answer should be 1,2,3, or 4!")
                                            break
                                        import mysql.connector as m
                                        con=m.connect(host='localhost',user='root',password='mysql',database='python_project')
                                        cs=con.cursor()
                                        q='insert into question values ({},{},{},{},{},{},{});' . format(number, question,option1,option2,option3,option4,answer)
                                        cs.execute(q)
                                        con.commit
                                        print(q)
                                        print("The new question has been added!")
                                        break
                                elif choice==2:
                                    print("You chose option 2: Update the test. This will allow you to change a question.")
                                    while True:
                                        change=input("What would you like to change? Your options are number, question, option1, option2, option3, option4, and answer.")
                                        change=change.lower()
                                        if change=='number' or change=='question' or change=='option1' or change=='option2' or change=='option3' or change=='option4' or change=='answer':
                                            number=int(input("What is the question number of the question you want to change? "))
                                            new=input('What would you like to replace the '+change+' with? ')
                                            new='"'+new+'"'
                                            q='update Question set {}={} where questionnumber={}' . format(change,new,number)
                                            cs.execute(q)
                                            con.commit
                                            print("The question has been succesfully updated!")
                                            break
                                        else:
                                            print("That was not an option!")
                                elif choice==3:
                                    delete=int(input("What is the question number of the question you want to delete? "))
                                    q='delete from Question where questionnumber={};' . format(delete)
                                    cs.execute(q)
                                    con.commit
                                    print("The question is now deleted!")
                                elif choice==4:
                                    print("Here is the test: ")
                                    q='Select * from Question'
                                    cs.execute(q)
                                    while True:
                                        i=cs.fetchone()
                                        if i==None:
                                            break
                                        else:
                                            print(i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t',i[6])
                                elif choice==5:
                                    name=input("What is the name of the student you would like to enter? ")
                                    name='"'+name+'"'
                                    rollnumber=int(input("What is the roll number of the student you would like to enter? "))
                                    grade=int(input("What grade level is the student in? "))
                                    q='insert into student(rollnumber, name, gradelevel) values ({},{},{})' . format(rollnumber,name,grade)
                                    cs.execute(q)
                                    con.commit
                                    print("The student has been succesfully added into the class list!")
                                elif choice==6:
                                    print("Edit student information")
                                    number=input("What is the roll number of the student you want to change? ")
                                    while True:
                                        change=input("What do you want to edit? Your options are: rollnumber, name, gradelevel, and score. ")
                                        chnage=change.lower()
                                        if change=='name' or change=='gradelevel' or change=='score':
                                            new=input("What do you want to replace "+change+" with?")
                                            new='"'+new+'"'
                                            q='update student set {}={} where rollnumber={}' . format(change,new,number)
                                            cs.execute(q)
                                            con.commit
                                            print("The student has succesfully been updated!")
                                            break
                                        elif change=='rollnumber':
                                            new=input("What do you want to replace rollnumber with?")
                                            q='update student set {}={} where rollnumber={}' . format(change,new,number)
                                            cs.execute(q)
                                            con.commit
                                            print("The student's rollnumber has been succesfully updated!")
                                            break
                                        else:
                                            print("that was not a valid input!")
                                elif choice==7:
                                    print("Remove a student")
                                    delete=int(input("What is the rollnumber of the student you want to delete? "))
                                    q='delete from Student where rollnumber={};' . format(delete)
                                    cs.execute(q)
                                    con.commit
                                    print("The student is now deleted!")
                                elif choice==8:
                                    print("Here is the list of all the students: ")
                                    q='Select * from student'
                                    cs.execute(q)
                                    while True:
                                        i=cs.fetchone()
                                        if i==None:
                                            break
                                        else:
                                            print(i[0],'\t',i[1],'\t',i[2],'\t',i[3])
                                elif choice==9:
                                    print("See you later! ")
                                    exit()
                                else:
                                    print("That was not an option! Please choose a number between 1 and 9.")
            elif account=='no':
                print('''
Ok, then! Let's create an account!
First you will need to make your Employee ID.
Here are the rules:
It should be more than 8 characters long
There should be letters, numbers, and one special character
No spaces
''')
                while True:
                    employeeid=input("What would you like your Employee ID to be? Please remember to follow all of the rules! ")
                    if len(employeeid)>=8:
                        space=0
                        alnum=0
                        special=0
                        for i in employeeid:
                            if i.isalnum():
                                alnum=alnum+1
                            elif i==" ":
                                space=space+1
                            else:
                                special=special+1
                        if space>0:
                            print("Please remember not to add any spaces!")
                            break
                        elif alnum>1 and special==1:
                            employeeid='"'+employeeid+'"'
                            import mysql.connector as m
                            con=m.connect(host='localhost',user='root',password='mysql',database='python_project')
                            cs=con.cursor()
                            q='insert into Teacher (EmployeeID) values ({});' . format(employeeid)
                            cs.execute(q)
                            con.commit()
                            print('''
Your employee ID works! Now please create your password. The password has the same rules as the Employee ID. Here is a reminder:
More than 8 characters long.
Letters, numbers, and one special character
No spaces
''')
                            while True:
                                password=input("What would you like your password to be? Please remember to follow all of the rules!")
                                if len(password)>=8:
                                    space=0
                                    alnum=0
                                    special=0
                                    for i in password:
                                        if i.isalnum():
                                            alnum=alnum+1
                                        elif i==" ":
                                            space=space+1
                                        else:
                                            special=special+1
                                    if space>0:
                                        print("Please remember not to add any spaces!")
                                        break
                                    elif special>1 or special<1:
                                        print("You need 1 special character!")
                                        break
                                    elif alnum<1:
                                        print("Remember to add numbers and letters to your password!")
                                    else:
                                        password='"'+password+'"'
                                        q='update Teacher set password={} where employeeid={};' . format(password,employeeid)
                                        cs.execute(q)
                                        con.commit()
                                        print("Your password is correct!")
                                        name=input("What is your name? ")
                                        name='"'+name+'"'
                                        q='update Teacher set name={} where employeeid={};' . format(name,employeeid)
                                        cs.execute(q)
                                        con.commit()
                                        print("Congtulations! You have created an teacher account!")
                                        print("See you later!")
                                        exit()
                                        
                                else:
                                    print("Remember: it should be more than 8 characters long!")
                                
                        elif special>1:
                            print("You may only have one special character!")
                            break
                        elif alnum<1:
                            print("Please remember to add numbers and letters to your Employee ID!")
                            break
                        else:
                            print("Remember to add a special character!")
                            break
                    else:
                        print("Your id is not long enough! Remember: It should be more than 8 characters long!")
                else:
                    print('Please answer with yes or no!')
    else:
        print("Please enter student or teacher! You did not give a valid input!")
