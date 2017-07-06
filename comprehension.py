# geussing the number game with five try

import random   # import the random module from standard library

guessesTaken = 0    # assign variable to zero

print('Hello! What is your name?')  # print a  message
myName = input()                    # assign the user input to a variable

number = random.randint(1, 20)      # assign one interger value to a variable using randint method from random modul
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') # print a message using a variable with arithmetic operators

while guessesTaken < 6:             # itarete through variable value if it is less than 6
    print('Take a guess.')          # print message to the user
    guess = input()                 # assign a user input to a variable
    guess = int(guess)              # change the type of the value of the variable to interger

    guessesTaken += 1               # assign a new value to a variable

    if guess < number:              # compare two  variables if the value of the right is greater
        print('Your guess is too low.')  # message if comparsion in this indentation block is true

    if guess > number:              # compare two  variables if the value of the left is greater
        print('Your guess is too high.')  # message if comparsion in this indentation block is true

    if guess == number:                 # compare two  variables if they are equal .
        break                           # if comparsion in this indentation block is true, stop the loop and move to the next line

if guess == number:                     # compare two  variables if they are equal
    guessesTaken = str(guessesTaken)    # if comparsion in this indentation block is true, change the type of variable to string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!') # if comparsion in this indentation block is true, print message using two variables with arithmetic operator. end program.

if guess != number:                     #compare two  variables if they are not equal .
    number = str(number)                # if comparsion in this indentation block is true, change the type of variable to string.
    print('Nope. The number I was thinking of was ' + number) # if comparsion in this indentation block is true, print message using two variables with arithmetic operator. end program
