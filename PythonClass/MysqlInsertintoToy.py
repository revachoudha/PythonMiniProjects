#Add a new row to the Toy Table in MySQL
while True:
    import mysql.connector as m
    con=m.connect(host='localhost',user='root',password='mysql',database='Reva')
    cs=con.cursor()
    tid=int(input("Enter the id of the new toy: "))
    tname=input("Enter the name of the new toy: ")
    tname='"'+tname+'"'
    price=float(input("Enter the price of the new toy: "))
    dop=input("What is the date of purchasing the new toy? (Please enter in the form of(yyy/mm/dd)")
    q='insert into Toy values({},{},{},{})' . format(tid,tname,price,'"'+dop+'"')
    cs.execute(q)
    con.commit()
    print("Success! The new column has been added to your table!")
