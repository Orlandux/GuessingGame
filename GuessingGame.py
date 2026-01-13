#Dominick Orlando 
#CIS 261 
#Guessing Game Introduction
 
import random 


print("Guess the number!")

play_again = "y"

while play_again == "y":

    limit = int(input("Enter the limit: "))
    print("I'm thinking of a number from 1 to", limit) 
    tries = 0 
    number = random.randint(1, limit) 

    while True:
        guess = int(input("Your guess: ")) 
        tries += 1

        if guess == number: 
            print("Your guessed it right in", tries, "tries!")
            break 
        elif guess > number:
            print("Too high. Try again.")
        else:
            print("Too low. Try again.")

    play_again = input("Play again? (y/n): ") 

print("Thanks for playing!")
