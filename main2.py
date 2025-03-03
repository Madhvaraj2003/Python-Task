import random                                   # to use random function
languages_list = ["python", "javascript", "java", "automation", "pytest", "guvi", "selenium"] # list of words
computer_choice = random.choice(languages_list) # Computer picks one word from list
scrambled_word = ''.join(random.sample(computer_choice,len(computer_choice)))       # Used random.sample() which shuffles the words.join() functions again joins the scrambled words back.
print("welcome to the languages scramble Guessing game ")
print(f"Unscramble this word: {scrambled_word}")
userattempts = 0         # Attempts starts from zero.
while True:              # Infinite loops starts.
    userattempts += 1    # user attempts increases for every unsuccessful tries.
    guess = input("Enter your answer:")    # Used guess variable.
    if guess != computer_choice :        # Used conditional statements.
        print("you guessed it wrong")
        print("please try again")
    else:
        print(f"you guessed it right in {userattempts} attempts!")
        break             # To exit from the loop


