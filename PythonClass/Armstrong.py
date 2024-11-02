a=int(input("Enter a number: "))
sum=0
b=a
while a>0:
    r=a%10
    c=r**3
    sum=sum+c
    a=a//10
if b==sum:
    print(b, "is Armstrong")
else:
    print(b, "is not Armstrong")
