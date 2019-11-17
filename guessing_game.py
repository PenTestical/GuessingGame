#!usr/bin/python3

import random

while True:
    print("Welcome, Friend! Enjoy this shit, enjoy this shit!")

    number_to_guess = random.randint(1,10)

    count_tries_number = 1
    #main programm to guess the correct number
    guess = int(input("Enter a number between 1-10, my Friend: "))
    while guess != number_to_guess:
        print("False Number, unfortunately!")
        if count_tries_number == 3:
            break
        elif guess < number_to_guess:
            print("Your number was lower than the correct one!")
        else:
            print("Your number was higher than the correct one, yo!")
        close_to_guess_up = number_to_guess + 1
        close_to_guess_down = number_to_guess - 1
        if guess == close_to_guess_up or guess == close_to_guess_down:
            print("Damn, that was very close to the real number!")
        guess = int(input("If you need to cheat enter -1, otherwise try again: "))
        count_tries_number += 1
        if guess == -1:
            print("The correct number is", number_to_guess, ", you cheater!")
            guess = int(input("Try again, cheater: "))
    #after three tries the result will be printed
    if number_to_guess == guess:
        print("YES BABY! You've won!")
        print("You took just", count_tries_number, "goes to complete the game!")
    else:
        print("Loooooooooooooser!")
        print("The correct number was",number_to_guess,", was it that hard?")

    #running the game again, asking for user input
    answer = input("Restart the game (y/n)?: ")
    if answer == "n":
        break
    elif answer == "y":
        continue
    else:
        print("You entered invalid input!")
        break
print("Game Over!")
