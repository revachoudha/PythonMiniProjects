while True:
    import mysql.connector as m
    con=m.connect(host='localhost',
    user='root',
    password='mysql',
        database='Reva')
    cs=con.cursor()
    choice=input('''
Would you like to...
1. print the entire table
2. print just one row
''')
    choice=choice.lower()
    if choice==2 or 'print just one row':
        a=int(input("Enter toy id: "))
        q='select * from toy where tid='+ str(a)
        cs.execute(q)
        i=cs.fetchone()
        print(i)
        if i==None:
            print("The toy id you gave is wrong.")
        else:
            print(i[0],'\t',i[1],'\t',i[2],'\t',i[3])
    elif choice==1 or 'print the entire table':
        q='select * from toy'
        cs.execute(q)
        i=cs.fetchall
        print(i)
    else:
        print('''
The number you gave was not an option! Please give 1 or 2!
''')
