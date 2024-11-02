a=int(input("Enter a number: "))
sum,b=0,a
while a>0:
    r=a%10
    sum=sum*10+r
    a=a//10
if b==sum:
    print(sum, "is a palindrome")
else:
    print(b, "is NOT a palindrome")
