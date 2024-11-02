#waf to take an input as a parameter and returns the factorial of the number
def factorial(a):
    b=1
    for i in range(1,a+1):
        b=i*b
    print(b)
