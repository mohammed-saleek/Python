#Guessing Game lmao

#importing os to clear screen
#import os

#This is the secret number
#secret_number = int(input("Enter the secret number:"))
secret_number = 9

#clearing screen after the secret number is given
#os.system('cls')

#Number of chances
guess_limit = 3

guess_count = 0

#while condition
while guess_count < guess_limit:
    # Guessed Number
    guess = int(input("Guess:"))
    guess_count += 1
    if guess == secret_number:
        print("You won the game!!!")
        exit()

#else part of while loop
else:
    print("Sorry You failed!!!")

