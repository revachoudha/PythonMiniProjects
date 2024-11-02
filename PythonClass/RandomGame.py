'''
wap to create a simple luck number game in python where:
1. generate a random integer from 1-50
2. user will get 3 chances to guess the number
3. if the number is matching, you will give a congratulations message if not, say that they lost
'''
import random
a=random.randint(1,5)
print(a)
for i in range(1,4):
    b=int(input("Enter a number: "))
    if a==b:
        print("Congratulations! You win!")
        break
    else:
        print("Try again!")
else:
    print("Sorry, you lose! Better luck next time.")
