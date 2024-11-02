'''
Factorial of a number
Factorial - 5!=1*2*3*4*5=x
Write it with ! after the number
'''
a=int(input("enter a number: "))
fact=1
i=1
while i<=a:
    fact=fact*i
    i=i+1
print(fact)
