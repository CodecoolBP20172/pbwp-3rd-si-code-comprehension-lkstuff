# guessing the number game with five try

import random   # import the random module from standard library

guessesTaken = 0    # assign variable to zero

print('Hello! What is your name?')  # print a  message
myName = input()                    # assign the user input to a variable

number = random.randint(1, 20)      # generate a random number between 1 and 20 and assign it to the number variable
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') # print a message concatenate it with the input value

while guessesTaken < 6:             #  start a loop until the variable value less than six
    print('Take a guess.')          # print message to the user
    guess = input()                 # assign a user input to a variable
    guess = int(guess)              # change the type of the value of the variable to interger

    guessesTaken += 1               # raise the variable value by one

    if guess < number:              # compare two  variables if the value of the right is greater
        print('Your guess is too low.')  # message if conditional statement is true

    if guess > number:              # compare two  variables if the value of the left is greater
        print('Your guess is too high.')  # message if conditional statement is true

    if guess == number:                 # compare two  variables if they are equal .
        break                           # if if conditional statement is true, exit from the loop continue in next block(line29)

if guess == number:                     # compare two  variables if they are equal
    guessesTaken = str(guessesTaken)    # if  conditional statement is true, change the type of variable to string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!') # if  conditional statement is true, message concatenate the message with two variable

if guess != number:                     #compare two  variables if they are not equal .
    number = str(number)                # if  conditional statement is true, change the type of variable to string.
    print('Nope. The number I was thinking of was ' + number) # if  conditional statement is true, message concatenate the message with one variable
