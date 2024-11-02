while True:
    import mysql.connector as m
    con=m.connect(host='localhost',user='root',password='mysql',database='Reva')
    cs=con.cursor()
    column=input("Enter the column you would like to update (tid, tname, price, or dop): ")
    toy=int(input("What is the id of the toy you would like to update? "))
    if column=='tid':
        value=int(input("What is the new id of the toy? "))
    elif column=='tname':
        value=input("What would you like to name the toy? ")
        value='"'+value+'"'
    elif column=='price':
        value=float(input("What is the new price of the toy? "))
    elif column=='dop':
        value=input("What is the new date you purchased the toy? (Please enter it in the format of yyyy/mm/dd): ")
        value='"'+value+'"'
    else:
        print("That's not a column! There is only tid, tname, price, and dop!")
    q='update Toy set {}={} where tid={}' . format(column,value,toy)
    cs.execute(q)
    con.commit()
    print("Your Table has been updated!")

