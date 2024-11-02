import mysql.connector as m
con=m.connect(host='localhost',user='root',password='mysql',database='Reva')
cs=con.cursor()
price=int(input("Enter the max price you would like to pay: "))
q='select  tname, price from toy where price < {}' . format(price)
cs.execute(q)
while True:
    c=cs.fetchone()
    if c==None:
        break
    else:
        print(c)
