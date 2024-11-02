#wap to find if a number is prime

a=int(input("Enter your number: "))
for i in range(2,a):
    if a%i==0:
        print("your number is not prime")
        break
else:
    print("Your number is a prime number")
        
