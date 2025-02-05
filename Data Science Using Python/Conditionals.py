### Step 1: Import the required libraries

import random

### Step 2: Initialize the variables

number = random.randint(1,9)
guess = 0
count = 0

### Step 3: Implement the logic of the guessing game in which user is going to
# guess the number between 1 to 9 and system will tell them whether they have
# guessed too low, too high, or exactly right.

print("Welcome To The Guessing Game")
while count != 6:
    guess = input("Guess the number between 1 to 9:")
    guess = int(guess)
    count += 1
    if guess < number:
            print("Too low!")
    elif guess > number:
            print("Too high!")
    else:
            print("You got it!")
            print("And it only took you",count,"tries!")
            break