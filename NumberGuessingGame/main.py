import random
import time

print("*********************************\n"
      "Number Guessing Game\n"
      "Guess a number between 1 and 50\n"
      "*********************************")

randomNumber = random.randint(1,50)
rightToGuess = 7

while True:
    guess = int(input("Your Guess:"))
    if(guess < randomNumber):
        print("Information is being questioned...")
        time.sleep(1)

        print("Guess a higher number")
        rightToGuess -= 1

    elif(guess>randomNumber):
        print("Information is being questioned...")
        time.sleep(1)

        print("Guess a lower number")
        rightToGuess -= 1
    else:
        print("Information is being questioned...")
        time.sleep(1)

        print("Congrats! Number:",randomNumber)
        break
    if(rightToGuess==0):
        print("You no longer have the right to guess.\nGame Over!")
        break
