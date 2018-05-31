import random

number = random.randint(0, 9)
#print (number)

while True:
    print('Guess the number from 0 to 9')
    guess = input()
    guess = int(guess)
    if guess == number:
        print("Correct!")
        break
    else:
        print("Wrong, try again!")


