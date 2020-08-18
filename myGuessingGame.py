# Create a file name 'game.py.

# Using a Python module name "random"
import random

#Prompt user to enter their name and store it to a variable named "player_name".
player_name = input("Hello, what is your name?")

#Use random module to generate a number between 1 and 10.
number = random.randint(1,10)

#Create a variable named "number_of_guesses".
number_of_guesses = 0

#Printing a string that includes the player's name.
print('Okay '+ player_name+', try to guess the number that I am thinking between 1 and 10:')

#Creating a while loop
while number_of_guesses < 5:

#Converting user input with Python's 'int()' method
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('You guessed too low!')
    if guess > number:
        print('Try again, your guess is too high!')
    if guess == number:
        break
if guess == number:
    print('You guessed it right! ' + str(number_of_guesses) + ' attempts!')
else:
    print('You got it wrong! It was ' + str(number))




