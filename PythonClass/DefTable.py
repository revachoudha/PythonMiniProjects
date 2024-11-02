#waf which takes one parameter and prints the table of the number
def table(a):
    i=1
    while i<=12:
        print(a*i)
        i=i+1
#calling
b=int(input("Enter a number: "))
table(b)
