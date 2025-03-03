import random                 # imported Random function .
numbers = random.randint(1, 70)     # Used to generate a random integer from 1 to 70.
userattempt = 0               # User attempt starting from zero.
print("guess your number from 1 to 70")
while True:                   # Used while loop to start infinite loop.
    guess = int(input("enter your number:"))
    userattempt += 1          # user attempt will increase from 1 to until the user find correct number.
    if guess > numbers:       # Used Conditional statements to find the number entered by the user is high or low.
        print("The number you have guessed is  high")
    elif guess < numbers :
        print("The number you have guessed is low ")  # Used to display or to print desired message on screen
    else:
        print(f"Hurray ! you have guessed  the number correctly in {userattempt} attempts") # Used Formatted string to declare variable in print statement.
        break                 # Used to exit from the loop


